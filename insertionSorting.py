def triInsertion(A):
    for j in range (1, len(A)):
        cle = A[j]
        i = j - 1
        while (i >= 0 and A[i] > cle):
            A[i + 1] = A[i]
            i-=1
        A[i + 1] = cle   

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
triInsertion(arr)
print ("Sorted array is:")
for i in range(n):
    print ("%d" %arr[i]),