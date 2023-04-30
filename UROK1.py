def diff_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        print("Длины массивов не равны!")
        return None

    diff_arr = []
    for i in range(len(arr1)):
        diff_arr.append(arr1[i] - arr2[i])

    return diff_arr


arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8, 10]

result = diff_arrays(arr1, arr2)
print(result) # [-1, -1, -1, -1, -1]

arr1 = [1, 3, 5, 7, 9]
arr2 = [2, 4, 6, 8]

result = diff_arrays(arr1, arr2)
print(result) # Длины массивов не равны! None