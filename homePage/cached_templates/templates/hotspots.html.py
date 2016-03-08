# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457390013.004108
_enable_loop = True
_template_filename = '/Users/benmackley/Projects/ancientassyrian/homePage/templates/hotspots.html'
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
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        identifiedChars = context.get('identifiedChars', UNDEFINED)
        characters = context.get('characters', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(' ')
        __M_writer('\n\n\n<!DOCTYPE html>\n<html lang="en" class="no-js">\n<head>\n    <meta charset="UTF-8" />\n    <title>Hotspot</title>\n    <meta name="description" content="" />\n    <meta name="keywords" value="" />\n    <link rel="stylesheet" href="/static/homePage/css/layout.css" type="text/css" />\n    <link rel="stylesheet" href="/static/homePage/css/hotspot-map-editor.css" type="text/css" />\n    <!--Minify file above for production\n    <link rel="stylesheet" href="/static/homePage/css/hotspot-map.min.css" type="text/css" /> \n    -->\n    <link rel="stylesheet" href="/static/homePage/css/lib/colorpicker.css" type="text/css" />\n    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">\n    <script src="/static/homePage/js/lib/modernizr-2.min.js"> </script>\n</head>\n<body>\n    ')
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
        request = context.get('request', UNDEFINED)
        identifiedChars = context.get('identifiedChars', UNDEFINED)
        characters = context.get('characters', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if identifiedChars == 'no characters':
            __M_writer('        <hr>\n')
        else:
            for i in identifiedChars:
                __M_writer('        <a class = "hotspotInfo" id = ')
                __M_writer(str(i.id))
                __M_writer('\n        data-id = ')
                __M_writer(str(i.id))
                __M_writer('\n        data-x = ')
                __M_writer(str(i.hotspot_x))
                __M_writer('\n        data-y = ')
                __M_writer(str(i.hotspot_y))
                __M_writer('\n        data-width = ')
                __M_writer(str(i.hotspot_width))
                __M_writer('\n        data-height = ')
                __M_writer(str(i.hotspot_height))
                __M_writer('\n')
                if i.sign is None:
                    __M_writer("          data-sign = 'None'\n")
                else:
                    __M_writer('          data-sign = ')
                    __M_writer(str(i.sign.filepath))
                    __M_writer('\n')
                __M_writer('        > </a>\n')
        __M_writer('    <div>\n        <center><h3>Tag characters and match the correct sign to the character. </h3></center>\n    </div>\n    <div id="shell" data-username=')
        __M_writer(str(request.user))
        __M_writer('>\n        <div id="hb-shell">\n            <div id="hb-map-wrap">\n                <img id =\'Tablet\' src ="/static/homePage/images/Tablets/KUG03-obv-01.jpg">\n            </div>\n        </div>\n    </div>\n    <div id = "Assyrian_sign" class = "inline" style = " bottom: 0px; background-color: black; position: fixed; width: 100%; z-index: 10000"><span style="color: white;" id = "line_text" >Line 1</span>\n      <ul class="social-icons list-inline draggable-char col-md-12 col-sm-12 col-xs-12">\n            <!--Found the code to center vertically online at http://zerosixthree.se/vertical-align-anything-with-just-3-lines-of-css/ and it worked like a charm-->\n            <li style="position: relative; top:50%; transform: translateY(-50%);" id = "previous_line" ><i class="fa fa-arrow-circle-left fa-4x fa-inverse "></i></li>\n')
        for object in characters:
            __M_writer('              <li id ="List')
            __M_writer(str(object.line))
            __M_writer(str(object.positionNO))
            __M_writer('"><img id = "Sign')
            __M_writer(str(object.line))
            __M_writer(str(object.positionNO))
            __M_writer('" data-id = ')
            __M_writer(str(object.line))
            __M_writer(str(object.positionNO))
            __M_writer(' data-sign = ')
            __M_writer(str(object.Sign.id))
            __M_writer(' data-line = ')
            __M_writer(str(object.line))
            __M_writer(' class = "Individual_signs" src="')
            __M_writer(str(object.Sign))
            __M_writer('"></li>\n')
        __M_writer('            <li style="position: relative; top:50%; transform: translateY(-50%);" id = "next_line"><i class="fa fa-arrow-right fa-4x fa-inverse "></i></li>\n      </ul>\n    </div>\n    <script src="/static/homePage/js/lib/jquery.min.js"></script>\n    <script src="/static/homePage/js/lib/colorpicker.js"></script>\n    <script src="/static/homePage/js/hotspot-map-editor.js"></script>\n    <script src="/static/homePage/js/hotspot-map.min.js"></script>\n    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>\n</body>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "hotspots.html", "source_encoding": "ascii", "line_map": {"28": 0, "38": 1, "39": 1, "49": 21, "58": 21, "59": 22, "60": 23, "61": 24, "62": 25, "63": 26, "64": 26, "65": 26, "66": 27, "67": 27, "68": 28, "69": 28, "70": 29, "71": 29, "72": 30, "73": 30, "74": 31, "75": 31, "76": 32, "77": 33, "78": 34, "79": 35, "80": 35, "81": 35, "82": 37, "83": 40, "84": 43, "85": 43, "86": 54, "87": 55, "88": 55, "89": 55, "90": 55, "91": 55, "92": 55, "93": 55, "94": 55, "95": 55, "96": 55, "97": 55, "98": 55, "99": 55, "100": 55, "101": 55, "102": 55, "103": 57, "109": 103}, "filename": "/Users/benmackley/Projects/ancientassyrian/homePage/templates/hotspots.html"}
__M_END_METADATA
"""
