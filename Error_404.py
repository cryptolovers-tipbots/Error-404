#Error 404 by CryptoLover705.
#Modifying form.
#Suggestions are welcome!
#Date: 16/09/2020
#Author: CryptoLover705
def decor(f):
 def wrap():
  print("|"+"="*35+"|")
  f()
  print("|"+"="*35+"|")
 return wrap
def decor1(f):
 def wrap1():
  print("|"+" "*11+"|"+"="*11+"|"+" "*11+'|')
  f()
  print("|"+" "*11+"|"+"="*11+"|"+" "*11+'|')
 return wrap1

def decor2(f):
 def wrap2():
  for k in range(7):
   if k==3:
    f()
   else:
    print("|"+" "*35+"|")
 return wrap2
@decor
@decor2
@decor1
def b():
 print("|"+" "*11+"| Error 404 |"+11*' '+'|')
b()
@decor
@decor2
def a():
 print("""|          Roses are red            |
|        The earth is round         |
|    The page you've searched for   |
|          Cannot be found          |""")
a()
