def findElement(arr, input):
    n = len(arr)
    for i in range(n):
        if input == arr[i]: 
            return "Element Found"
    
    return "Number not found"


arr = [1, 45, 63, 56, 76, 56 ,89, 91]
print(findElement(arr, 76))