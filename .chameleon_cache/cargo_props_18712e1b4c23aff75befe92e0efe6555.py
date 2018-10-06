# -*- coding: utf-8 -*-
__filename = 'C:\\Users\\Alex\\Documents\\fernz\\src\\templates\\cargo_props.pynml'
__tokens = {54: ('item(FEAT_CARGOS, ${cargo.id}_${economy.id}, ${cargo.get_numeric_id(economy)}) {\n    property {', 2, 0), 74: ('cargo.id', 2, 20), 86: ('economy.id', 2, 32), 101: ('cargo.get_numeric_id(economy)', 2, 47), 191: ("${cargo.get_property_declaration('type_name')}\n        ${cargo.get_property_declaration('unit_name')}\n        ${cargo.get_property_declaration('type_abbreviation')}\n        ${cargo.get_property_declaration('sprite')}\n        ${cargo.get_property_declaration('weight')}\n        ${cargo.get_property_declaration('station_list_colour')}\n        ${cargo.get_property_declaration('cargo_payment_list_colour')}\n        ${cargo.get_property_declaration('is_freight')}\n        ${cargo.get_property_declaration('cargo_classes')}\n        ${cargo.get_property_declaration('town_growth_effect', economy)}\n        ${cargo.get_property_declaration('town_growth_multiplier', economy)}\n        ${cargo.get_property_declaration('units_of_cargo')}\n        ${cargo.get_property_declaration('items_of_cargo')}\n        ${cargo.get_property_declaration('penalty_lowerbound', economy)}\n        ${cargo.get_property_declaration('single_penalty_length', economy)}\n        ${cargo.get_property_declaration('price_factor', economy)}\n        ${cargo.get_property_declaration('capacity_multiplier')}", 5, 8), 193: ("cargo.get_property_declaration('type_name')", 5, 10), 248: ("cargo.get_property_declaration('unit_name')", 6, 10), 303: ("cargo.get_property_declaration('type_abbreviation')", 7, 10), 366: ("cargo.get_property_declaration('sprite')", 8, 10), 418: ("cargo.get_property_declaration('weight')", 9, 10), 470: ("cargo.get_property_declaration('station_list_colour')", 10, 10), 535: ("cargo.get_property_declaration('cargo_payment_list_colour')", 11, 10), 606: ("cargo.get_property_declaration('is_freight')", 12, 10), 662: ("cargo.get_property_declaration('cargo_classes')", 13, 10), 721: ("cargo.get_property_declaration('town_growth_effect', economy)", 14, 10), 794: ("cargo.get_property_declaration('town_growth_multiplier', economy)", 15, 10), 871: ("cargo.get_property_declaration('units_of_cargo')", 16, 10), 931: ("cargo.get_property_declaration('items_of_cargo')", 17, 10), 991: ("cargo.get_property_declaration('penalty_lowerbound', economy)", 18, 10), 1064: ("cargo.get_property_declaration('single_penalty_length', economy)", 19, 10), 1140: ("cargo.get_property_declaration('price_factor', economy)", 20, 10), 1207: ("cargo.get_property_declaration('capacity_multiplier')", 21, 10), 1338: ('cargo_label: ${cargo.get_cargo_label()};\n        number: ${cargo.get_numeric_id(economy)};\n    }\n    graphics {\n        cargoicon_${cargo.id};\n    }\n}', 23, 8), 1353: ('cargo.get_cargo_label()', 23, 23), 1397: ('cargo.get_numeric_id(economy)', 24, 18), 1470: ('cargo.id', 27, 20)}

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

            # <Interpolation value=<Substitution '\nitem(FEAT_CARGOS, ${cargo.id}_${economy.id}, ${cargo.get_numeric_id(economy)}) {\n    property {\n        ' (1:53)> braces_required=True translation=False at 1e3258b89b0> -> __content_2075086945112
            __token = 54
            __token = 74
            __content_2075086945112 = _lookup_attr(getitem('cargo'), 'id')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __token = 86
            __content_2075086945112_84 = _lookup_attr(getitem('economy'), 'id')
            __content_2075086945112_84 = __quote(__content_2075086945112_84, '\x00', '&#0;', None, False)
            __token = 101
            __content_2075086945112_99 = _lookup_attr(getitem('cargo'), 'get_numeric_id')(getitem('economy'))
            __content_2075086945112_99 = __quote(__content_2075086945112_99, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s%s%s%s%s' % ('\nitem(FEAT_CARGOS, ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), '_', (__content_2075086945112_84 if (__content_2075086945112_84 is not None) else ''), ', ', (__content_2075086945112_99 if (__content_2075086945112_99 is not None) else ''), ') {\n    property {\n        ', ))
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

            # <Interpolation value=<Substitution "\n        ${cargo.get_property_declaration('type_name')}\n        ${cargo.get_property_declaration('unit_name')}\n        ${cargo.get_property_declaration('type_abbreviation')}\n        ${cargo.get_property_declaration('sprite')}\n        ${cargo.get_property_declaration('weight')}\n        ${cargo.get_property_declaration('station_list_colour')}\n        ${cargo.get_property_declaration('cargo_payment_list_colour')}\n        ${cargo.get_property_declaration('is_freight')}\n        ${cargo.get_property_declaration('cargo_classes')}\n        ${cargo.get_property_declaration('town_growth_effect', economy)}\n        ${cargo.get_property_declaration('town_growth_multiplier', economy)}\n        ${cargo.get_property_declaration('units_of_cargo')}\n        ${cargo.get_property_declaration('items_of_cargo')}\n        ${cargo.get_property_declaration('penalty_lowerbound', economy)}\n        ${cargo.get_property_declaration('single_penalty_length', economy)}\n        ${cargo.get_property_declaration('price_factor', economy)}\n        ${cargo.get_property_declaration('capacity_multiplier')}\n        " (4:32)> braces_required=True translation=False at 1e3258b8da0> -> __content_2075086945112
            __token = 191
            __token = 193
            __content_2075086945112 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('type_name')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __token = 248
            __content_2075086945112_246 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('unit_name')
            __content_2075086945112_246 = __quote(__content_2075086945112_246, '\x00', '&#0;', None, False)
            __token = 303
            __content_2075086945112_301 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('type_abbreviation')
            __content_2075086945112_301 = __quote(__content_2075086945112_301, '\x00', '&#0;', None, False)
            __token = 366
            __content_2075086945112_364 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('sprite')
            __content_2075086945112_364 = __quote(__content_2075086945112_364, '\x00', '&#0;', None, False)
            __token = 418
            __content_2075086945112_416 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('weight')
            __content_2075086945112_416 = __quote(__content_2075086945112_416, '\x00', '&#0;', None, False)
            __token = 470
            __content_2075086945112_468 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('station_list_colour')
            __content_2075086945112_468 = __quote(__content_2075086945112_468, '\x00', '&#0;', None, False)
            __token = 535
            __content_2075086945112_533 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('cargo_payment_list_colour')
            __content_2075086945112_533 = __quote(__content_2075086945112_533, '\x00', '&#0;', None, False)
            __token = 606
            __content_2075086945112_604 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('is_freight')
            __content_2075086945112_604 = __quote(__content_2075086945112_604, '\x00', '&#0;', None, False)
            __token = 662
            __content_2075086945112_660 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('cargo_classes')
            __content_2075086945112_660 = __quote(__content_2075086945112_660, '\x00', '&#0;', None, False)
            __token = 721
            __content_2075086945112_719 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('town_growth_effect', getitem('economy'))
            __content_2075086945112_719 = __quote(__content_2075086945112_719, '\x00', '&#0;', None, False)
            __token = 794
            __content_2075086945112_792 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('town_growth_multiplier', getitem('economy'))
            __content_2075086945112_792 = __quote(__content_2075086945112_792, '\x00', '&#0;', None, False)
            __token = 871
            __content_2075086945112_869 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('units_of_cargo')
            __content_2075086945112_869 = __quote(__content_2075086945112_869, '\x00', '&#0;', None, False)
            __token = 931
            __content_2075086945112_929 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('items_of_cargo')
            __content_2075086945112_929 = __quote(__content_2075086945112_929, '\x00', '&#0;', None, False)
            __token = 991
            __content_2075086945112_989 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('penalty_lowerbound', getitem('economy'))
            __content_2075086945112_989 = __quote(__content_2075086945112_989, '\x00', '&#0;', None, False)
            __token = 1064
            __content_2075086945112_1062 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('single_penalty_length', getitem('economy'))
            __content_2075086945112_1062 = __quote(__content_2075086945112_1062, '\x00', '&#0;', None, False)
            __token = 1140
            __content_2075086945112_1138 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('price_factor', getitem('economy'))
            __content_2075086945112_1138 = __quote(__content_2075086945112_1138, '\x00', '&#0;', None, False)
            __token = 1207
            __content_2075086945112_1205 = _lookup_attr(getitem('cargo'), 'get_property_declaration')('capacity_multiplier')
            __content_2075086945112_1205 = __quote(__content_2075086945112_1205, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), '\n        ', (__content_2075086945112_246 if (__content_2075086945112_246 is not None) else ''), '\n        ', (__content_2075086945112_301 if (__content_2075086945112_301 is not None) else ''), '\n        ', (__content_2075086945112_364 if (__content_2075086945112_364 is not None) else ''), '\n        ', (__content_2075086945112_416 if (__content_2075086945112_416 is not None) else ''), '\n        ', (__content_2075086945112_468 if (__content_2075086945112_468 is not None) else ''), '\n        ', (__content_2075086945112_533 if (__content_2075086945112_533 is not None) else ''), '\n        ', (__content_2075086945112_604 if (__content_2075086945112_604 is not None) else ''), '\n        ', (__content_2075086945112_660 if (__content_2075086945112_660 is not None) else ''), '\n        ', (__content_2075086945112_719 if (__content_2075086945112_719 is not None) else ''), '\n        ', (__content_2075086945112_792 if (__content_2075086945112_792 is not None) else ''), '\n        ', (__content_2075086945112_869 if (__content_2075086945112_869 is not None) else ''), '\n        ', (__content_2075086945112_929 if (__content_2075086945112_929 is not None) else ''), '\n        ', (__content_2075086945112_989 if (__content_2075086945112_989 is not None) else ''), '\n        ', (__content_2075086945112_1062 if (__content_2075086945112_1062 is not None) else ''), '\n        ', (__content_2075086945112_1138 if (__content_2075086945112_1138 is not None) else ''), '\n        ', (__content_2075086945112_1205 if (__content_2075086945112_1205 is not None) else ''), '\n        ', ))
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

            # <Interpolation value=<Substitution '\n        cargo_label: ${cargo.get_cargo_label()};\n        number: ${cargo.get_numeric_id(economy)};\n    }\n    graphics {\n        cargoicon_${cargo.id};\n    }\n}\n' (22:67)> braces_required=True translation=False at 1e3258b80f0> -> __content_2075086945112
            __token = 1338
            __token = 1353
            __content_2075086945112 = _lookup_attr(getitem('cargo'), 'get_cargo_label')()
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __token = 1397
            __content_2075086945112_1395 = _lookup_attr(getitem('cargo'), 'get_numeric_id')(getitem('economy'))
            __content_2075086945112_1395 = __quote(__content_2075086945112_1395, '\x00', '&#0;', None, False)
            __token = 1470
            __content_2075086945112_1468 = _lookup_attr(getitem('cargo'), 'id')
            __content_2075086945112_1468 = __quote(__content_2075086945112_1468, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s%s%s%s%s' % ('\n        cargo_label: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n        number: ', (__content_2075086945112_1395 if (__content_2075086945112_1395 is not None) else ''), ';\n    }\n    graphics {\n        cargoicon_', (__content_2075086945112_1468 if (__content_2075086945112_1468 is not None) else ''), ';\n    }\n}\n', ))
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