# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1455063597.584958
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/history/homePage/templates/hotspots.html'
_template_uri = 'hotspots.html'
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
        characters = context.get('characters', UNDEFINED)
        identifiedChars = context.get('identifiedChars', UNDEFINED)
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer(' ')
        __M_writer('\n\n\n<!DOCTYPE html>\n <html lang="en" class="no-js">\n  <meta charset="UTF-8" />\n\n  <title>Hotspot</title>\n\n  <meta name="description" content="" />\n  <meta name="keywords" value="" />\n\n  <link rel="stylesheet" href="/static/homePage/css/layout.css" type="text/css" />\n  <link rel="stylesheet" href="/static/homePage/css/hotspot-map-editor.css" type="text/css" />\n  <!--Minify file above for production\n  <link rel="stylesheet" href="/static/homePage/css/hotspot-map.min.css" type="text/css" /> \n  -->\n  <link rel="stylesheet" href="/static/homePage/css/lib/colorpicker.css" type="text/css" />\n  <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">\n\n  <script src="/static/homePage/js/lib/modernizr-2.min.js"> </script>\n\n</head>\n<body>\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        characters = context.get('characters', UNDEFINED)
        identifiedChars = context.get('identifiedChars', UNDEFINED)
        request = context.get('request', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if identifiedChars == 'no characters':
            __M_writer('  <hr>\n')
        else:
            for i in identifiedChars:
                __M_writer('  <a class = "hotspotInfo" id = ')
                __M_writer(str(i.id))
                __M_writer('\n  data-id = ')
                __M_writer(str(i.id))
                __M_writer('\n  data-x = ')
                __M_writer(str(i.hotspot_x))
                __M_writer('\n  data-y = ')
                __M_writer(str(i.hotspot_y))
                __M_writer('\n  data-width = ')
                __M_writer(str(i.hotspot_width))
                __M_writer('\n  data-height = ')
                __M_writer(str(i.hotspot_height))
                __M_writer('\n')
                if i.sign is None:
                    __M_writer("    data-sign = 'None'\n")
                else:
                    __M_writer('    data-sign = ')
                    __M_writer(str(i.sign.filepath))
                    __M_writer('\n')
                __M_writer('  > </a>\n')
        __M_writer('</div>\n')
        if request.user.is_authenticated():
            __M_writer('  <center><h3>Tag characters and match the correct sign to the character. </h3></center>\n<!--\n<div class="row">\n      <div class="col col s2 offset-s10"><i class="fa fa-angle-right fa-5x"></i>\n-->\n</div>\n</div>\n<div id="shell" data-username=')
            __M_writer(str(request.user))
            __M_writer('>\n  <div id="hb-shell">\n  <!--\n    <div id="hb-top-wrap" class="hb-main-wrap">\n      <div id="hb-global-settings-wrap">\n        <h1>Global Settings</h1>\n        <table>\n          <tr>\n            <td width="100">Show tooltips on: </td>\n            <td>\n              <select id="show-select" autocomplete="off">\n                <option value="mouseover" selected>Mouseover</option>\n                <option value="click">Click</option>\n                <option value="always">Always Visible</option>\n              </select>\n              <div class="form-help">This option determines how the user will trigger the tooltips - when he clicks on the spot, when he hovers the mouse over it, or the tooltips will be visible all the time. This is not active in the content builder.</div>\n            </td>\n          </tr>\n          <tr>\n            <td width="100">Responsive: </td>\n            <td>\n              <input type="checkbox" id="checkbox-responsive">\n              <div class="form-help">If this is checked, the widget will be as wide as it\'s parent, while still preserving the image ratio. If not checked, the widget\'s size will be as the size of the image.</div>\n            </td>\n          </tr>\n        </table>\n      </div>\n    </div>\n    <div id="hb-main-wrap" class="hb-main-wrap">\n      <div id="hb-settings-wrap">\n        <h2>Selected Spot Settings</h2>\n        <table>\n          <tr>\n            <td width="100">Spot visibility: </td>\n            <td>\n              <select id="visible-select">\n                <option value="visible">Visible</option>\n                <option value="invisible" selected>Invisible</option>\n              </select>\n              <div class="form-help">Determines the visibility of the spot. If set to "invisible", the user will not know that there is a spot, unless he triggers it. <br />The spot will not look the same in the final product as it looks in the content builder.</div>\n            </td>\n          </tr>\n          <tr>\n            <td width="100">Tint Color: </td>\n            <td>\n              <input type="text" id="input-tint-color">\n            </td>\n          </tr>\n          <tr>\n            <td width="100">Tooltip width: </td>\n            <td>\n              <input type="text" id="tooltip-width">\n              <input type="checkbox" id="tooltip-auto-width" checked value="Auto"><label for="tooltip-auto-width">Auto</label>\n              <div class="form-help">If you need a fixed value for the tooltip set a number in pixels (without "px") in the text field. If you don&#39;t, then check "Auto".</div>\n            </td>\n          </tr>\n          <tr>\n            <td>Popup position: </td>\n            <td>\n              <select id="position-select">\n                <option value="left" selected>Left</option>\n                <option value="right">Right</option>\n                <option value="top">Top</option>\n                <option value="bottom">Bottom</option>\n              </select>\n              <div class="form-help">Choose where you want the popup to appear, relative to the spot that it belongs to.</div>\n            </td>\n          </tr>\n          <tr>\n            <td>Content: </td>\n            <td>\n              <textarea id="content" autocomplete="off"></textarea>\n            </td>\n          </tr>\n          <tr><td>&nbsp;</td><td>&nbsp;</td></tr>\n          <tr>\n            <td>Delete?</td>\n            <td><input type="button" id="delete" value="Delete Spot"></td>\n          </tr>\n        </table>\n      </div>\n      -->\n      <div id="hb-map-wrap">\n         <img id =\'Tablet\' src ="/static/homePage/images/Tablets/KUG03-obv-01.jpg">\n      </div>\n      <div class="clear"></div>\n    </div>\n    \n\t<!--\n    <div id="hb-bottom-wrap" class="hb-main-wrap">\n      <h1>Live Preview</h1>\n      <div id="hb-live-preview"></div>\n    </div>\n    <div id="hb-bottom-wrap" class="hb-main-wrap">\n      <div class="left">\n        <h1>HTML Code</h1>\n        <textarea id="hb-html-code" autocomplete="off"></textarea>\n      </div>\n\n      <div class="right">\n        <h1>JavaScript Code</h1>\n        <textarea id="hb-javascript-code" autocomplete="off"></textarea>\n      </div>\n      <div class="clear"></div>\n    </div>\n    -->\n  </div>\n  <div>\n    <p class = \'success\'></p>\n  <div>\n')
        else:
            __M_writer('   <div>\n    <form method="POST">\n        ')
            __M_writer(str( form ))
            __M_writer('\n        <div class="row">\n        <br>\n          <div class="col-md-7">\n            <input type="submit" value="Sign In" class="btn btn-cta-secondary pull-right push-bottom" data-loading-text="Loading...">\n          </div>\n        </div>\n      </form>\n    </div>\n')
        __M_writer('</div>\n<div id = "Assyrian_sign" class = "inline" style = " bottom: 0px; background-color: black; position: fixed; width: 100%; z-index: 10000">\n  <ul class="social-icons list-inline draggable-char col-md-12 col-sm-12 col-xs-12">\n')
        for object in characters:
            __M_writer('      <li><img id = "Sign')
            __M_writer(str(object.Sign.id))
            __M_writer('" data-id = ')
            __M_writer(str(object.Sign.id))
            __M_writer(' class = "Individual_signs" src="')
            __M_writer(str(object.Sign))
            __M_writer('"></li>\n')
        __M_writer('  </ul>\n</div>\n  <script src="/static/homePage/js/lib/jquery.min.js"></script>\n<script src="/static/homePage/js/lib/colorpicker.js"></script>\n  <script src="/static/homePage/js/hotspot-map-editor.js"></script>\n  <script src="/static/homePage/js/hotspot-map.min.js"></script>\n  <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>\n</body>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"28": 0, "39": 1, "40": 1, "50": 25, "60": 25, "61": 26, "62": 27, "63": 28, "64": 29, "65": 30, "66": 30, "67": 30, "68": 31, "69": 31, "70": 32, "71": 32, "72": 33, "73": 33, "74": 34, "75": 34, "76": 35, "77": 35, "78": 36, "79": 37, "80": 38, "81": 39, "82": 39, "83": 39, "84": 41, "85": 44, "86": 45, "87": 46, "88": 53, "89": 53, "90": 163, "91": 164, "92": 166, "93": 166, "94": 176, "95": 179, "96": 180, "97": 180, "98": 180, "99": 180, "100": 180, "101": 180, "102": 180, "103": 182, "109": 103}, "filename": "/Users/benmackley/Projects/history/homePage/templates/hotspots.html", "uri": "hotspots.html"}
__M_END_METADATA
"""
