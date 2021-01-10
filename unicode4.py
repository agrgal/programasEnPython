# *-* coding:utf-8 *-*

import codecs
  
f = codecs.open('test', encoding='utf-8', mode='w+')
f.write(u'\u4500 blah blah blah\n')
f.seek(0)
print f.readline()[:1]
f.close()
