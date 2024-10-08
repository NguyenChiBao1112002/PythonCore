# Input:  { 6, 0, 8, 2, 3, 0, 4, 0, 1 }
# Output: { 6, 8, 2, 3, 4, 1, 0, 0, 0 }

def move_zero_to_end(arr):
    n = len(arr)
    total_of_zero = arr.count(0)
    

    while total_of_zero > 0:
        arr.remove(0)
        arr.append(0)
        total_of_zero -= 1
    
    return arr


test_case = [6, 0, 8, 2, 3, 0, 4, 0, 1]
print(move_zero_to_end(test_case))

