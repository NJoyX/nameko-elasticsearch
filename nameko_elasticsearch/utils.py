from __future__ import unicode_literals, print_function, absolute_import

from werkzeug.utils import import_string

__author__ = 'Fill Q'

json = filter(None, map(lambda j: import_string(j, silent=True), [
    'rapidjson',
    'ujson',
    'simplejson',
    'json'
]))[0]
