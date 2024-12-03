def is_asce_or_desc(arr):
    if not all([arr[x] < arr[x+1] for x in range(len(arr) -1 )]) and not all([arr[x] > arr[x+1] for x in range(len(arr) -1 )]):
        return False
    return True

def check_bounds(arr): 
    diff = []
    for i in range(len(arr) - 1):
        diff.append(abs(arr[i] - arr[i+1]))
    if not all([x <= 3 and x != 0 for x in diff]):
        return False
    return True
        
    
def exclude_given(arr):
    for i in range(len(arr)):
        print(arr[:i] + arr[i+1:])
        if is_asce_or_desc(arr[:i] + arr[i+1:]) and check_bounds(arr[:i] + arr[i+1:]):
            return True
    return False


        
with open('input.txt', "r") as file:
    data = file.read().splitlines()
    arr = []
    for entry in data: 
        temp_arr = entry.split(' ') 
        arr.append(list(map(int, temp_arr)))
    
    safe_counter = 0
    # for entry in arr:
    #     if (is_asce_or_desc(entry) and check_bounds(entry)):
    #         safe_counter += 1
    #         print(f"Safe: {entry}")
    for entry in arr: 
        if is_asce_or_desc(entry) and check_bounds(entry):
            safe_counter += 1
            print(f"Safe: {entry}")
        elif exclude_given(entry):
            safe_counter += 1
            print(f"Safe: {entry}")
    
        
    print(safe_counter)
            


    