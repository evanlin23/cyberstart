a = "03 09 0e 02 09 08 0b 15 13 03 01 02 05 05"
m = [int(x, 16) for x in a.split()]
s = "swi&CNJCtPVbCyyAmNG8PqFZsYpyXegEQRGt"
print([s[i] for i in m], end='')

b = ['&', 'P', 'y', 'i', 'P', 't', 'b', 'q', '8', '&', 'w', 'i', 'N', 'N']
c=''
for item in b:
    c+=item
print(c)
