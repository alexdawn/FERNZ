# -*- coding: utf-8 -*-
__filename = 'C:\\Users\\Alex\\Documents\\fernz\\src\\templates\\industry_tertiary.pynml'
__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: availability.pynml', 26, 30), 988: ('load: availability.pynml', 26, 30), 1064: ('load: location_check_macros_industry.pynml', 28, 46), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1404: ('economies', 34, 37), 1455: ("industry.get_property('enabled', economy) == True", 35, 39), 1515: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    colour:                   switch_colour;\n                }\n            }\n        }', 36, 8), 1530: ('economy.numeric_id', 36, 23), 1589: ('industry.id', 37, 36), 1605: ('industry.numeric_id', 37, 52), 1704: ('industry.id', 39, 48), 1870: ('industry.id', 41, 48), 1947: ('industry.get_extra_text_fund(economy)', 42, 48)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_2075100224536 = 'load: properties_industry.pynml'
_static_2075100222968 = "location_checks_industry.macros['render_tree']"
_static_2075100224368 = 'load: availability.pynml'
_static_2075100221624 = 'load: layouts.pynml'
_static_2075100225432 = 'load: properties_tile.pynml'
_static_2075099319824 = "animation_macros.macros['tile_animation']"
_static_2075101125600 = "location_checks_tile.macros['render_tree']"
_static_2075101122744 = 'load: graphics_switches.pynml'
_static_2075101125488 = 'load: spritelayouts.pynml'
_static_2075101124200 = 'load: spritesets.pynml'

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
            __append('/* ******************************************************************\n * Definition of the industry tile, its callbacks, and graphics chain\n * ******************************************************************/\n\n')
            __backup_macroname_2075101316552 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325AA5668> name=None at 1e325aa5b00> -> __value
            __value = _static_2075101124200
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075101316552 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075101316552
            __append('\n\n')
            __backup_macroname_2075101936904 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325AA5B70> name=None at 1e325aa59e8> -> __value
            __value = _static_2075101125488
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075101936904 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075101936904
            __append('\n\n')
            __backup_macroname_2075101318728 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325AA50B8> name=None at 1e325aa5780> -> __value
            __value = _static_2075101122744
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075101318728 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075101318728
            __append('\n\n')
            __backup_location_checks_tile_2075099684760 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_2075100621000 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325AA5BE0> name=None at 1e325aa57f0> -> __value
            __value = _static_2075101125600
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100621000 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100621000
            if (__backup_location_checks_tile_2075099684760 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_2075099684760
            __append('\n\n')
            __backup_animation_macros_2075101630080 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_2075100679624 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3258ECE10> name=None at 1e325aa54e0> -> __value
            __value = _static_2075099319824
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100679624 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100679624
            if (__backup_animation_macros_2075101630080 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_2075101630080
            __append('\n\n')
            __backup_macroname_2075100621512 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259C9F98> name=None at 1e3259c9b00> -> __value
            __value = _static_2075100225432
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100621512 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100621512
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')
            __backup_macroname_2075100619912 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259C90B8> name=None at 1e3259c97b8> -> __value
            __value = _static_2075100221624
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100619912 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100619912
            __append('\n\n')
            __backup_macroname_2075102014280 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259C9B70> name=None at 1e3259c9e10> -> __value
            __value = _static_2075100224368
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075102014280 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075102014280
            __append('\n\n')
            __backup_location_checks_industry_2075101639400 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (28:46)> -> __value
            __token = 1064
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_2075102095944 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259C95F8> name=None at 1e3259c9208> -> __value
            __value = _static_2075100222968
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (29:30)> -> __macro
            __token = 1138
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1138
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075102095944 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075102095944
            if (__backup_location_checks_industry_2075101639400 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_2075101639400
            __append('\n\n')
            __backup_macroname_2075101316616 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259C9C18> name=None at 1e3259c9630> -> __value
            __value = _static_2075100224536
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (31:30)> -> __macro
            __token = 1220
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1220
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075101316616 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075101316616
            __append('\n\n')
            __append('\n')
            __backup_economy_2075100148512 = get('economy', __marker)

            # <Value 'economies' (34:37)> -> __iterator
            __token = 1404
            __iterator = getitem('economies')
            (__iterator, ____index_2075099822960, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Value "industry.get_property('enabled', economy) == True" (35:39)> -> __condition
                __token = 1455
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ' (35:90)> braces_required=True translation=False at 1e325967e80> -> __content_2075086945112
                    __token = 1515
                    __token = 1530
                    __content_2075086945112 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __token = 1589
                    __content_2075086945112_1587 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_1587 = __quote(__content_2075086945112_1587, '\x00', '&#0;', None, False)
                    __token = 1605
                    __content_2075086945112_1603 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_2075086945112_1603 = __quote(__content_2075086945112_1603, '\x00', '&#0;', None, False)
                    __token = 1704
                    __content_2075086945112_1702 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_1702 = __quote(__content_2075086945112_1702, '\x00', '&#0;', None, False)
                    __token = 1870
                    __content_2075086945112_1868 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_1868 = __quote(__content_2075086945112_1868, '\x00', '&#0;', None, False)
                    __token = 1947
                    __content_2075086945112_1945 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_2075086945112_1945 = __quote(__content_2075086945112_1945, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_2075086945112_1587 if (__content_2075086945112_1587 is not None) else ''), ', ', (__content_2075086945112_1603 if (__content_2075086945112_1603 is not None) else ''), ') {\n                graphics {\n                    construction_probability: ', (__content_2075086945112_1702 if (__content_2075086945112_1702 is not None) else ''), '_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    location_check:           ', (__content_2075086945112_1868 if (__content_2075086945112_1868 is not None) else ''), '_check_location;\n                    extra_text_fund:          ', (__content_2075086945112_1945 if (__content_2075086945112_1945 is not None) else ''), ';\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ', ))
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
                __append('\n')
                ____index_2075099822960 -= 1
                if (____index_2075099822960 > 0):
                    __append('')
            if (__backup_economy_2075100148512 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_2075100148512
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }