# -*- coding: utf-8 -*-
__filename = 'C:\\Users\\Alex\\Documents\\fernz\\src\\templates\\industry_primary.pynml'
__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: extra_text_primary.pynml', 26, 30), 988: ('load: extra_text_primary.pynml', 26, 30), 1054: ('load: produce_primary.pynml', 28, 30), 1054: ('load: produce_primary.pynml', 28, 30), 1117: ('load: check_primary_supplies_delivered.pynml', 30, 30), 1117: ('load: check_primary_supplies_delivered.pynml', 30, 30), 1197: ('load: availability.pynml', 32, 30), 1197: ('load: availability.pynml', 32, 30), 1273: ('load: location_check_macros_industry.pynml', 34, 46), 1347: ("location_checks_industry.macros['render_tree']", 35, 30), 1347: ("location_checks_industry.macros['render_tree']", 35, 30), 1429: ('load: properties_industry.pynml', 37, 30), 1429: ('load: properties_industry.pynml', 37, 30), 1613: ('economies', 40, 37), 1664: ("industry.get_property('enabled', economy) == True", 41, 39), 1724: ('if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    produce_256_ticks:        ${industry.id}_produce_256_ticks;\n                    monthly_prod_change:      ${industry.id}_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }', 42, 8), 1739: ('economy.numeric_id', 42, 23), 1798: ('industry.id', 43, 36), 1814: ('industry.numeric_id', 43, 52), 1913: ('industry.id', 45, 48), 2079: ('industry.id', 47, 48), 2149: ('industry.id', 48, 48), 2229: ('industry.id', 49, 48), 2389: ('industry.id', 51, 48), 2466: ('industry.get_extra_text_fund(economy)', 52, 48), 2554: ('industry.id', 53, 48), 2627: ('industry.id', 54, 48)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_2075101124704 = 'load: properties_industry.pynml'
_static_2075101125432 = "location_checks_industry.macros['render_tree']"
_static_2075101125712 = 'load: availability.pynml'
_static_2075101125936 = 'load: check_primary_supplies_delivered.pynml'
_static_2075101125208 = 'load: produce_primary.pynml'
_static_2075101126552 = 'load: extra_text_primary.pynml'
_static_2075099075528 = 'load: layouts.pynml'
_static_2075099075136 = 'load: properties_tile.pynml'
_static_2075099078608 = "animation_macros.macros['tile_animation']"
_static_2075099076648 = "location_checks_tile.macros['render_tree']"
_static_2075099076144 = 'load: graphics_switches.pynml'
_static_2075099078496 = 'load: spritelayouts.pynml'
_static_2075099075640 = 'load: spritesets.pynml'

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
            __backup_macroname_2075100620296 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3258B1438> name=None at 1e3258b1208> -> __value
            __value = _static_2075099075640
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100620296 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100620296
            __append('\n\n')
            __backup_macroname_2075100620936 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3258B1F60> name=None at 1e3258b14a8> -> __value
            __value = _static_2075099078496
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100620936 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100620936
            __append('\n\n')
            __backup_macroname_2075100619784 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3258B1630> name=None at 1e3258b1c88> -> __value
            __value = _static_2075099076144
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100619784 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100619784
            __append('\n\n')
            __backup_location_checks_tile_2075101627056 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_2075100621512 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3258B1828> name=None at 1e3258b1908> -> __value
            __value = _static_2075099076648
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100621512 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100621512
            if (__backup_location_checks_tile_2075101627056 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_2075101627056
            __append('\n\n')
            __backup_animation_macros_2075101627224 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_2075100622472 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3258B1FD0> name=None at 1e3258b17f0> -> __value
            __value = _static_2075099078608
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100622472 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100622472
            if (__backup_animation_macros_2075101627224 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_2075101627224
            __append('\n\n')
            __backup_macroname_2075100620488 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3258B1240> name=None at 1e3258b17b8> -> __value
            __value = _static_2075099075136
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100620488 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100620488
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')
            __backup_macroname_2075100619976 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3258B13C8> name=None at 1e3258b1f98> -> __value
            __value = _static_2075099075528
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100619976 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100619976
            __append('\n\n')
            __backup_macroname_2075100618952 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325AA5F98> name=None at 1e325aa5c88> -> __value
            __value = _static_2075101126552
            econtext['macroname'] = __value

            # <Value 'load: extra_text_primary.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' extra_text_primary.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100618952 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100618952
            __append('\n\n')
            __backup_macroname_2075099218696 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325AA5A58> name=None at 1e325aa57f0> -> __value
            __value = _static_2075101125208
            econtext['macroname'] = __value

            # <Value 'load: produce_primary.pynml' (28:30)> -> __macro
            __token = 1054
            __macro = ' produce_primary.pynml'
            __macro = __loader(__macro)
            __token = 1054
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075099218696 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075099218696
            __append('\n\n')
            __backup_macroname_2075099218568 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325AA5D30> name=None at 1e325aa5630> -> __value
            __value = _static_2075101125936
            econtext['macroname'] = __value

            # <Value 'load: check_primary_supplies_delivered.pynml' (30:30)> -> __macro
            __token = 1117
            __macro = ' check_primary_supplies_delivered.pynml'
            __macro = __loader(__macro)
            __token = 1117
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075099218568 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075099218568
            __append('\n\n')
            __backup_macroname_2075101990408 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325AA5C50> name=None at 1e325aa5d68> -> __value
            __value = _static_2075101125712
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (32:30)> -> __macro
            __token = 1197
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 1197
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075101990408 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075101990408
            __append('\n\n')
            __backup_location_checks_industry_2075101629968 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (34:46)> -> __value
            __token = 1273
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_2075099490312 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325AA5B38> name=None at 1e325aa5b00> -> __value
            __value = _static_2075101125432
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (35:30)> -> __macro
            __token = 1347
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1347
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075099490312 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075099490312
            if (__backup_location_checks_industry_2075101629968 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_2075101629968
            __append('\n\n')
            __backup_macroname_2075100054984 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325AA5860> name=None at 1e325aa5b70> -> __value
            __value = _static_2075101124704
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (37:30)> -> __macro
            __token = 1429
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1429
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075100054984 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075100054984
            __append('\n\n')
            __append('\n')
            __backup_economy_2075101630024 = get('economy', __marker)

            # <Value 'economies' (40:37)> -> __iterator
            __token = 1613
            __iterator = getitem('economies')
            (__iterator, ____index_2075101124984, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item
                __append('\n    ')

                # <Value "industry.get_property('enabled', economy) == True" (41:39)> -> __condition
                __token = 1664
                __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                if __condition:

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n                graphics {\n                    construction_probability: ${industry.id}_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ${industry.id}_produce;\n                    produce_256_ticks:        ${industry.id}_produce_256_ticks;\n                    monthly_prod_change:      ${industry.id}_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ${industry.id}_check_location;\n                    extra_text_fund:          ${industry.get_extra_text_fund(economy)};\n                    extra_text_industry:      ${industry.id}_extra_text;\n                    cargo_subtype_display:    ${industry.id}_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ' (41:90)> braces_required=True translation=False at 1e3258e70f0> -> __content_2075086945112
                    __token = 1724
                    __token = 1739
                    __content_2075086945112 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __token = 1798
                    __content_2075086945112_1796 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_1796 = __quote(__content_2075086945112_1796, '\x00', '&#0;', None, False)
                    __token = 1814
                    __content_2075086945112_1812 = _lookup_attr(getitem('industry'), 'numeric_id')
                    __content_2075086945112_1812 = __quote(__content_2075086945112_1812, '\x00', '&#0;', None, False)
                    __token = 1913
                    __content_2075086945112_1911 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_1911 = __quote(__content_2075086945112_1911, '\x00', '&#0;', None, False)
                    __token = 2079
                    __content_2075086945112_2077 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_2077 = __quote(__content_2075086945112_2077, '\x00', '&#0;', None, False)
                    __token = 2149
                    __content_2075086945112_2147 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_2147 = __quote(__content_2075086945112_2147, '\x00', '&#0;', None, False)
                    __token = 2229
                    __content_2075086945112_2227 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_2227 = __quote(__content_2075086945112_2227, '\x00', '&#0;', None, False)
                    __token = 2389
                    __content_2075086945112_2387 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_2387 = __quote(__content_2075086945112_2387, '\x00', '&#0;', None, False)
                    __token = 2466
                    __content_2075086945112_2464 = _lookup_attr(getitem('industry'), 'get_extra_text_fund')(getitem('economy'))
                    __content_2075086945112_2464 = __quote(__content_2075086945112_2464, '\x00', '&#0;', None, False)
                    __token = 2554
                    __content_2075086945112_2552 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_2552 = __quote(__content_2075086945112_2552, '\x00', '&#0;', None, False)
                    __token = 2627
                    __content_2075086945112_2625 = _lookup_attr(getitem('industry'), 'id')
                    __content_2075086945112_2625 = __quote(__content_2075086945112_2625, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n        if (economy==', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ') {\n            item(FEAT_INDUSTRIES, ', (__content_2075086945112_1796 if (__content_2075086945112_1796 is not None) else ''), ', ', (__content_2075086945112_1812 if (__content_2075086945112_1812 is not None) else ''), ') {\n                graphics {\n                    construction_probability: ', (__content_2075086945112_1911 if (__content_2075086945112_1911 is not None) else ''), '_check_availability;\n                    build_prod_change:        randomise_primary_production_on_build;\n                    produce_cargo_arrival:    ', (__content_2075086945112_2077 if (__content_2075086945112_2077 is not None) else ''), '_produce;\n                    produce_256_ticks:        ', (__content_2075086945112_2147 if (__content_2075086945112_2147 is not None) else ''), '_produce_256_ticks;\n                    monthly_prod_change:      ', (__content_2075086945112_2227 if (__content_2075086945112_2227 is not None) else ''), '_monthly_update;\n                    random_prod_change:       return CB_RESULT_IND_PROD_NO_CHANGE;\n                    location_check:           ', (__content_2075086945112_2387 if (__content_2075086945112_2387 is not None) else ''), '_check_location;\n                    extra_text_fund:          ', (__content_2075086945112_2464 if (__content_2075086945112_2464 is not None) else ''), ';\n                    extra_text_industry:      ', (__content_2075086945112_2552 if (__content_2075086945112_2552 is not None) else ''), '_extra_text;\n                    cargo_subtype_display:    ', (__content_2075086945112_2625 if (__content_2075086945112_2625 is not None) else ''), '_cargo_subtype_display;\n                    colour:                   switch_colour;\n                }\n            }\n        }\n    ', ))
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
                ____index_2075101124984 -= 1
                if (____index_2075101124984 > 0):
                    __append('')
            if (__backup_economy_2075101630024 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_2075101630024
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }