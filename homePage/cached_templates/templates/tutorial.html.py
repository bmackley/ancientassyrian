# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457112783.636096
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/ancientassyrian/homePage/templates/tutorial.html'
_template_uri = 'tutorial.html'
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
        __M_writer(' ')
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n<center><h1>How to Identify Hotspots</h1>\n   <div class = "row">\n  <!-- Block to Show Animation -->\n    <div class="col s6 m4 offset-m1 l3 offset-l2">\n      <div id="animate">\n        <div class="card medium">\n            <div class="card-image">\n              <img id = "animate_img" src ="/static/homePage/images/Tutorial_character.jpeg" > \n            </div>\n            <div class="card-content">\n              The most important part is creating the hotspots for each character. \n            </div>\n            <div class="card-action">\n               <a class="animate waves-effect waves-teal btn-flat">Animate</a>\n            </div>\n        </div>\n      </div>\n      <div id ="animate_box">\n      </div>\n    </div>\n  <!-- User test block -->\n    <div class="col s6 m4 offset-m2 l3 offset-l2">\n        <div class="card medium">\n          <div class="card-image">\n            <div id="hb-map-wrap">\n              <img id="Tablet1" src ="/static/homePage/images/Tutorial_character.jpeg" > \n            </div>\n          </div>\n          <div class="card-content">\n            Try it out! Click and drag the mouse to create a hotspot that covers the whole character.  \n          </div>\n          <div id ="check_hotspot" class="card-action">\n            <a href="#">Check Hotspot</a>\n          </div>\n      </div>\n  </div>\n \n\n<div id="modal_continue" class="modal">\n    <div class="modal-content">\n      <p>Congratulations! Now that you have the basic concept down, we are going to take it up a notch.  </p>\n    </div>\n    <div class="modal-footer">\n      <a href="/homePage/hotspots" class=" modal-action modal-close waves-effect waves-green btn-flat">Let&#8217;s Go!</a>\n    </div>\n  </div>\n\n\n\n\n\n<script src="/static/homePage/js/lib/jquery.min.js"></script>\n<script src="/static/homePage/js/lib/colorpicker.js"></script>\n<script src="/static/homePage/js/tutorial.js"></script>\n<script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>\n<script src="/static/base_app/styles/plugins/bootstrap/js/bootstrap.js">\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "tutorial.html", "filename": "/Users/benmackley/Projects/ancientassyrian/homePage/templates/tutorial.html", "source_encoding": "ascii", "line_map": {"35": 1, "36": 1, "52": 2, "58": 52, "28": 0, "46": 2}}
__M_END_METADATA
"""
