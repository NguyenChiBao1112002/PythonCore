# Iput: nums = [8, 7, 2, 5, 3, 1]
# target = 10
# Output: Pair found (8, 2)
#         or
#         Pair found (7, 3) 

# Input: nums = [5, 2, 6, 8, 1, 9]
# target = 12
# Output: Pair not found

# Medthod 1:
def find_pair_1(arr, target):
    n = len(arr)
    existed_pair = False
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target:
                print(f"Pair found ({arr[i]}, {arr[j]})")
                existed_pair = True

    if existed_pair == False:
        print("Pair not found")



# Method 2:
def find_pair_2(arr, target):
    n = len(arr)
    existed_pair = False
    set_values = set()

    for i in range(n):
        complement = target - arr[i]
        if complement in set_values:
            print(f"Pair found ({arr[i]}, {complement})")
            existed_pair = True
        else:
            set_values.add(arr[i])
        
    if existed_pair == False:
        print("Pair not found")

# Advance: If printing the indexes of the pair:
def find_pair_indexes(arr, target):
    n = len(arr)
    existed_pair = False
    dict_value =  dict()

    for i in range(n):
        complement = target - arr[i]
        # complement is key (check key)
        if complement in dict_value:
            print(f"Pair found ({i}, {dict_value[complement]})")
            existed_pair = True
        else: 
            dict_value[arr[i]] = i
    
    if existed_pair == False:
        print("Pair not found")


nums_1 = [8, 7, 2, 5, 3, 1]
target_1 = 10
nums_2 = [5, 2, 6, 8, 1, 9]
target_2 = 12

print("Results for nums_1: ")
find_pair_2(nums_1, target_1)
print("Results for nums_2: ")
find_pair_2(nums_2, target_2)
