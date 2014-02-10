#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# tests for eurdep module
# Copyright (C) 2014 Pall Sigurdsson
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import pprint
import eurdep

with open('data/IS20131215-reitr.EUR') as f:
    data = f.read()
    result = eurdep.load(data)
    for i in result['EURDEP']:
        message_id = i['HEADER'][0]['MESSAGE_ID'][0]
        sent_at = i['HEADER'][0]['SENT'][0]
        importance = i['HEADER'][0]['IMPORTANCE'][0]

        value = i['RADIOLOGICAL'][0]['field_list'][0]['VALUE']
        unit = i['RADIOLOGICAL'][0]['DEFAULT'][0]['UNIT'][0]

        print "# Message ID:", message_id
        print "# Sent at %s" % sent_at
        print "%f %s" % (float(value), unit)
        print ""

# Use this to print the whole result
# pp = pprint.PrettyPrinter(indent=4)
# pp.pprint(result)
