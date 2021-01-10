#!/usr/bin/python
# -*- coding: utf-8 -*-

import unicodedata

# declaro un expresión UNICODE con caracteres de escape
cad = u'\x70\u78f1\u78fa\U00008001'
print cad

u = unichr(15) + unichr(0x0bf2) + unichr(3972) + unichr(6000) + unichr(13231)
print u + "\n"
for i, c in enumerate(u):
    print i, '%04x' % ord(c), unicodedata.category(c),
    print unicodedata.name(c)

# Get numeric value of second character
print unicodedata.numeric(u[1])


