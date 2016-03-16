# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457581959.076769
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/ancientassyrian/homePage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('<!DOCTYPE html>\n')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="section no-pad-bot" id="index-banner">\n    <div class="container">\n      <br><br>\n      <h1 class="header center amber-text">Assyrian Project</h1>\n      <div class="row center">\n        <h5 class="header col s12 light">The Assyrian Project was formed to index over 10,000 ancient Assyrian tablets.  Cuneiform tablets were written using clay and a stylus.  Although not as efficient as modern day tablets, the documents preserved extremely well and contained important data - mostly business information from transactions between wealthy mercants. Tablets were hard to make, and so the whole tablet was utilized for writing - even the sides! </h5>\n      </div>\n      <div class="row center">\n        <a class="btn-large waves-effect waves-light amber modal-trigger" href="#modal2" >Get Started</a>\n      </div>\n      <br><br>\n    </div>\n  </div>\n\n  <div class="container">\n    <div class="section">\n\n      <!--   Icon Section   -->\n      <div class="row">\n        <div class="col s12 m4">\n          <div class="icon-block">\n            <h2 class="center light-blue-text"><i class="large material-icons">broken_image</i></h2>\n            <h5 class="center">Seperate image based on lines</h5>\n\n            <p class="light">The first step to indexing the tablets is to seperate the images into lines.  Much like regular lined paper, Assyrians divided their tablets into lines to segement their writing.  Knowing which characters are in which line helps with indexing processes so that the text can be transliterated into a readable form.  </p>\n          </div>\n        </div>\n\n        <div class="col s12 m4">\n          <div class="icon-block">\n            <h2 class="center light-blue-text"><i class="large material-icons">crop</i></h2>\n            <h5 class="center">Crop Characters</h5>\n\n            <p class="light">Identifying hotspots is the first step for understanding these ancient documents.  Writing with a stylus on clay is much like handwriting - each person has their unique way of forming the characters, and because the characters are not uniform, a computer has a difficulty trying to determine which character is which character.  That is where human intervention is so helpful. </p>\n          </div>\n        </div>\n\n        <div class="col s12 m4">\n          <div class="icon-block">\n            <h2 class="center light-blue-text"><i class="large material-icons">select_all</i></h2>\n            <h5 class="center">Match the Character with its symbol</h5>\n\n            <p class="light">With each character identified, it has to be linked to its symbol in the Assyrian alphabet.  Since the number of people that can read Assyrian in the world is limited to a handful of people, we simplified the transliteration.  Identifying the characters is as simple as a matching game!</p>\n          </div>\n        </div>\n      </div>\n\n    </div>\n    <br><br>\n\n    <div class="section">\n\n    </div>\n    <!--\n  </div>\n    <div class = "section red lighten-5">\n      <div class="container">\n        <p> Four thousand years ago, Assyrian merchants traversed plains and crossed mountains to truck and sell goods for a profit. To accomplish their trade, they wrote documents. Lots of documents. [put a map behind this text with people moving I have a clip we can use]\n        </p>\n      </div>\n    </div>\n    <div class = "section red lighten-4">\n      <div class="container">\n      <p>\n       Today we have recovered more than 23,000 of these documents. This is the earliest collection of documents in the world that tells us about private trade. \n        [put a picture of lots of tablets behind this picture]\n      </p>\n      </div>\n    </div>\n    <div class = "section">\n      <div class="container">\n      <p>\n         Most documents come from a site in Turkey: K&uuml;ltepe. Its ancient name was Kanesh. Many of the merchants had an office here in a neighborhood at the foot of the large acropolis. \n\n        [picture of Kanesh]\n      </p>\n      </div>\n    </div>\n     <div class = "section red lighten-5">\n      <div class="container">\n      <p>\n       The documents are made of clay, and the characters were created by impressing a stylus into the clay, making characters by arranging the wedge&#45;shaped impressions.\n        [put a close up of cuneiform behind this picture]\n        Cuneiform is Latin for "wedge-shaped" \n      </p>\n      </div>\n      </div>\n    <div class = "section">\n      <div class="container">\n      <p>\n       Most of the tablets are the size of cell phone or smaller. \n      [I&#39;ll get a pic of tablet in my hand]\n\n\n      Writers made the most of some tablets. They started at the top of one side, wrote all the way down, continuing around the bottom, then up the back until they arrived at the point where they started. \n      If they still needed space, they wrote in the left edge.\n\n      [appropriate pictures here]\n\n\n      Thousands of merchants were involved in the trade. They had names like:\n      </p>\n    </div>\n    </div>\n     <div class = "section red lighten-4">\n      <div class="container">\n      <p>\n       We are confident that most of these people, both men and women, read and wrote their own documents. \n      [some quote from a letter with a picture of the cuneiform behind it]\n      But we want to prove this more rigorously. \n\n      One way to do this is to compare the handwriting of all documents.\n\n      [picture of two different UD signs from the different letters]\n\n      You can help. \n      We need to clip up our images, so we can compare all the \n      UD characters:\n\n      EN characters:\n\n      and all the other characters\n\n      Here&#39;s how: \n\n      </p>\n    </div>\n      -->\n  </div>\n\n  <div class="page-footer red lighten-3">\n    <div class="container">\n      <div class="row">\n        <div class="col l6 s12">\n          <h5 class="white-text">Copywrite &copy; 2015 by Edward Stratford and Benjamin Mackley</h5>\n          <p class="grey-text text-lighten-4">Images used curteousy of edli.</p>\n\n\n        </div>\n        <!--\n        <div class="col l3 s12">\n          <h5 class="white-text">Settings</h5>\n          <ul>\n            <li><a class="white-text" href="#!">Link 1</a></li>\n          </ul>\n        </div>\n        <div class="col l3 s12">\n          <h5 class="white-text">Connect</h5>\n          <ul>\n            <li><a class="white-text" href="#!">Link 1</a></li>\n          </ul>\n        </div>\n        -->\n      </div>\n    </div>\n    <div class="footer-copyright">\n      <div class="container">\n      Made by <a class="red-text text-lighten-1" href="http://benjaminmackley.com">Mackley Design</a>\n      </div>\n    </div>\n  </div>\n\n\n  <!--  Scripts-->\n  <script src="https://code.jquery.com/jquery-2.1.1.min.js"></script>\n  <script src="../../bin/materialize.js"></script>\n  <script src="js/init.js"></script>\n\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "36": 2, "53": 3, "41": 174, "59": 53, "28": 0, "47": 3}, "source_encoding": "ascii", "uri": "about.html", "filename": "/Users/benmackley/Projects/ancientassyrian/homePage/templates/about.html"}
__M_END_METADATA
"""
