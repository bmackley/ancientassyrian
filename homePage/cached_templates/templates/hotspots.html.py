# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1457808473.443916
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
        characters = context.get('characters', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        identifiedChars = context.get('identifiedChars', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(' ')
        __M_writer('\n\n\n<!DOCTYPE html>\n<html lang="en" class="no-js">\n<script>\n  (function(i,s,o,g,r,a,m){i[\'GoogleAnalyticsObject\']=r;i[r]=i[r]||function(){\n  (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),\n  m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)\n  })(window,document,\'script\',\'//www.google-analytics.com/analytics.js\',\'ga\');\n\n  ga(\'create\', \'UA-74941206-1\', \'auto\');\n  ga(\'send\', \'pageview\');\n\n</script>\n<head>\n    <meta charset="UTF-8" />\n    <title>Hotspot</title>\n    <meta name="description" content="" />\n    <meta name="keywords" value="" />\n    <link rel="stylesheet" href="/static/homePage/css/layout.css" type="text/css" />\n    <link rel="stylesheet" href="/static/homePage/css/hotspot-map-editor.css" type="text/css" />\n    <!--Minify file above for production\n    <link rel="stylesheet" href="/static/homePage/css/hotspot-map.min.css" type="text/css" /> \n    -->\n    <link rel="stylesheet" href="/static/homePage/css/lib/colorpicker.css" type="text/css" />\n    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/themes/smoothness/jquery-ui.css">\n    <script src="/static/homePage/js/lib/modernizr-2.min.js"> </script>\n</head>\n<body>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        characters = context.get('characters', UNDEFINED)
        def content():
            return render_content(context)
        request = context.get('request', UNDEFINED)
        identifiedChars = context.get('identifiedChars', UNDEFINED)
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
        __M_writer('    <div>\n        <center><h3>Drag the signs onto the image of the tablet and then resize the sign to fit the corresponding sign on the image. </h3></center>\n    </div>\n    <div id="shell" data-username=')
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
        __M_writer('            <li style="position: relative; top:50%; transform: translateY(-50%);" id = "next_line"><i class="fa fa-arrow-circle-right fa-4x fa-inverse "></i></li>\n      </ul>\n    </div>\n    <script src="/static/homePage/js/lib/jquery.min.js"></script>\n    <script src="/static/homePage/js/lib/colorpicker.js"></script>\n    <script src="/static/homePage/js/hotspot-map-editor.js"></script>\n    <script src="/static/homePage/js/hotspot-map.min.js"></script>\n    <script src="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.4/jquery-ui.min.js"></script>\n</body>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/benmackley/Projects/ancientassyrian/homePage/templates/hotspots.html", "uri": "hotspots.html", "line_map": {"28": 0, "38": 1, "39": 1, "49": 31, "58": 31, "59": 32, "60": 33, "61": 34, "62": 35, "63": 36, "64": 36, "65": 36, "66": 37, "67": 37, "68": 38, "69": 38, "70": 39, "71": 39, "72": 40, "73": 40, "74": 41, "75": 41, "76": 42, "77": 43, "78": 44, "79": 45, "80": 45, "81": 45, "82": 47, "83": 50, "84": 53, "85": 53, "86": 64, "87": 65, "88": 65, "89": 65, "90": 65, "91": 65, "92": 65, "93": 65, "94": 65, "95": 65, "96": 65, "97": 65, "98": 65, "99": 65, "100": 65, "101": 65, "102": 65, "103": 67, "109": 103}, "source_encoding": "ascii"}
__M_END_METADATA
"""
