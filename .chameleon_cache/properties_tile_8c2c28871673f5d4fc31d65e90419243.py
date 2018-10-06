# -*- coding: utf-8 -*-
__filename = 'C:\\Users\\Alex\\Documents\\fernz\\src\\templates\\properties_tile.pynml'
__tokens = {24: ('industry.tiles', 1, 24), 107: ('item(FEAT_INDUSTRYTILES, ${tile.id}, ${tile.numeric_id}) {\n        property {\n            substitute:         0;\n            land_shape_flags:   ${tile.land_shape_flags};', 3, 4), 134: ('tile.id', 3, 31), 146: ('tile.numeric_id', 3, 43), 254: ('tile.land_shape_flags', 6, 34), 320: ('tile.special_flags is not None', 7, 42), 369: ('special_flags: ${tile.special_flags};', 8, 16), 386: ('tile.special_flags', 8, 33), 580: ('tile.animation_length > 1', 11, 43), 624: ("animation_info: [${'ANIMATION_LOOPING' if tile.animation_looping else 'ANIMATION_NON_LOOPING'}, ${tile.animation_length}];", 12, 16), 643: ("'ANIMATION_LOOPING' if tile.animation_looping else 'ANIMATION_NON_LOOPING'", 12, 35), 722: ('tile.animation_length', 12, 114), 825: ('tile.animation_speed > 0', 14, 44), 868: ('animation_speed: ${tile.animation_speed};', 15, 16), 887: ('tile.animation_speed', 15, 35), 957: ('animation_triggers: ${tile.get_animation_triggers()};\n        }\n\n        graphics {', 17, 12), 979: ('tile.get_animation_triggers()', 17, 34), 1083: ('len(tile.location_checks.get_render_tree(tile.id, industry.id)) > 0', 21, 42), 1163: ('tile_check: ${tile.location_checks.get_render_tree(tile.id, industry.id)[-1].switch_entry_point};', 22, 10), 1177: ('tile.location_checks.get_render_tree(tile.id, industry.id)[-1].switch_entry_point', 22, 24), 1344: ('tile.custom_animation_next_frame', 24, 44), 1395: ('anim_next_frame: return ${tile.custom_animation_next_frame};', 25, 16), 1421: ('tile.custom_animation_next_frame', 25, 42), 1526: ('tile.custom_animation_control is not None', 27, 35), 1580: ('anim_control: ${tile.id}_anim_control;', 28, 10), 1596: ('tile.id', 28, 26), 1688: ('tile.random_trigger is not None', 30, 43), 1738: ('random_trigger: ${tile.random_trigger};', 31, 16), 1756: ('tile.random_trigger', 31, 34), 1846: ('tile.foundations is not None', 33, 34), 1893: ('foundations: ${tile.foundations};', 34, 16), 1908: ('tile.foundations', 34, 31), 1990: ('tile.autoslope is not None', 36, 32), 2035: ('autoslope: ${tile.autoslope};', 37, 16), 2048: ('tile.autoslope', 37, 29), 2106: ('${industry.id}_tile_fences;\n        }\n    }', 39, 12), 2108: ('industry.id', 39, 14), 2251: ('economies', 45, 35), 2271: ('if (economy==${economy.numeric_id}) {', 46, 8), 2286: ('economy.numeric_id', 46, 23), 2356: ("industry.get_property('enabled', economy) == True", 47, 47), 2424: ('item(FEAT_INDUSTRYTILES, ${tile.id}, ${tile.numeric_id}) {\n                    property {\n                        accepted_cargos:  [${tile.get_expression_for_tile_acceptance(industry, economy)}];\n                    }\n                }', 48, 16), 2451: ('tile.id', 48, 43), 2463: ('tile.numeric_id', 48, 55), 2559: ('tile.get_expression_for_tile_acceptance(industry, economy)', 50, 45)}

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
            __backup_tile_2075100595928 = get('tile', __marker)

            # <Value 'industry.tiles' (1:24)> -> __iterator
            __token = 24
            __iterator = _lookup_attr(getitem('industry'), 'tiles')
            (__iterator, ____index_2075101627392, ) = getitem('repeat')('tile', __iterator)
            econtext['tile'] = None
            for __item in __iterator:
                econtext['tile'] = __item
                __append('\n    ')

                # <Interpolation value=<Substitution '\n    item(FEAT_INDUSTRYTILES, ${tile.id}, ${tile.numeric_id}) {\n        property {\n            substitute:         0;\n            land_shape_flags:   ${tile.land_shape_flags};\n            ' (2:61)> braces_required=True translation=False at 1e325b20fd0> -> __content_2075086945112
                __token = 107
                __token = 134
                __content_2075086945112 = _lookup_attr(getitem('tile'), 'id')
                __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                __token = 146
                __content_2075086945112_144 = _lookup_attr(getitem('tile'), 'numeric_id')
                __content_2075086945112_144 = __quote(__content_2075086945112_144, '\x00', '&#0;', None, False)
                __token = 254
                __content_2075086945112_252 = _lookup_attr(getitem('tile'), 'land_shape_flags')
                __content_2075086945112_252 = __quote(__content_2075086945112_252, '\x00', '&#0;', None, False)
                __content_2075086945112 = ('%s%s%s%s%s%s%s' % ('\n    item(FEAT_INDUSTRYTILES, ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ', ', (__content_2075086945112_144 if (__content_2075086945112_144 is not None) else ''), ') {\n        property {\n            substitute:         0;\n            land_shape_flags:   ', (__content_2075086945112_252 if (__content_2075086945112_252 is not None) else ''), ';\n            ', ))
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

                # <Value 'tile.special_flags is not None' (7:42)> -> __condition
                __token = 320
                __condition = (_lookup_attr(getitem('tile'), 'special_flags') is not None)
                if __condition:

                    # <Interpolation value=<Substitution '\n                special_flags: ${tile.special_flags};\n            ' (7:74)> braces_required=True translation=False at 1e325b20c50> -> __content_2075086945112
                    __token = 369
                    __token = 386
                    __content_2075086945112 = _lookup_attr(getitem('tile'), 'special_flags')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s' % ('\n                special_flags: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n            ', ))
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
                __append('\n            ')
                __append('\n            ')

                # <Value 'tile.animation_length > 1' (11:43)> -> __condition
                __token = 580
                __condition = (_lookup_attr(getitem('tile'), 'animation_length') > 1)
                if __condition:

                    # <Interpolation value=<Substitution "\n                animation_info: [${'ANIMATION_LOOPING' if tile.animation_looping else 'ANIMATION_NON_LOOPING'}, ${tile.animation_length}];\n            " (11:70)> braces_required=True translation=False at 1e325b20198> -> __content_2075086945112
                    __token = 624
                    __token = 643
                    __content_2075086945112 = ('ANIMATION_LOOPING' if _lookup_attr(getitem('tile'), 'animation_looping') else 'ANIMATION_NON_LOOPING')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __token = 722
                    __content_2075086945112_720 = _lookup_attr(getitem('tile'), 'animation_length')
                    __content_2075086945112_720 = __quote(__content_2075086945112_720, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s%s%s' % ('\n                animation_info: [', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ', ', (__content_2075086945112_720 if (__content_2075086945112_720 is not None) else ''), '];\n            ', ))
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
                __append('\n            ')

                # <Value 'tile.animation_speed > 0' (14:44)> -> __condition
                __token = 825
                __condition = (_lookup_attr(getitem('tile'), 'animation_speed') > 0)
                if __condition:

                    # <Interpolation value=<Substitution '\n                animation_speed: ${tile.animation_speed};\n            ' (14:70)> braces_required=True translation=False at 1e324a3b780> -> __content_2075086945112
                    __token = 868
                    __token = 887
                    __content_2075086945112 = _lookup_attr(getitem('tile'), 'animation_speed')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s' % ('\n                animation_speed: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n            ', ))
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

                # <Interpolation value=<Substitution '\n            animation_triggers: ${tile.get_animation_triggers()};\n        }\n\n        graphics {\n    \t\t' (16:34)> braces_required=True translation=False at 1e325b20358> -> __content_2075086945112
                __token = 957
                __token = 979
                __content_2075086945112 = _lookup_attr(getitem('tile'), 'get_animation_triggers')()
                __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                __content_2075086945112 = ('%s%s%s' % ('\n            animation_triggers: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n        }\n\n        graphics {\n    \t\t', ))
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

                # <Value 'len(tile.location_checks.get_render_tree(tile.id, industry.id)) > 0' (21:42)> -> __condition
                __token = 1083
                __condition = (len(_lookup_attr(_lookup_attr(getitem('tile'), 'location_checks'), 'get_render_tree')(_lookup_attr(getitem('tile'), 'id'), _lookup_attr(getitem('industry'), 'id'))) > 0)
                if __condition:

                    # <Interpolation value=<Substitution '\n    \t\t    tile_check: ${tile.location_checks.get_render_tree(tile.id, industry.id)[-1].switch_entry_point};\n            ' (21:111)> braces_required=True translation=False at 1e324a3b518> -> __content_2075086945112
                    __token = 1163
                    __token = 1177
                    __content_2075086945112 = _lookup_attr(_lookup_attr(_lookup_attr(getitem('tile'), 'location_checks'), 'get_render_tree')(_lookup_attr(getitem('tile'), 'id'), _lookup_attr(getitem('industry'), 'id'))[- 1], 'switch_entry_point')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s' % ('\n    \t\t    tile_check: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n            ', ))
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
                __append('\n            ')

                # <Value 'tile.custom_animation_next_frame' (24:44)> -> __condition
                __token = 1344
                __condition = _lookup_attr(getitem('tile'), 'custom_animation_next_frame')
                if __condition:

                    # <Interpolation value=<Substitution '\n                anim_next_frame: return ${tile.custom_animation_next_frame};\n            ' (24:78)> braces_required=True translation=False at 1e324a3bc88> -> __content_2075086945112
                    __token = 1395
                    __token = 1421
                    __content_2075086945112 = _lookup_attr(getitem('tile'), 'custom_animation_next_frame')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s' % ('\n                anim_next_frame: return ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n            ', ))
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
                __append('\n    \t\t')

                # <Value 'tile.custom_animation_control is not None' (27:35)> -> __condition
                __token = 1526
                __condition = (_lookup_attr(getitem('tile'), 'custom_animation_control') is not None)
                if __condition:

                    # <Interpolation value=<Substitution '\n    \t\t    anim_control: ${tile.id}_anim_control;\n    \t\t' (27:78)> braces_required=True translation=False at 1e324a3b6d8> -> __content_2075086945112
                    __token = 1580
                    __token = 1596
                    __content_2075086945112 = _lookup_attr(getitem('tile'), 'id')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s' % ('\n    \t\t    anim_control: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), '_anim_control;\n    \t\t', ))
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
                __append('\n            ')

                # <Value 'tile.random_trigger is not None' (30:43)> -> __condition
                __token = 1688
                __condition = (_lookup_attr(getitem('tile'), 'random_trigger') is not None)
                if __condition:

                    # <Interpolation value=<Substitution '\n                random_trigger: ${tile.random_trigger};\n            ' (30:76)> braces_required=True translation=False at 1e325b1b6a0> -> __content_2075086945112
                    __token = 1738
                    __token = 1756
                    __content_2075086945112 = _lookup_attr(getitem('tile'), 'random_trigger')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s' % ('\n                random_trigger: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n            ', ))
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
                __append('\n    \t\t')

                # <Value 'tile.foundations is not None' (33:34)> -> __condition
                __token = 1846
                __condition = (_lookup_attr(getitem('tile'), 'foundations') is not None)
                if __condition:

                    # <Interpolation value=<Substitution '\n                foundations: ${tile.foundations};\n            ' (33:64)> braces_required=True translation=False at 1e325b1b470> -> __content_2075086945112
                    __token = 1893
                    __token = 1908
                    __content_2075086945112 = _lookup_attr(getitem('tile'), 'foundations')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s' % ('\n                foundations: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n            ', ))
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
                __append('\n    \t\t')

                # <Value 'tile.autoslope is not None' (36:32)> -> __condition
                __token = 1990
                __condition = (_lookup_attr(getitem('tile'), 'autoslope') is not None)
                if __condition:

                    # <Interpolation value=<Substitution '\n                autoslope: ${tile.autoslope};\n            ' (36:60)> braces_required=True translation=False at 1e325b1b668> -> __content_2075086945112
                    __token = 2035
                    __token = 2048
                    __content_2075086945112 = _lookup_attr(getitem('tile'), 'autoslope')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s' % ('\n                autoslope: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n            ', ))
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

                # <Interpolation value=<Substitution '\n            ${industry.id}_tile_fences;\n        }\n    }\n    ' (38:28)> braces_required=True translation=False at 1e325b1b518> -> __content_2075086945112
                __token = 2106
                __token = 2108
                __content_2075086945112 = _lookup_attr(getitem('industry'), 'id')
                __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                __content_2075086945112 = ('%s%s%s' % ('\n            ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), '_tile_fences;\n        }\n    }\n    ', ))
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
                __backup_economy_2075083927448 = get('economy', __marker)

                # <Value 'economies' (45:35)> -> __iterator
                __token = 2251
                __iterator = getitem('economies')
                (__iterator, ____index_2075101607696, ) = getitem('repeat')('economy', __iterator)
                econtext['economy'] = None
                for __item in __iterator:
                    econtext['economy'] = __item

                    # <Interpolation value=<Substitution '\n        if (economy==${economy.numeric_id}) {\n            ' (45:46)> braces_required=True translation=False at 1e325b1b160> -> __content_2075086945112
                    __token = 2271
                    __token = 2286
                    __content_2075086945112 = _lookup_attr(getitem('economy'), 'numeric_id')
                    __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                    __content_2075086945112 = ('%s%s%s' % ('\n        if (economy==', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ') {\n            ', ))
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

                    # <Value "industry.get_property('enabled', economy) == True" (47:47)> -> __condition
                    __token = 2356
                    __condition = (_lookup_attr(getitem('industry'), 'get_property')('enabled', getitem('economy')) == True)
                    if __condition:

                        # <Interpolation value=<Substitution '\n                item(FEAT_INDUSTRYTILES, ${tile.id}, ${tile.numeric_id}) {\n                    property {\n                        accepted_cargos:  [${tile.get_expression_for_tile_acceptance(industry, economy)}];\n                    }\n                }\n            ' (47:98)> braces_required=True translation=False at 1e325b1b198> -> __content_2075086945112
                        __token = 2424
                        __token = 2451
                        __content_2075086945112 = _lookup_attr(getitem('tile'), 'id')
                        __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                        __token = 2463
                        __content_2075086945112_2461 = _lookup_attr(getitem('tile'), 'numeric_id')
                        __content_2075086945112_2461 = __quote(__content_2075086945112_2461, '\x00', '&#0;', None, False)
                        __token = 2559
                        __content_2075086945112_2557 = _lookup_attr(getitem('tile'), 'get_expression_for_tile_acceptance')(getitem('industry'), getitem('economy'))
                        __content_2075086945112_2557 = __quote(__content_2075086945112_2557, '\x00', '&#0;', None, False)
                        __content_2075086945112 = ('%s%s%s%s%s%s%s' % ('\n                item(FEAT_INDUSTRYTILES, ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ', ', (__content_2075086945112_2461 if (__content_2075086945112_2461 is not None) else ''), ') {\n                    property {\n                        accepted_cargos:  [', (__content_2075086945112_2557 if (__content_2075086945112_2557 is not None) else ''), '];\n                    }\n                }\n            ', ))
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
                    __append('\n        }\n    ')
                    ____index_2075101607696 -= 1
                    if (____index_2075101607696 > 0):
                        __append('')
                if (__backup_economy_2075083927448 is __marker):
                    del econtext['economy']
                else:
                    econtext['economy'] = __backup_economy_2075083927448
                __append('\n')
                ____index_2075101627392 -= 1
                if (____index_2075101627392 > 0):
                    __append('')
            if (__backup_tile_2075100595928 is __marker):
                del econtext['tile']
            else:
                econtext['tile'] = __backup_tile_2075100595928
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }