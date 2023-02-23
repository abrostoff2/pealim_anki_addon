* handle formatted urls - right now throws error when given a link
* add less values

@font-face {
 font-family: 'yoav';
 src: url('_YoavCursive.woff2') format('woff2');
}

.card {
 font-family: arial;
 font-size: 15px;
 line-height: 95%;


 display: -webkit-box;

 width: 100%;
 height: 100%;
 margin: auto;

 text-align: center;
 word-wrap: break-word;
 hyphens: auto;


 -webkit-box-align: stretch;
 -webkit-box-pack: center;
 -webkit-box-orient: vertical;

}
#back {
}

.mobile .card {
 max-width: none;
 max-height: none;
 margin: 0 0 0 0;
}

.replaybutton {
 font-size: 25px;
}

#out {
 position: absolute;
 z-index: 1;
 top: 0;
 right: 0;
 bottom: 0;
 left: 0;

 display: table;

 width: 100%;
 height: 100%;
}

#inn {
 display: table-cell;

 vertical-align: middle;
}

.typeMissed {
 color: inherit !important;
 background: inherit !important;
}

.typeGood {
 color: inherit !important;
 background: #8be68b !important;
}

.typeBad {
 color: inherit !important;
 background: #ff9a9a !important;
}

.tycol.ז code#typeans { color: #0169CE; }
.tycol.נ code#typeans { color: #88001B; }
.tycol.פָּעַ code#typeans { color: #B1850B; }
.tycol.פִּעֵ code#typeans { color: #077456; }
.tycol.הִפְ code#typeans { color: #33137A; }
.tycol.הִתְ code#typeans { color: #AAB00B; }
.tycol.הֻפְ code#typeans { color: #C1368D; }
.tycol.פֻּעַ code#typeans { color: #2B9709; }
.tycol.נִפְ code#typeans { color: #B2400A; }
.ז { background-color: #D9ECFF; }
.נ { background-color: #FEE2E8; }
.פָּעַ { background-color: #FFF5D9; }
.פִּעֵ { background-color: #D9F9F0; }
.הִפְ { background-color: #E9E1FA; }
.הִתְ { background-color: #FDFFD3; }
.הֻפְ { background-color: #FCDFF1; }
.פֻּעַ { background-color: #E7FDE0; }
.נִפְ { background-color: #FFE7DC; }

.ז, .נ, .פָּעַ, .פִּעֵ,.הִפְ, .הִתְ, .הֻפְ, .פֻּעַ, .נִפְ { color: black; }

.night_mode.ז { color: #1E90FF; }
.night_mode.נ { color: #DC143C; }
.night_mode.פָּעַ { color: #F68546; }

.heb b {
 font-weight: normal;
}

.ז .heb b, .ז .col { color: #1E90FF; }
.נ .heb b, .נ .col { color: #DC143C; }
.פָּעַ .heb b, .פָּעַ .col { color: #F6C746; }
.פִּעֵ .heb b, .פִּעֵ .col { color: #2EA181; }
.הִפְ .heb b, .הִפְ .col { color: #5E3CA9; }
.הִתְ .heb b, .הִתְ .col { color: #DAE21B; }
.הֻפְ .heb b, .הֻפְ .col { color: #E27FBD; }
.פֻּעַ .heb b, .פֻּעַ .col { color: #5FD13B; }
.נִפְ .heb b, .נִפְ .col { color: #F77F3445; }
.heb b, .col { color: #ccddff; }

#main {
 line-height: 82px;

 vertical-align: middle;
}

.bl {
 display: block;
}

.op#ext {
 font-size: 24px;
}

#ext {
 font-size: 35px;
 line-height: 50px;
}

#pea {
 font-size: 30px;
 line-height: 50px;

 display: block;

 color: #817f7f;
}

span.v {
 display: inline !important;
}

#ext br {
 display: block;

 margin: 0 0;

 content: ' ';
}

#typeans,
#hide {
 font-family: arial;
 font-size: 54px;

 width: auto;
}

:not(.eng) > br {
 display: block;

 margin: 24px 0;

 content: ' ';
}

a {
 text-decoration: inherit;

 color: inherit !important;
}

code#typeans {
 font-size: 80px;
}

.gra {
 display: none;
}

.cur {
 font-family: yoav;
 font-size: 90px;
 line-height: .7;

 display: none;
}

#ext .cur {
 font-size: 48px;
}

.wrapper:hover#main {
 font-family: yoav;
}

.cur code#typeans {
 font-family: yoav;
 font-size: 90px;
 line-height: .74;
}

.wrapper {
 overflow: hidden;
}

.wrapper:hover .cur,
.wrapper:hover .gra {
 display: inline;
 overflow: hidden;
}

.wrapper:hover .reg {
 display: none;
}

table {
 line-height: 1.33;

 margin-right: auto;
 margin-left: auto;

 border-spacing: 1px 1px;

 text-align: center;

 background-color: white;
}

tr.bord {
 height: 1px;
}

tr.cont {
 color: #0169ce;
 background-color: #d9ecff;
}

td:not([colspan]):nth-child(2),
td:nth-child(4) {
 color: #88001b;
 background-color: #fee2e8;
}

.cont {
 display: none;
 overflow: hidden;
}

.butt {
 color: white;
 background-color: #d5d5d5;
}

.butt:hover {
 background-color: #9099a2;
}

.w {
 background-color: #d7d9f2;
}

ruby {
 display: inline-flex;
 flex-direction: column-reverse;

 ruby-align: center;
 ruby-position: under;
}

ruby rt {
 line-height: .75;

 display: none;

 color: #817f7f;
}

tr ruby rt {
 color: black;
}

ruby:hover rt {
 display: block;
}

.heb {
 font-size: 30px;
 line-height: 32pt;
}

text {
 font-family: Arial;
}

.heb:hover {
 font-family: yoav;
 font-size: 38px;
 line-height: 42px;
}

.eng {
 font-family: arial;
 font-size: 18px;

 display: none;
}

.heb:hover .eng {
 display: block;

 color: #c9362e;
}

img {
 max-height: 258px !important;
 max-weight: 258px !important;
}

#imgBg {
 position: absolute;
 z-index: -1;

 width: 100%;
 /*overflow: hidden;*/
 font-size: 200%;
}

#imgBg > img {
 opacity: .5;
}

.night_mode polygon {
 fill: white;
}

.op {
 opacity: .33;
}

#typeans:not(code) {
 padding: 0;

 text-align: center;
 /*padding: 0 .5em 0 .5em;*/

 color: inherit !important;
 border-width: 0 0 1px;
 border-color: rgba(255,255,255, .75) !important;
 background-color: inherit !important;
 border-style: none;
}

#hide {
 /*padding: 0 .5em 0 .5em;*/
 position: absolute;

 overflow: hidden;

 height: 0;
 margin: 0;
 padding: 0;

 white-space: pre;
}

.night_mode #typeans {
 background-color: inherit;
}

.right {
 right:25px;
}
.bottom {
 position:fixed;
 bottom:5px;
 z-index:1;
}

button#play {
 border: 1px solid #999;
 background: #eef;
}

#audio svg {
 display: inline;

 width: 48px;
 min-width: 12px;
 height: 25px;
 min-height: 12px;

 stroke: none;
 fill: black;
}

#audio text {
 fill: white;
}

polygon, .night_mode #audio text {
 fill: black;
}

.night_mode polygon {
 fill: white;
}

#blink {
 fill: rgba(0,0,0,0);
}

#blink:active {
 fill: rgba(255,255,255,1);
}

::placeholder {
 color: #686868;
}

.heb {
 display: none;
}

.card1 :not(#back *) > .eng {
 display: none;
}

.riddle b {
 color: rgba(0,0,0,0);
 border: dotted 1px black;
}

.night_mode .riddle b {
 border: dotted 1px white;
}