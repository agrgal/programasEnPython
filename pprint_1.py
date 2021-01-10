# -*- coding: utf-8 -*-

from pprint import pprint

data = [ (i, { 'a':'A',
               'b':'B',
               'c':'C',
               'd':'D',
               'e':'E',
               'f':'F',
               'g':'G',
               'h':'H',
               })
         for i in xrange(3)
         ]

print 'PRINT:'
print data
print
print 'PPRINT:'
pprint(data)

