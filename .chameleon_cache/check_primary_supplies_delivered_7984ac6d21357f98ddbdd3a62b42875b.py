# -*- coding: utf-8 -*-
__filename = 'C:\\Users\\Alex\\Documents\\fernz\\src\\templates\\check_primary_supplies_delivered.pynml'
__tokens = {245: ('industry.perm_storage', 6, 32), 273: ('switch(FEAT_INDUSTRIES, SELF, ${industry.id}_monthly_update, [\n        STORE_PERM(LOAD_PERM(${perm_storage.var_num_supplies_delivered_last}), ${perm_storage.var_num_supplies_delivered_bef_last}),\n        STORE_PERM(LOAD_PERM(${perm_storage.var_num_supplies_delivered}), ${perm_storage.var_num_supplies_delivered_last}),\n        STORE_PERM(0, ${perm_storage.var_num_supplies_delivered})\n    ]) {\n        return CB_RESULT_IND_PROD_NO_CHANGE;\n    }', 7, 4), 305: ('industry.id', 7, 36), 367: ('perm_storage.var_num_supplies_delivered_last', 8, 31), 417: ('perm_storage.var_num_supplies_delivered_bef_last', 8, 81), 500: ('perm_storage.var_num_supplies_delivered', 9, 31), 545: ('perm_storage.var_num_supplies_delivered_last', 9, 76), 617: ('perm_storage.var_num_supplies_delivered', 10, 24)}

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
            __append('\n\n/* =================================== */\n/* Production change evaluated monthly */\n/* =================================== */\n')
            __backup_perm_storage_2075099754904 = get('perm_storage', __marker)

            # <Value 'industry.perm_storage' (6:32)> -> __value
            __token = 245
            __value = _lookup_attr(getitem('industry'), 'perm_storage')
            econtext['perm_storage'] = __value

            # <Interpolation value=<Substitution '\n    switch(FEAT_INDUSTRIES, SELF, ${industry.id}_monthly_update, [\n        STORE_PERM(LOAD_PERM(${perm_storage.var_num_supplies_delivered_last}), ${perm_storage.var_num_supplies_delivered_bef_last}),\n        STORE_PERM(LOAD_PERM(${perm_storage.var_num_supplies_delivered}), ${perm_storage.var_num_supplies_delivered_last}),\n        STORE_PERM(0, ${perm_storage.var_num_supplies_delivered})\n    ]) {\n        return CB_RESULT_IND_PROD_NO_CHANGE;\n    }\n' (6:55)> braces_required=True translation=False at 1e325aa5a58> -> __content_2075086945112
            __token = 273
            __token = 305
            __content_2075086945112 = _lookup_attr(getitem('industry'), 'id')
            __content_2075086945112 = __quote(__content_2075086945112, '\x00', '&#0;', None, False)
            __token = 367
            __content_2075086945112_365 = _lookup_attr(getitem('perm_storage'), 'var_num_supplies_delivered_last')
            __content_2075086945112_365 = __quote(__content_2075086945112_365, '\x00', '&#0;', None, False)
            __token = 417
            __content_2075086945112_415 = _lookup_attr(getitem('perm_storage'), 'var_num_supplies_delivered_bef_last')
            __content_2075086945112_415 = __quote(__content_2075086945112_415, '\x00', '&#0;', None, False)
            __token = 500
            __content_2075086945112_498 = _lookup_attr(getitem('perm_storage'), 'var_num_supplies_delivered')
            __content_2075086945112_498 = __quote(__content_2075086945112_498, '\x00', '&#0;', None, False)
            __token = 545
            __content_2075086945112_543 = _lookup_attr(getitem('perm_storage'), 'var_num_supplies_delivered_last')
            __content_2075086945112_543 = __quote(__content_2075086945112_543, '\x00', '&#0;', None, False)
            __token = 617
            __content_2075086945112_615 = _lookup_attr(getitem('perm_storage'), 'var_num_supplies_delivered')
            __content_2075086945112_615 = __quote(__content_2075086945112_615, '\x00', '&#0;', None, False)
            __content_2075086945112 = ('%s%s%s%s%s%s%s%s%s%s%s%s%s' % ('\n    switch(FEAT_INDUSTRIES, SELF, ', (__content_2075086945112 if (__content_2075086945112 is not None) else ''), '_monthly_update, [\n        STORE_PERM(LOAD_PERM(', (__content_2075086945112_365 if (__content_2075086945112_365 is not None) else ''), '), ', (__content_2075086945112_415 if (__content_2075086945112_415 is not None) else ''), '),\n        STORE_PERM(LOAD_PERM(', (__content_2075086945112_498 if (__content_2075086945112_498 is not None) else ''), '), ', (__content_2075086945112_543 if (__content_2075086945112_543 is not None) else ''), '),\n        STORE_PERM(0, ', (__content_2075086945112_615 if (__content_2075086945112_615 is not None) else ''), ')\n    ]) {\n        return CB_RESULT_IND_PROD_NO_CHANGE;\n    }\n', ))
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
            if (__backup_perm_storage_2075099754904 is __marker):
                del econtext['perm_storage']
            else:
                econtext['perm_storage'] = __backup_perm_storage_2075099754904
            __append('\n')
        except:
            if (__token is not None):
                rcontext.setdefault('__error__', []).append((__tokens[__token] + (__filename, _exc_info()[1], )))
            raise

    return {'render': render, }