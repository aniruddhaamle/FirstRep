def findTriplets(arr, n, sum):
 
    for i in range(0, n - 2): 
        for j in range(i + 1, n - 1): 
            for k in range(j + 1, n):
                if (arr[i] + arr[j] +
                    arr[k] == sum): 
                    print(arr[i], " ", 
                          arr[j], " ", 
                          arr[k], sep = "")
             
# Driver code
arr = [ 10, 20, 30, 9]
n = len(arr) 
findTriplets(arr, n, 59)