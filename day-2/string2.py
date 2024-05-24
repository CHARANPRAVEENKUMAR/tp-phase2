a="charan"
c=['i','am','charan']
print(a.split())
print(a.split('a'))
print(a.split('a',maxsplit=1))
print(a.partition('a'))
print(" ".join(c))
try:
    print(a.index('j'))
except :
    print("error")