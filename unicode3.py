# *-* coding:utf-8 *-*

import unicodedata

u = unichr(233) + unichr(0x0bf2) + unichr(3972) + unichr(6000) + unichr(13231)

for i, c in enumerate(u):
    print i, '%04x' % ord(c), unicodedata.category(c)
    print unicodedata.name(c)
    print u[i]

# Get numeric value of second character
print unicodedata.numeric(u[1])
