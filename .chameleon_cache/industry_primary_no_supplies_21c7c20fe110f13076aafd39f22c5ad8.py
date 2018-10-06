# -*- coding: utf-8 -*-
__filename = 'C:\\Users\\Alex\\Documents\\fernz\\src\\templates\\industry_primary_no_supplies.pynml'
__tokens = {242: ('load: spritesets.pynml', 5, 30), 242: ('load: spritesets.pynml', 5, 30), 300: ('load: spritelayouts.pynml', 7, 30), 300: ('load: spritelayouts.pynml', 7, 30), 361: ('load: graphics_switches.pynml', 9, 30), 361: ('load: graphics_switches.pynml', 9, 30), 438: ('load: location_check_macros_tile.pynml', 11, 42), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 508: ("location_checks_tile.macros['render_tree']", 12, 30), 594: ('load: animation_macros.pynml', 14, 38), 654: ("animation_macros.macros['tile_animation']", 15, 30), 654: ("animation_macros.macros['tile_animation']", 15, 30), 731: ('load: properties_tile.pynml', 17, 30), 731: ('load: properties_tile.pynml', 17, 30), 933: ('load: layouts.pynml', 24, 30), 933: ('load: layouts.pynml', 24, 30), 988: ('load: availability.pynml', 26, 30), 988: ('load: availability.pynml', 26, 30), 1064: ('load: location_check_macros_industry.pynml', 28, 46), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1138: ("location_checks_industry.macros['render_tree']", 29, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1220: ('load: properties_industry.pynml', 31, 30), 1406: ('item(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n\tgraphics {\n\t\tconstruction_probability:${industry.id}_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ${industry.id}_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}', 35, 0), 1430: ('industry.id', 35, 24), 1446: ('industry.numeric_id', 35, 40), 1511: ('industry.id', 37, 29), 1645: ('industry.id', 39, 29)}

from sys import exc_info as _exc_info
from chameleon.py26 import lookup_attr as _lookup_attr

_static_2075100148008 = 'load: properties_industry.pynml'
_static_2075100151704 = "location_checks_industry.macros['render_tree']"
_static_2075100148960 = 'load: availability.pynml'
_static_2075100151760 = 'load: layouts.pynml'
_static_2075100150752 = 'load: properties_tile.pynml'
_static_2075100149800 = "animation_macros.macros['tile_animation']"
_static_2075100566696 = "location_checks_tile.macros['render_tree']"
_static_2075100566416 = 'load: graphics_switches.pynml'
_static_2075100565632 = 'load: spritelayouts.pynml'
_static_2075100569272 = 'load: spritesets.pynml'

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
            __backup_macroname_2075102004872 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325A1DEB8> name=None at 1e325a1dc18> -> __value
            __value = _static_2075100569272
            econtext['macroname'] = __value

            # <Value 'load: spritesets.pynml' (5:30)> -> __macro
            __token = 242
            __macro = ' spritesets.pynml'
            __macro = __loader(__macro)
            __token = 242
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075102004872 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075102004872
            __append('\n\n')
            __backup_macroname_2075102075336 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325A1D080> name=None at 1e325a1dac8> -> __value
            __value = _static_2075100565632
            econtext['macroname'] = __value

            # <Value 'load: spritelayouts.pynml' (7:30)> -> __macro
            __token = 300
            __macro = ' spritelayouts.pynml'
            __macro = __loader(__macro)
            __token = 300
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075102075336 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075102075336
            __append('\n\n')
            __backup_macroname_2075102094664 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325A1D390> name=None at 1e325a1dc88> -> __value
            __value = _static_2075100566416
            econtext['macroname'] = __value

            # <Value 'load: graphics_switches.pynml' (9:30)> -> __macro
            __token = 361
            __macro = ' graphics_switches.pynml'
            __macro = __loader(__macro)
            __token = 361
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075102094664 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075102094664
            __append('\n\n')
            __backup_location_checks_tile_2075102081096 = get('location_checks_tile', __marker)

            # <Value 'load: location_check_macros_tile.pynml' (11:42)> -> __value
            __token = 438
            __value = ' location_check_macros_tile.pynml'
            __value = __loader(__value)
            econtext['location_checks_tile'] = __value
            __backup_macroname_2075102095496 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E325A1D4A8> name=None at 1e325a1db70> -> __value
            __value = _static_2075100566696
            econtext['macroname'] = __value

            # <Value "location_checks_tile.macros['render_tree']" (12:30)> -> __macro
            __token = 508
            __macro = _lookup_attr(getitem('location_checks_tile'), 'macros')['render_tree']
            __token = 508
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075102095496 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075102095496
            if (__backup_location_checks_tile_2075102081096 is __marker):
                del econtext['location_checks_tile']
            else:
                econtext['location_checks_tile'] = __backup_location_checks_tile_2075102081096
            __append('\n\n')
            __backup_animation_macros_2075102084008 = get('animation_macros', __marker)

            # <Value 'load: animation_macros.pynml' (14:38)> -> __value
            __token = 594
            __value = ' animation_macros.pynml'
            __value = __loader(__value)
            econtext['animation_macros'] = __value
            __backup_macroname_2075102003528 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259B7828> name=None at 1e3259b7908> -> __value
            __value = _static_2075100149800
            econtext['macroname'] = __value

            # <Value "animation_macros.macros['tile_animation']" (15:30)> -> __macro
            __token = 654
            __macro = _lookup_attr(getitem('animation_macros'), 'macros')['tile_animation']
            __token = 654
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075102003528 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075102003528
            if (__backup_animation_macros_2075102084008 is __marker):
                del econtext['animation_macros']
            else:
                econtext['animation_macros'] = __backup_animation_macros_2075102084008
            __append('\n\n')
            __backup_macroname_2075102097352 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259B7BE0> name=None at 1e3259b7ba8> -> __value
            __value = _static_2075100150752
            econtext['macroname'] = __value

            # <Value 'load: properties_tile.pynml' (17:30)> -> __macro
            __token = 731
            __macro = ' properties_tile.pynml'
            __macro = __loader(__macro)
            __token = 731
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075102097352 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075102097352
            __append('\n\n\n/* *************************************************\n * Definition of the industry\n * *************************************************/\n\n')
            __backup_macroname_2075101318728 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259B7FD0> name=None at 1e3259b76a0> -> __value
            __value = _static_2075100151760
            econtext['macroname'] = __value

            # <Value 'load: layouts.pynml' (24:30)> -> __macro
            __token = 933
            __macro = ' layouts.pynml'
            __macro = __loader(__macro)
            __token = 933
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075101318728 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075101318728
            __append('\n\n')
            __backup_macroname_2075102074568 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259B74E0> name=None at 1e3259b7518> -> __value
            __value = _static_2075100148960
            econtext['macroname'] = __value

            # <Value 'load: availability.pynml' (26:30)> -> __macro
            __token = 988
            __macro = ' availability.pynml'
            __macro = __loader(__macro)
            __token = 988
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075102074568 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075102074568
            __append('\n\n')
            __backup_location_checks_industry_2075102081880 = get('location_checks_industry', __marker)

            # <Value 'load: location_check_macros_industry.pynml' (28:46)> -> __value
            __token = 1064
            __value = ' location_check_macros_industry.pynml'
            __value = __loader(__value)
            econtext['location_checks_industry'] = __value
            __backup_macroname_2075101903560 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259B7F98> name=None at 1e3259b7b38> -> __value
            __value = _static_2075100151704
            econtext['macroname'] = __value

            # <Value "location_checks_industry.macros['render_tree']" (29:30)> -> __macro
            __token = 1138
            __macro = _lookup_attr(getitem('location_checks_industry'), 'macros')['render_tree']
            __token = 1138
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075101903560 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075101903560
            if (__backup_location_checks_industry_2075102081880 is __marker):
                del econtext['location_checks_industry']
            else:
                econtext['location_checks_industry'] = __backup_location_checks_industry_2075102081880
            __append('\n\n')
            __backup_macroname_2075099732104 = get('macroname', __marker)

            # <Static value=<_ast.Str object at 0x000001E3259B7128> name=None at 1e32594a978> -> __value
            __value = _static_2075100148008
            econtext['macroname'] = __value

            # <Value 'load: properties_industry.pynml' (31:30)> -> __macro
            __token = 1220
            __macro = ' properties_industry.pynml'
            __macro = __loader(__macro)
            __token = 1220
            __m = __macro.include
            __m(__stream, econtext.copy(), rcontext, __i18n_domain)
            econtext.update(rcontext)
            if (__backup_macroname_2075099732104 is __marker):
                del econtext['macroname']
            else:
                econtext['macroname'] = __backup_macroname_2075099732104
            __append('\n\n')
            __append('\n')

            # <Interpolation value=<Substitution '\nitem(FEAT_INDUSTRIES, ${industry.id}, ${industry.numeric_id}) {\n\tgraphics {\n\t\tconstruction_probability:${industry.id}_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ${industry.id}_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}\n' (34:38)> braces_required=True translation=False at 1e32594a550> -> __content_2075086945112
            __token = 1406
            __token = 1430
            __content_2075086945112 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __token = 1446
            __content_2075086945112_1444 = _lookup_attr(getitem('industry'), 'numeric_id')
            __content_2075086945112_1444 = __quote(__content_2075086945112_1444, '\x00', '&#0;', None, False)
            __token = 1511
            __content_2075086945112_1509 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112_1509 = __quote(__content_2075086945112_1509, '\x00', '&#0;', None, False)
            __token = 1645
            __content_2075086945112_1643 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112_1643 = __quote(__content_2075086945112_1643, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s%s%s%s%s%s%s' % ('\nitem(FEAT_INDUSTRIES, ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ', ', (__content_2075086945112_1444 if (__content_2075086945112_1444 is not None) else ''), ') {\n\tgraphics {\n\t\tconstruction_probability:', (__content_2075086945112_1509 if (__content_2075086945112_1509 is not None) else ''), '_check_availability;\n        build_prod_change:       randomise_primary_production_on_build;\n\t\tlocation_check:          ', (__content_2075086945112_1643 if (__content_2075086945112_1643 is not None) else ''), '_check_location;\n\t\tmonthly_prod_change:     return CB_RESULT_IND_PROD_NO_CHANGE;\n\t\trandom_prod_change:      return CB_RESULT_IND_PROD_NO_CHANGE;\n//\t\textra_text_industry:     // no extra text. No production increase by means of FMSP\n\t\tcolour:                  switch_colour;\n\t}\n}\n', ))
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