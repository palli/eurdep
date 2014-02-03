#!/usr/bin/env python
import sys
from collections import namedtuple

__version__ = 0.5


def get_version():
    """ Returns the version number of eurdep  """
    return __version__


def load(data):
    """ Parse a eurdep message and produce a corresponding Python object """
    array = data.splitlines()
    return _load_array(array)


def _load_array(array, line_num=0):
    result = {}
    field_list = []
    field_headers = None
    while array:
        current_line = array.pop(0)
        line_num += 1
        i = current_line.strip('\n').strip('\\').strip(';')
        if not i:
            continue
        elif not current_line.startswith('\\'):
            error("line does not start with a '\\': '%s'" % current_line, line_num)
        elif not current_line.endswith(';'):
            error("line does not end with a ';': '%s'" % current_line, line_num)
        elif i.startswith('BEGIN_'):
            #section = get_section(current_line, lines)
            section_name = i.replace('BEGIN_','')
            result[section_name] = _load_array(array)
        elif i.startswith('END_'):
            if field_list:
                result['field_list'] = field_list
            return result
        elif i.startswith('FIELD_LIST'):
            field_headers = i.split()[1].split(',')
            field_tuple = namedtuple('FIELD_LIST', field_headers)
        elif field_headers:
            fields = i.split(',')
            fields = map(lambda x: x.strip(), fields)
            # we know all the field names, so lets convert our fields into a dict
            field_dict = {}
            for i, e in enumerate(fields):
                field_name = field_headers[i]
                field_dict[field_name] = e
            field_list.append(field_dict)
        else:
            key, value = i.split(None, 1)
            result[key] = value
    return result


def error(message, line_num):
    print "Error on line {line_num}: {message}".format(**locals())
