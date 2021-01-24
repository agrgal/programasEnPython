# *-* coding: utf-8 *-*

import re
p = re.compile(r'\b(\w+)\s+\1\s+\1\b')
m = p.search("Aquí no hay coca coca cola")

print m.group()

