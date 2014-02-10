About
=====
eurdep is a python module used to parse EURDEP messages into python lists and dictionaries.

More information on EURDEP [here](http://eurdep.jrc.ec.europa.eu/Basic/Pages/Public/Home/Default.aspx]).

How to install it
=================
The python module can be installed with pip:

```
pip install eurdep
```


Example Usage
=============
```
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

```

Get the source
============

```
git clone https://github.com/palli/eurdep
```
