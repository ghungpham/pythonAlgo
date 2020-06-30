##Given a sorted array, create a new array containing squares of all number of input array in SORTED order
# [-2,-1,0, 2, 3] to [0,1,4,4,9]

def make_square2(arr):
    squares = [0] * len(arr)
    left = 0
    right = len(arr) - 1
    index_sq = len(squares) - 1

    while left <= right:
        ## why not left < right?
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2
        if left_square > right_square:
            squares[index_sq] = left_square
            left += 1
        else:
            squares[index_sq] = right_square
            right -= 1
        index_sq -= 1

    return squares

def make_square(arr):
    #space = O(n)
    ans= []
    p_index = n_index = 0
    #making pos index points to 0 and above
    while p_index < len(arr) and arr[p_index] < 0:
        p_index += 1
    #making neg points to the first neg before 0:
    n_index = p_index - 1

    while n_index >=0 and p_index < len(arr):
        n_square = arr[n_index] ** 2
        p_square = arr[p_index] ** 2
        if n_square > p_square:
            ans.append(p_square)
            p_index += 1
        else:
            ans.append(n_square)
            n_index -= 1

    #one leftover that needs to get in
    while n_index >= 0:
        ans.append(arr[n_index]**2)
        n_index -= 1
    while p_index < len(arr):
        ans.append(arr[p_index]**2)
        p_index += 1


    return ans



arr1 = [-8,-3,-1,0,1,2,5]

print(str(arr1) + " to " + str(make_square(arr1)))
print(str(arr1) + " to " + str(make_square2(arr1)))
        



