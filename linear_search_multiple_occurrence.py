def findElement(arr, input):
    index = []
    n = len(arr)
    for i in range(n):
        if input == arr[i]: 
            index.append(i)
    return index 


arr = [1, 45, 63, 56, 76, 56 ,89, 91, 76]
print(findElement(arr, 100))