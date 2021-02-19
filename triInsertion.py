from array import *

i = 0
a = [5, 2, 4, 6, 1, 3]
insert = [5, 0, 0, 0, 0, 0]
for j in range (0, 6):
    cle = a[j]
    insert[j] = a[j]
    i = j - 1
    print(insert)
    while i > 0 and insert[i] > cle:
        insert[i+1] = insert[i]
        i = i - 1 
    insert[i+1] = cle
print(insert) 
