# -*- coding: utf-8 -*-
__filename = 'C:\\Users\\Alex\\Documents\\fernz\\src\\templates\\extra_text_primary.pynml'
__tokens = {59: ('switch(FEAT_INDUSTRIES, SELF, ${industry.id}_extra_text, [\n\tSTORE_TEMP((primary_level1_requirement * ${industry.supply_requirements[2]}) |\n\t(primary_level2_requirement * ${industry.supply_requirements[2]})', 3, 0), 91: ('industry.id', 3, 32), 162: ('industry.supply_requirements[2]', 4, 44), 231: ('industry.supply_requirements[2]', 5, 33), 268: ('16, 0x100),\n\tLOAD_PERM(${industry.perm_storage.var_current_supplies_prod_factor})\n]) {\n\tprimary_level2_bonus: return string(STR_${industry.supply_requirements[1]}_PRODUCTION_4X);\n\tprimary_level1_bonus: return string(STR_${industry.supply_requirements[1]}_PRODUCTION_2X);\n\treturn string(STR_${industry.supply_requirements[1]}_PRODUCTION_1X);\n}', 5, 70), 293: ('industry.perm_storage.var_current_supplies_prod_factor', 6, 13), 398: ('industry.supply_requirements[1]', 8, 43), 490: ('industry.supply_requirements[1]', 9, 43), 560: ('industry.supply_requirements[1]', 10, 21), 834: ('switch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display, 1) {\n    return 0x3800 + string(STR_EMPTY);\n}', 18, 0), 867: ('industry.id', 18, 33)}

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

            # <Interpolation value=<Substitution '\n\nswitch(FEAT_INDUSTRIES, SELF, ${industry.id}_extra_text, [\n\tSTORE_TEMP((primary_level1_requirement * ${industry.supply_requirements[2]}) |\n\t(primary_level2_requirement * ${industry.supply_requirements[2]}) ' (1:57)> braces_required=True translation=False at 1e325982208> -> __content_2075086945112
            __token = 59
            __token = 91
            __content_2075086945112 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __token = 162
            __content_2075086945112_160 = _lookup_attr(getitem('industry'), 'supply_requirements')[2]
            __content_2075086945112_160 = __quote(__content_2075086945112_160, '\x00', '&#0;', None, False)
            __token = 231
            __content_2075086945112_229 = _lookup_attr(getitem('industry'), 'supply_requirements')[2]
            __content_2075086945112_229 = __quote(__content_2075086945112_229, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s%s%s%s%s' % ('\n\nswitch(FEAT_INDUSTRIES, SELF, ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), '_extra_text, [\n\tSTORE_TEMP((primary_level1_requirement * ', (__content_2075086945112_160 if (__content_2075086945112_160 is not None) else ''), ') |\n\t(primary_level2_requirement * ', (__content_2075086945112_229 if (__content_2075086945112_229 is not None) else ''), ') ', ))
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
            __append('<')
            __append('<')

            # <Interpolation value=<Substitution ' 16, 0x100),\n\tLOAD_PERM(${industry.perm_storage.var_current_supplies_prod_factor})\n]) {\n\tprimary_level2_bonus: return string(STR_${industry.supply_requirements[1]}_PRODUCTION_4X);\n\tprimary_level1_bonus: return string(STR_${industry.supply_requirements[1]}_PRODUCTION_2X);\n\treturn string(STR_${industry.supply_requirements[1]}_PRODUCTION_1X);\n}\n\n' (5:69)> braces_required=True translation=False at 1e3259b1518> -> __content_2075086945112
            __token = 268
            __token = 293
            __content_2075086945112 = _lookup_attr(_lookup_attr(getitem('industry'), 'perm_storage'), 'var_current_supplies_prod_factor')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __token = 398
            __content_2075086945112_396 = _lookup_attr(getitem('industry'), 'supply_requirements')[1]
            __content_2075086945112_396 = __quote(__content_2075086945112_396, '\x00', '&#0;', None, False)
            __token = 490
            __content_2075086945112_488 = _lookup_attr(getitem('industry'), 'supply_requirements')[1]
            __content_2075086945112_488 = __quote(__content_2075086945112_488, '\x00', '&#0;', None, False)
            __token = 560
            __content_2075086945112_558 = _lookup_attr(getitem('industry'), 'supply_requirements')[1]
            __content_2075086945112_558 = __quote(__content_2075086945112_558, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s%s%s%s%s%s%s' % (' 16, 0x100),\n\tLOAD_PERM(', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), ')\n]) {\n\tprimary_level2_bonus: return string(STR_', (__content_2075086945112_396 if (__content_2075086945112_396 is not None) else ''), '_PRODUCTION_4X);\n\tprimary_level1_bonus: return string(STR_', (__content_2075086945112_488 if (__content_2075086945112_488 is not None) else ''), '_PRODUCTION_2X);\n\treturn string(STR_', (__content_2075086945112_558 if (__content_2075086945112_558 is not None) else ''), '_PRODUCTION_1X);\n}\n\n', ))
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

            # <Interpolation value=<Substitution '\n\nswitch (FEAT_INDUSTRIES, SELF, ${industry.id}_cargo_subtype_display, 1) {\n    return 0x3800 + string(STR_EMPTY);\n}\n' (16:3)> braces_required=True translation=False at 1e3259b1160> -> __content_2075086945112
            __token = 834
            __token = 867
            __content_2075086945112 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s' % ('\n\nswitch (FEAT_INDUSTRIES, SELF, ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), '_cargo_subtype_display, 1) {\n    return 0x3800 + string(STR_EMPTY);\n}\n', ))
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