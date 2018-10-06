# -*- coding: utf-8 -*-
__filename = 'C:\\Users\\Alex\\Documents\\fernz\\src\\templates\\header.pynml'
__tokens = {0: ('grf {\n\tgrfid: "JB00";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ${repo_vars.repo_revision};\n\tmin_compatible_version: 5932;\n\tparam 0 {', 1, 0), 119: ('repo_vars.repo_revision', 6, 12), 312: ('economy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(economies)-1};\n\t\t\tnames: {', 10, 2), 451: ('len(economies)-1', 14, 16), 526: ('economies', 16, 44), 558: ('${repeat.economy.index}: string(STR_PARAM_VALUE_ECONOMIES_${economy.id});', 17, 20), 560: ('repeat.economy.index', 17, 22), 618: ('economy.id', 17, 80), 1441: ('param 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}', 52, 1), 2055: ('global_constants.FARM_MINE_SUPPLY_REQUIREMENT', 74, 16), 2325: ('5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT', 83, 16)}

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

            # <Interpolation value=<Substitution 'grf {\n\tgrfid: "JB00";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ${repo_vars.repo_revision};\n\tmin_compatible_version: 5932;\n\tparam 0 {\n\t    ' (1:0)> braces_required=True translation=False at 1e325885d30> -> __content_2075086945112
            __token = 0
            __token = 119
            __content_2075086945112 = _lookup_attr(getitem('repo_vars'), 'repo_revision')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s' % ('grf {\n\tgrfid: "JB00";\n\tname: string(STR_GRF_NAME);\n\tdesc: string(STR_GRF_DESC);\n\turl: string(STR_GRF_URL);\n\tversion: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n\tmin_compatible_version: 5932;\n\tparam 0 {\n\t    ', ))
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

            # <Interpolation value=<Substitution '\n\t\teconomy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ${len(economies)-1};\n\t\t\tnames: {\n\t\t\t    ' (9:122)> braces_required=True translation=False at 1e325885dd8> -> __content_2075086945112
            __token = 312
            __token = 451
            __content_2075086945112 = (len(getitem('economies')) - 1)
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s' % ('\n\t\teconomy_selection {\n\t\t\tname: string(STR_PARAM_NAME_ECONOMIES);\n\t\t\tdesc: string(STR_PARAM_DESC_ECONOMIES);\n\t\t\tmin_value: 0;\n\t\t\tmax_value: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n\t\t\tnames: {\n\t\t\t    ', ))
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
            __backup_economy_2075083912920 = get('economy', __marker)

            # <Value 'economies' (16:44)> -> __iterator
            __token = 526
            __iterator = getitem('economies')
            (__iterator, ____index_2075098898328, ) = getitem('repeat')('economy', __iterator)
            econtext['economy'] = None
            for __item in __iterator:
                econtext['economy'] = __item

                # <Interpolation value=<Substitution '\n                    ${repeat.economy.index}: string(STR_PARAM_VALUE_ECONOMIES_${economy.id});\n\t\t\t    ' (16:55)> braces_required=True translation=False at 1e3258a1048> -> __content_2075086945112
                __token = 558
                __token = 560
                __content_2075086945112 = _lookup_attr(_lookup_attr(getitem('repeat'), 'economy'), 'index')
                __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
                __token = 618
                __content_2075086945112_616 = _lookup_attr(getitem('economy'), 'id')
                __content_2075086945112_616 = __quote(__content_2075086945112_616, '\x00', '&#0;', None, False)
                __content_2075086945112 = ('%s%s%s%s%s' % ('\n                    ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ': string(STR_PARAM_VALUE_ECONOMIES_', (__content_2075086945112_616 if (__content_2075086945112_616 is not None) else ''), ');\n\t\t\t    ', ))
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
                ____index_2075098898328 -= 1
                if (____index_2075098898328 > 0):
                    __append('')
            if (__backup_economy_2075083912920 is __marker):
                del econtext['economy']
            else:
                econtext['economy'] = __backup_economy_2075083912920
            __append('\n\t\t\t};\n\t\t}\n\t}\n\tparam 2 {\n\t\t')
            __append('\n\t\t')
            __append('\n\t\tallow_close_secondary {\n\t\t\tname: string(STR_PARAM_NAME_SECONDARY_NEVER_CLOSE);\n\t\t\tdesc: string(STR_PARAM_DESC_SECONDARY_NEVER_CLOSE);\n\t\t\ttype: bool;\n\t\t\tbit: 1;\n\t\t}\n\t\trestrict_open_during_gameplay {\n\t\t\tname: string(STR_PARAM_NAME_NO_OPENINGS);\n\t\t\tdesc: string(STR_PARAM_DESC_NO_OPENINGS);\n\t\t\ttype: bool;\n\t\t\tbit: 2;\n\t\t}\n\t}\n\t')
            __append('\n\t')

            # <Interpolation value=<Substitution '\n\tparam 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ${5 * global_constants.FARM_MINE_SUPPLY_REQUIREMENT};\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}\n\n' (51:6)> braces_required=True translation=False at 1e3258a10b8> -> __content_2075086945112
            __token = 1441
            __token = 2055
            __content_2075086945112 = _lookup_attr(getitem('global_constants'), 'FARM_MINE_SUPPLY_REQUIREMENT')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __token = 2325
            __content_2075086945112_2323 = (5 * _lookup_attr(getitem('global_constants'), 'FARM_MINE_SUPPLY_REQUIREMENT'))
            __content_2075086945112_2323 = __quote(__content_2075086945112_2323, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s%s%s' % ('\n\tparam 7 {\n\t\tprimary_level1_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 150;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 9 {\n\t\tprimary_level2_produced_percent {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_BONUS);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_BONUS);\n\t\t\tdef_value: 300;\n\t\t\tmin_value: 100;\n\t\t\tmax_value: 1000;\n\t\t}\n\t}\n\tparam 6 {\n\t\tprimary_level1_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL1_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ';\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 8 {\n\t\tprimary_level2_requirement {\n\t\t\tname: string(STR_PARAM_NAME_PRIMARY_LEVEL2_REQUIREMENT);\n\t\t\tdesc: string(STR_PARAM_DESC_PRIMARY_LEVEL_REQUIREMENT);\n\t\t\tdef_value: ', (__content_2075086945112_2323 if (__content_2075086945112_2323 is not None) else ''), ';\n\t\t\tmin_value: 1;\n\t\t\tmax_value: 10000;\n\t\t}\n\t}\n\tparam 4 {\n\t\tmarine_industry_max_coastal_distance {\n\t\t\tname: string(STR_PARAM_NAME_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\tdesc: string(STR_PARAM_DESC_COAST_DISTANCE_MARINE_INDUSTRY);\n\t\t\ttype: int;\n\t\t\tdef_value: 0;\n\t\t\tmin_value: 0;\n\t\t\tmax_value: 255;\n\t\t\tnames: {\n\t\t\t\t0: string(STR_PARAM_VALUE_SECONDARY_NEVER_CLOSE_0);\n\t\t\t};\n\t\t}\n\t}\n}\n\nbasecost {\n\tPR_BUILD_INDUSTRY: 2;       // Industries are more expensive\n\tPR_BUILD_INDUSTRY_RAW : 2;  // Building primary industries is also expensive\n\tPR_CLEAR_INDUSTRY : 2;      // Deleting industries must also be expensive\n}\n\n', ))
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
            __append('\nif (param[6] == 0) { param[6] = 100; }\nif (param[7] == 0) { param[7] = 100; }\nif (param[8] == 0) { param[8] = 400; }\nif (param[9] == 0) { param[9] = 300; }\n\n')
            __append('\ndisable_item(FEAT_INDUSTRIES, 0, 36);\n\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }