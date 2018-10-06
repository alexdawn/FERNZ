# -*- coding: utf-8 -*-
__filename = 'C:\\Users\\Alex\\Documents\\fernz\\src\\templates\\extra_text_secondary.pynml'
__tokens = {59: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_extra_text, economy) {', 3, 0), 92: ('industry.id', 3, 33), 163: ('economies', 4, 35), 218: ("industry.get_property('enabled', economy) == True", 5, 43), 282: ('${economy.numeric_id}: return ${industry.get_extra_text_string(economy)};', 6, 12), 284: ('economy.numeric_id', 6, 14), 314: ('industry.get_extra_text_string(economy)', 6, 44), 637: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display_cargo_1, [current_date - LOAD_PERM(${industry.perm_storage.date_received_1}) > 90]) {\n    0: return 0x3800 + string(STR_CARGO_SUBTYPE_DISPLAY_SECONDARY_CARGO_DELIVERED);\n    1: return 0x3800 + string(STR_EMPTY);\n}\n\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display_cargo_2, [current_date - LOAD_PERM(${industry.perm_storage.date_received_2}) > 90]) {\n    0: return 0x3800 + string(STR_CARGO_SUBTYPE_DISPLAY_SECONDARY_CARGO_DELIVERED);\n    1: return 0x3800 + string(STR_EMPTY);\n}\n\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display_cargo_3, [current_date - LOAD_PERM(${industry.perm_storage.date_received_3}) > 90]) {\n    0: return 0x3800 + string(STR_CARGO_SUBTYPE_DISPLAY_SECONDARY_CARGO_DELIVERED);\n    1: return 0x3800 + string(STR_EMPTY);\n}\n\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display_switch_cargo, getbits(extra_callback_info2, 0, 8)) {\n    0: ${industry.id}_cargo_subtype_display_cargo_1;\n    1: ${industry.id}_cargo_subtype_display_cargo_2;\n    2: ${industry.id}_cargo_subtype_display_cargo_3;\n    return CB_RESULT_NO_TEXT;\n}', 17, 0), 670: ('industry.id', 17, 33), 742: ('industry.perm_storage.date_received_1', 17, 105), 953: ('industry.id', 22, 33), 1025: ('industry.perm_storage.date_received_2', 22, 105), 1236: ('industry.id', 27, 33), 1308: ('industry.perm_storage.date_received_3', 27, 105), 1519: ('industry.id', 32, 33), 1616: ('industry.id', 33, 9), 1669: ('industry.id', 34, 9), 1722: ('industry.id', 35, 9), 1865: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display, getbits(extra_callback_info2, 8, 8)) {\n    1: ${industry.id}_cargo_subtype_display_switch_cargo;\n    return CB_RESULT_NO_TEXT;\n}', 39, 0), 1898: ('industry.id', 39, 33), 1982: ('industry.id', 40, 9)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

import re
import functools
from itertools import chain as __chain
__marker = object()
g_re_amp = re.compile('&(?!([A-Za-z]+|#[0-9]+);)')
g_re_needs_escape = re.compile('[&<>\\"\\\']').search
__re_whitespace = functools.partial(re.compile('\\s+').sub, ' ')

def initialize(__loader, macros, nothing, template):

    def render(__stream, econtext, rcontext, __i18n_domain=None, __i18n_context=None):
        __append = __stream.append
        __re_amp = g_re_amp
        __token = None
        __re_needs_escape = g_re_needs_escape

        def __convert(target):
            if (target is None):
                return
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except AttributeError:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            target = target()
            return target

        def __quote(target, quote, quote_entity, default, default_marker):
            if (target is None):
                return
            if (target is default_marker):
                return default
            __tt = type(target)
            if ((__tt is int) or (__tt is float) or (__tt is int)):
                target = str(target)
            else:
                if (__tt is bytes):
                    target = decode(target)
                else:
                    if (__tt is not str):
                        try:
                            target = target.__html__
                        except:
                            __converted = convert(target)
                            target = (str(target) if (target is __converted) else __converted)
                        else:
                            return target()
                if (target is not None):
                    try:
                        escape = (__re_needs_escape(target) is not None)
                    except TypeError:
                        pass
                    else:
                        if escape:
                            if ('&' in target):
                                target = target.replace('&', '&amp;')
                            if ('<' in target):
                                target = target.replace('<', '&lt;')
                            if ('>' in target):
                                target = target.replace('>', '&gt;')
                            if ((quote is not None) and (quote in target)):
                                target = target.replace(quote, quote_entity)
            return target
        translate = econtext['__translate']
        decode = econtext['__decode']
        convert = econtext['__convert']
        try:
            getitem = econtext.__getitem__
            get = econtext.get

            # <Interpolation value=<Substitution '\n\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_extra_text, economy) {\n    ' (1:57)> braces_required=True translation=False at 1e3258e70f0> -> __content_2075086945112
            __token = 59
            __token = 92
            __content_2075086945112 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s' % ('\n\nswitch (FEAT_INDUSTRIES, SELF, ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), '_extra_text, economy) {\n    ', ))
            if (__content_2075086945112 is None):
                pass
            else:
                if (__content_2075086945112 is False):
                    __content_2075086945112 = None
                else:
                    __tt = type(__content_2075086945112)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_2075086945112 = str(__content_2075086945112)
                    else:
                        if (__tt is bytes):
                            __content_2075086945112 = decode(__content_2075086945112)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_2075086945112 = __content_2075086945112.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_2075086945112)
                                    __content_2075086945112 = (str(__content_2075086945112) if (__content_2075086945112 is __converted) else __converted)
                                else:
                                    __content_2075086945112 = __content_2075086945112()
            if (__content_2075086945112 is not None):
                __append(__content_2075086945112)
            __backup_economy_2075100596376 = get('economy', __marker)

            # <Value 'economies' (4:35)> -> __iterator
            __token = 163
            __iterator = getitem('economies')
            (__iterator, ____index_2075099297608, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n        ')

                # <Value "industry.get_property('enabled', economy) == True" (5:43)> -> __condition
                __token = 218
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n            ${economy.numeric_id}: return ${industry.get_extra_text_string(economy)};\n        ' (5:94)> braces_required=True translation=False at 1e3258e7518> -> __content_2075086945112
                    __token = 282
                    __token = 284
                    __content_2075086945112 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __token = 314
                    __content_2075086945112_312 = _lookup_attr(getitem('industry'), 'get_extra_text_string')(getitem('economy'))
                    __content_2075086945112_312 = __quote(__content_2075086945112_312, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s%s%s' % ('\n            ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ': return ', (__content_2075086945112_312 if (__content_2075086945112_312 is not None) else ''), ';\n        ', ))
                    if (__content_2075086945112 is None):
                        pass
                    else:
                        if (__content_2075086945112 is False):
                            __content_2075086945112 = None
                        else:
                            __tt = type(__content_2075086945112)
                            if ((__tt is int) or (__tt is float) or (__tt is int)):
                                __content_2075086945112 = str(__content_2075086945112)
                            else:
                                if (__tt is bytes):
                                    __content_2075086945112 = decode(__content_2075086945112)
                                else:
                                    if (__tt is not str):
                                        try:
                                            __content_2075086945112 = __content_2075086945112.__html__
                                        except get('AttributeError', AttributeError):
                                            __converted = convert(__content_2075086945112)
                                            __content_2075086945112 = (str(__content_2075086945112) if (__content_2075086945112 is __converted) else __converted)
                                        else:
                                            __content_2075086945112 = __content_2075086945112()
                    if (__content_2075086945112 is not None):
                        __append(__content_2075086945112)
                __append('\n    ')
                ____index_2075099297608 -= 1
                if (____index_2075099297608 > 0):
                    __append('')
            if (__backup_economy_2075100596376 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_2075100596376
            __append('\n}\n\n\n')

            # <Interpolation value=<Substitution '\n\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display_cargo_1, [current_date - LOAD_PERM(${industry.perm_storage.date_received_1}) > 90]) {\n    0: return 0x3800 + string(STR_CARGO_SUBTYPE_DISPLAY_SECONDARY_CARGO_DELIVERED);\n    1: return 0x3800 + string(STR_EMPTY);\n}\n\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display_cargo_2, [current_date - LOAD_PERM(${industry.perm_storage.date_received_2}) > 90]) {\n    0: return 0x3800 + string(STR_CARGO_SUBTYPE_DISPLAY_SECONDARY_CARGO_DELIVERED);\n    1: return 0x3800 + string(STR_EMPTY);\n}\n\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display_cargo_3, [current_date - LOAD_PERM(${industry.perm_storage.date_received_3}) > 90]) {\n    0: return 0x3800 + string(STR_CARGO_SUBTYPE_DISPLAY_SECONDARY_CARGO_DELIVERED);\n    1: return 0x3800 + string(STR_EMPTY);\n}\n\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display_switch_cargo, getbits(extra_callback_info2, 0, 8)) {\n    0: ${industry.id}_cargo_subtype_display_cargo_1;\n    1: ${industry.id}_cargo_subtype_display_cargo_2;\n    2: ${industry.id}_cargo_subtype_display_cargo_3;\n    return CB_RESULT_NO_TEXT;\n}\n' (15:3)> braces_required=True translation=False at 1e3258e7780> -> __content_2075086945112
            __token = 637
            __token = 670
            __content_2075086945112 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __token = 742
            __content_2075086945112_740 = _lookup_attr(_lookup_attr(getitem('industry'), 'perm_storage'), 'date_received_1')
            __content_2075086945112_740 = __quote(__content_2075086945112_740, '\x00', '&#0;', None, False)
            __token = 953
            __content_2075086945112_951 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112_951 = __quote(__content_2075086945112_951, '\x00', '&#0;', None, False)
            __token = 1025
            __content_2075086945112_1023 = _lookup_attr(_lookup_attr(getitem('industry'), 'perm_storage'), 'date_received_2')
            __content_2075086945112_1023 = __quote(__content_2075086945112_1023, '\x00', '&#0;', None, False)
            __token = 1236
            __content_2075086945112_1234 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112_1234 = __quote(__content_2075086945112_1234, '\x00', '&#0;', None, False)
            __token = 1308
            __content_2075086945112_1306 = _lookup_attr(_lookup_attr(getitem('industry'), 'perm_storage'), 'date_received_3')
            __content_2075086945112_1306 = __quote(__content_2075086945112_1306, '\x00', '&#0;', None, False)
            __token = 1519
            __content_2075086945112_1517 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112_1517 = __quote(__content_2075086945112_1517, '\x00', '&#0;', None, False)
            __token = 1616
            __content_2075086945112_1614 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112_1614 = __quote(__content_2075086945112_1614, '\x00', '&#0;', None, False)
            __token = 1669
            __content_2075086945112_1667 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112_1667 = __quote(__content_2075086945112_1667, '\x00', '&#0;', None, False)
            __token = 1722
            __content_2075086945112_1720 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112_1720 = __quote(__content_2075086945112_1720, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n\nswitch (FEAT_INDUSTRIES, SELF, ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), '_cargo_subtype_display_cargo_1, [current_date - LOAD_PERM(', (__content_2075086945112_740 if (__content_2075086945112_740 is not None) else ''), ') > 90]) {\n    0: return 0x3800 + string(STR_CARGO_SUBTYPE_DISPLAY_SECONDARY_CARGO_DELIVERED);\n    1: return 0x3800 + string(STR_EMPTY);\n}\n\nswitch (FEAT_INDUSTRIES, SELF, ', (__content_2075086945112_951 if (__content_2075086945112_951 is not None) else ''), '_cargo_subtype_display_cargo_2, [current_date - LOAD_PERM(', (__content_2075086945112_1023 if (__content_2075086945112_1023 is not None) else ''), ') > 90]) {\n    0: return 0x3800 + string(STR_CARGO_SUBTYPE_DISPLAY_SECONDARY_CARGO_DELIVERED);\n    1: return 0x3800 + string(STR_EMPTY);\n}\n\nswitch (FEAT_INDUSTRIES, SELF, ', (__content_2075086945112_1234 if (__content_2075086945112_1234 is not None) else ''), '_cargo_subtype_display_cargo_3, [current_date - LOAD_PERM(', (__content_2075086945112_1306 if (__content_2075086945112_1306 is not None) else ''), ') > 90]) {\n    0: return 0x3800 + string(STR_CARGO_SUBTYPE_DISPLAY_SECONDARY_CARGO_DELIVERED);\n    1: return 0x3800 + string(STR_EMPTY);\n}\n\nswitch (FEAT_INDUSTRIES, SELF, ', (__content_2075086945112_1517 if (__content_2075086945112_1517 is not None) else ''), '_cargo_subtype_display_switch_cargo, getbits(extra_callback_info2, 0, 8)) {\n    0: ', (__content_2075086945112_1614 if (__content_2075086945112_1614 is not None) else ''), '_cargo_subtype_display_cargo_1;\n    1: ', (__content_2075086945112_1667 if (__content_2075086945112_1667 is not None) else ''), '_cargo_subtype_display_cargo_2;\n    2: ', (__content_2075086945112_1720 if (__content_2075086945112_1720 is not None) else ''), '_cargo_subtype_display_cargo_3;\n    return CB_RESULT_NO_TEXT;\n}\n', ))
            if (__content_2075086945112 is None):
                pass
            else:
                if (__content_2075086945112 is False):
                    __content_2075086945112 = None
                else:
                    __tt = type(__content_2075086945112)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_2075086945112 = str(__content_2075086945112)
                    else:
                        if (__tt is bytes):
                            __content_2075086945112 = decode(__content_2075086945112)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_2075086945112 = __content_2075086945112.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_2075086945112)
                                    __content_2075086945112 = (str(__content_2075086945112) if (__content_2075086945112 is __converted) else __converted)
                                else:
                                    __content_2075086945112 = __content_2075086945112()
            if (__content_2075086945112 is not None):
                __append(__content_2075086945112)

            # <Interpolation value=<Substitution '\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display, getbits(extra_callback_info2, 8, 8)) {\n    1: ${industry.id}_cargo_subtype_display_switch_cargo;\n    return CB_RESULT_NO_TEXT;\n}\n' (38:66)> braces_required=True translation=False at 1e3258e7d30> -> __content_2075086945112
            __token = 1865
            __token = 1898
            __content_2075086945112 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __token = 1982
            __content_2075086945112_1980 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112_1980 = __quote(__content_2075086945112_1980, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s%s%s' % ('\nswitch (FEAT_INDUSTRIES, SELF, ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), '_cargo_subtype_display, getbits(extra_callback_info2, 8, 8)) {\n    1: ', (__content_2075086945112_1980 if (__content_2075086945112_1980 is not None) else ''), '_cargo_subtype_display_switch_cargo;\n    return CB_RESULT_NO_TEXT;\n}\n', ))
            if (__content_2075086945112 is None):
                pass
            else:
                if (__content_2075086945112 is False):
                    __content_2075086945112 = None
                else:
                    __tt = type(__content_2075086945112)
                    if ((__tt is int) or (__tt is float) or (__tt is int)):
                        __content_2075086945112 = str(__content_2075086945112)
                    else:
                        if (__tt is bytes):
                            __content_2075086945112 = decode(__content_2075086945112)
                        else:
                            if (__tt is not str):
                                try:
                                    __content_2075086945112 = __content_2075086945112.__html__
                                except get('AttributeError', AttributeError):
                                    __converted = convert(__content_2075086945112)
                                    __content_2075086945112 = (str(__content_2075086945112) if (__content_2075086945112 is __converted) else __converted)
                                else:
                                    __content_2075086945112 = __content_2075086945112()
            if (__content_2075086945112 is not None):
                __append(__content_2075086945112)
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }