## the first one is for arrays w distinct digits

def three_sum_zero (arr):
    triplets = []
    #must sort first
    arr.sort()

    for i in range(len(arr)):
        target =  0 - arr[i]
        left = i+1
        right = len(arr) - 1
        while right > left:
            if arr[right] + arr[left] == target:
                triplets.append([i,arr[right], arr[left]])
                left += 1
                right -= 1
            elif arr[right] + arr[left] < target: 
                left += 1
            else:
                right -= 1
    return triplets

def three_sum_zero_dups(arr):
    triplets = []
    arr.sorted()
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        search_binary(arr, -arr[i], i+1, triplets )
    return triplets

def search_binary(arr, target, l, triplets):
    r = len(arr) -1
    while r >= l:
        curr_sum = arr[r] + arr[l]
        if curr_sum == target:
            triplets.append([-target, arr[l], arr[r]])
            l +=1
            r -=1
            #if previous left is duplicate to curr
            while r >= l and arr[l-1] == arr[l]:
                l += 1
            #if previous right is duplicate to curr
            while r>= l and arr[r+1] == arr[r]:
                l -=1
        elif curr_sum < target:
            l += 1
        else:
            r -= 1
    return triplets
