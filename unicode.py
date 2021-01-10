#!/usr/bin/python
# -*- coding: utf-8 -*-

s = unicode("abcde")
print type(s)
print s

s = unicode("abcdeñ", errors="ignore")
print s
s = unicode("abcdeñ", errors="replace")
print s
s = unicode("abcdeñ", errors="strict")
print s

