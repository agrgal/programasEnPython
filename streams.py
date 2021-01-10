# -*- coding: utf-8 -*-

import sys

while True:
  # Escribo
  print "Yet another iteration ..."
  try:
    # lwywndo desde stdin
    print >> sys.stdout, "Introduce un número: ", ;
    # number = sys.stdin.readline()[:-1]
    number = raw_input("")
    number = int(number)
  except EOFError:
    print >> sys.stdout, "\nHasta luego, Lucas"
    break
  except ValueError:
	print >> sys.stdout, "\nNo es un número"
  else:
    if number == 0:
      print >> sys.stderr, "0 no tiene inverso"
    else:
      print "inverso de %d es %f" % (number, 1.0/number) 
