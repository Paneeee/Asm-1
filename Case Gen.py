import exrex
from re import fullmatch
import random
import time

random.seed(None)
a = random.randint(1,20)
s= "fconst 34.22"
pattern = "((i|f)(add|sub|mul|div|neg|eq|neq|lt|gt))|(i(rem|and|or|bnot|2f))|(f2i)|(top)|(iconst -?[1-9][0-9]{0,5})|(fconst -?[1-9][0-9]{0,5}(|[.][0-9]{1,3}))|((istore|fstore|iload|fload|val|par) [a-zA-Z]+) "
for i in range(0,a):
    print(exrex.getone(pattern))