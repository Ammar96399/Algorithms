def fusion(A, left_index, right_index, middle):
    left_copy = A[left_index:middle + 1]
    right_copy = A[middle + 1:right_index + 1]
    
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            A[sorted_index] = left_copy[left_copy_index]
            left_copy_index += 1

        else: 
            A[sorted_index] = right_copy[right_copy_index]
            right_copy_index += 1

        sorted_index += 1

    while left_copy_index < len(left_copy):
        A[sorted_index] = left_copy[left_copy_index]
        left_copy_index += 1
        sorted_index += 1

    while right_copy_index < len(right_copy):
        A[sorted_index] = right_copy[right_copy_index]
        right_copy_index += 1
        sorted_index += 1

def triFusion (A, left_index, right_index): 
    if left_index >= right_index:
        return

    middle = (left_index + right_index) // 2
    triFusion(A, left_index, middle)
    triFusion(A, middle + 1, right_index)
    fusion(A, left_index, right_index, middle)


A = [99, 101, 34, 22, 32, 8, 33, 12, 54, 44, 44, 44, 12, 0, 44, 12, 100]
triFusion(A, 0, len(A) -1)
print(A)