from pathlib import Path
from typing import List, NamedTuple

import requests
from bs4 import BeautifulSoup as bs
from jinja2 import Environment, FileSystemLoader

templates_dir = Path(__file__).parent
templates_dir = templates_dir.absolute()

env = Environment(loader=FileSystemLoader(templates_dir))
template = env.get_template("verb_he_en.html")

pealim_to_jinja = {
    "AP-ms": "p_x_s_m",
    "AP-fs": "p_x_s_f",
    "AP-mp": "p_x_p_m",
    "AP-fp": "p_x_p_f",
    "PERF-1s": "pp_1_s_x",
    "PERF-1p": "pp_1_p_x",
    "PERF-2ms": "pp_2_s_m",
    "PERF-2fs": "pp_2_s_f",
    "PERF-2mp": "pp_2_p_m",
    "PERF-2fp": "pp_2_p_f",
    "PERF-3ms": "pp_3_s_m",
    "PERF-3fs": "pp_3_s_f",
    "PERF-3p": "pp_2_p_x",
    "IMPF-1s": "f_1_s_x",
    "IMPF-1p": "f_1_p_x",
    "IMPF-2ms": "f_2_s_m",
    "IMPF-2fs": "f_2_s_f",
    "IMPF-2mp": "f_2_p_m",
    "IMPF-2fp": "f_2_p_f",
    "IMPF-3ms": "f_3_s_m",
    "IMPF-3fs": "f_3_s_f",
    "IMPF-3mp": "f_3_p_m",
    "IMPF-3fp": "f_3_p_f",
    "IMP-2ms": "im_2_s_m",
    "IMP-2fs": "im_2_s_f",
    "IMP-2mp": "im_2_p_m",
    "IMP-2fp": "im_2_p_f",
    "INF-L": "inf",
}


class HebrewCard(NamedTuple):
    Hebrew: str
    Definition: str
    Gender: str
    PartOfSpeech: str
    Shoresh: str
    Audio: str
    Inflections: str
    Extended: str
    Image: str

    def __post_init__(self):
        """Perform validation on Gender, PartOfSpeech"""
        if self.Gender not in ["", "נ", "ז", "פָּעַ", "פִּעֵ", "הִפְ", "הִתְ", "נִפְ"]:
            self.Gender = ""

        if self.PartOfSpeech not in ["n", "v", "a", ""]:
            self.PartOfSpeech = ""

    def to_list(self) -> List[str]:
        return [
            self.Hebrew,
            self.Definition,
            self.Gender,
            self.PartOfSpeech,
            self.Shoresh,
            self.Audio,
            self.Inflections,
            self.Extended,
            self.Image,
        ]


def get_language(search_input: str) -> str:
    """Decides if the search term is in hebrew or english

    Args:
        search_input::string

    Returns:
        str: either "english" or "hebrew

    """
    if any("\u0590" <= c <= "\u05EA" for c in search_input):
        return 'hebrew'
    else:
        return 'english'


def is_link(search_input: str) -> bool:
    """decides if the search input is a string or not

    Args:
        search_input::string

    Returns:
        bool:: whether input is a string (True) or not (False)
    """
    if '.com' in search_input:
        return True
    else:
        return False


def search_to_url(search_input: str) -> str:
    """Turns a search into a pealim search url
    Args:
        search_input::string

    Returns:
        str: url from the search
    """
    return f'https://www.pealim.com/search/?q={search_input}'


def search_pealim(search_url: str, language: str) -> list:
    """Finds the table contents for the pealim search
    Args:
        search_url::string
        language::str - language of input, either english or hebrew

    Returns:
        list: list of all the contents for pealim search matches
    """
    resp = requests.get(search_url)
    soup = bs(resp.content, features="html.parser")
    body = soup.body
    if language == 'english':
        table = body.find('tbody')
    if language == 'hebrew':
        table = body.find(class_='verb-search-result')
    return table.contents


def format_search_options(search_content: list) -> list:
    """Finds information about each of the pealim matches including the word, translation, transliteration, href,
    and url

    Args:
        search_content::list

    Returns:
        list: list of dictionary with keys 'word', 'meaning', 'transliteration', href', 'url'
    """
    response = []
    for div in search_content:
        word = div.find("span", class_="menukad").text
        try:
            trans = div.find(class_="dict-transcription").text
            meaning = div.find(class_="dict-meaning").text
        except AttributeError:
            trans = None
            meaning = None
        href = div.find_all('a', href=True)[0]['href']
        url = "https://www.pealim.com" + href
        response.append({'word': word, 'meaning': meaning, 'transliteration': trans, 'href': href, 'url': url})
    return response


def choose_word(search_word_matches: list) -> dict:
    """Chooses one of the words from the search_content and returns their corresponding dictionary

    Args:
        search_word_matches::list
        i:int

    Returns:
        dict: dictionary with keys 'word', 'meaning', 'transliteration', href', 'url' for chosen word
    """
    return search_word_matches[0]


def get_word_url_soup(word_url: str) -> str:  # check the type
    """gets the soup of the word's url

    Args:
        word_url

    Return:
        soup object for word
    """
    resp = requests.get(word_url)
    return bs(resp.content, features="html.parser")


def extract_pos(soup) -> object:
    """
    extracts the pos from the soup object for given word

    Args:
        soup

    Returns:
        object of type HebrewCard
    """

    def get_subheader(soup) -> str:
        return soup.find("h2", class_="page-header").nextSibling.text

    def convert_shoresh(shoresh: str) -> str:
        if not shoresh:
            return
        shoresh = shoresh.replace("-", "־")
        shoresh = "".join(shoresh.split())
        return shoresh

    def extract_binyan(text: str):
        upper = text.upper()
        if "PA'AL" in upper:
            return "פָּעַ"  # pa'al
        elif "PI'EL" in upper:
            return "פִּעֵ"
        elif "HIF'IL" in upper:
            return "הִפְ"
        elif "HITPA'EL" in upper:
            return "הִתְ"
        elif "NIF'AL" in upper:
            return "נִפְ"
        elif "PU'AL" in upper:
            return "פֻּעַ"
        elif "HUF'AL" in upper:
            return "הֻפְ"
        else:
            return ""

    def convert_verb(soup) -> HebrewCard:
        out_dict = {}

        shoresh = soup.find("span", class_="menukad").text
        definition = soup.find("div", class_="lead").text

        inf = None

        for peal, jinj in pealim_to_jinja.items():
            div = soup.find("div", id=peal)
            word = div.find("span", class_="menukad").text
            pron = div.find("div", class_="transcription").text
            td = f"<ruby>{word}<rt>{pron}</rt></ruby>"
            out_dict[jinj] = td

            if peal == "INF-L":
                inf = word

        binyan_p = get_subheader(soup)
        binyan = extract_binyan(binyan_p)

        return HebrewCard(
            Hebrew=inf,
            Definition=definition,
            Gender=binyan,
            PartOfSpeech="v",
            Shoresh=convert_shoresh(shoresh),
            Audio="",
            Inflections=template.render(**out_dict),
            Extended="",
            Image="",
        )

    def convert_noun(soup) -> HebrewCard:
        shoresh = None
        for p in soup.find_all("p"):
            if p.text.startswith("Root:"):
                shoresh = p.find("span").text

        definition = soup.find("div", class_="lead").text

        t1 = soup.find("table", class_="conjugation-table")

        singular = t1.find("div", id="s").find("span", class_="menukad").text
        singular_pr = t1.find("div", id="s").find("div", class_="transcription").text

        plural_div = t1.find("div", id="p")
        plural, plural_pr = "", ""
        if plural_div is not None:
            plural = plural_div.find("span", class_="menukad").text
            plural_pr = plural_div.find("div", class_="transcription").text

        gender = None
        for p in soup.find_all("p"):
            if p.text.startswith("Noun"):
                gender_field = p.text.split(" ")[-1]
                gender = "נ" if "fem" in gender_field else ""
                gender = "ז" if "mas" in gender_field else ""

        return HebrewCard(
            Hebrew=singular,
            Definition=definition,
            Gender=gender,  # TODO
            PartOfSpeech="n",
            Shoresh=convert_shoresh(shoresh),
            Audio="",
            Inflections=plural,
            Extended=f"{singular_pr}, {plural_pr}",
            Image="",
        )

    def convert_adj(soup):
        shoresh = None
        for p in soup.find_all("p"):
            if p.text.startswith("Root:"):
                shoresh = p.find("span").text

        definition = soup.find("div", class_="lead").text

        t1 = soup.find("table", class_="conjugation-table")

        m_singular = t1.find("div", id="ms-a").find("span", class_="menukad").parent.text
        m_singular_pr = t1.find("div", id="ms-a").find("div", class_="transcription").text
        m_plural = t1.find("div", id="mp-a").find("span", class_="menukad").parent.text
        m_plural_pr = t1.find("div", id="mp-a").find("div", class_="transcription").text

        f_singular = t1.find("div", id="fs-a").find("span", class_="menukad").parent.text
        f_singular_pr = t1.find("div", id="fs-a").find("div", class_="transcription").text
        f_plural = t1.find("div", id="fp-a").find("span", class_="menukad").parent.text
        f_plural_pr = t1.find("div", id="fp-a").find("div", class_="transcription").text

        gender = ""

        return HebrewCard(
            Hebrew=f"{m_singular} / {f_singular}",
            Definition=definition,
            Gender=gender,
            PartOfSpeech="n",
            Shoresh=convert_shoresh(shoresh),
            Audio="",
            Inflections=f"{m_plural} / {f_plural}",
            Extended=f"{m_singular_pr} / {f_singular_pr}\n{m_plural_pr} / {f_plural_pr}",
            Image="",
        )

    pos_p = soup.find("h2", class_="page-header").nextSibling.text
    if "noun" in pos_p.lower():
        return convert_noun(soup)
    if "verb" in pos_p.lower():
        return convert_verb(soup)
    if "adjective" in pos_p.lower():
        return convert_adj(soup)

def translate(user_input):
    if is_link(user_input):
        pass
    else:
        url = search_to_url(user_input)
        language = get_language(user_input)
        contents = search_pealim(url, language)
        search_words_dict = format_search_options(contents)
        url_dict = choose_word(search_words_dict)
        soup = get_word_url_soup(url_dict['url'])
        return extract_pos(soup).to_list()

