from anki.hooks import addHook
from aqt.utils import tooltip
from .convert import translate
from aqt.utils import showInfo, qconnect



def populate_fields(editor):
    """triggers _populate_fields"""
    editor.saveNow(lambda: _populate_fields(editor))

def next_option(i):
    return i


def _populate_fields(editor):
    """method that takes the user input and runs translate"""
    user_input = editor.note.fields[0]
    vals = translate(user_input)

    for idx, val in enumerate(vals):
        editor.note.fields[idx] = val
        editor.loadNote()
    editor.note.add_tag(vals[4])
    editor.loadNote()



def add_auto_button(buttons, editor):
    """function that creates auto button. When pressed, it triggers the populate_fields method"""
    auto_button = editor.addButton(
        icon=None,
        cmd="פע",
        func=populate_fields,
        tip="Download from Pealim",
        toggleable=False,
        label="",
        keys=None,
        disables=False,
    )
    buttons.append(auto_button)
    return buttons



addHook("setupEditorButtons", add_auto_button)

