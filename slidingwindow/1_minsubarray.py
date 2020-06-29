def smallest_subarray_with_given_sum_array (s, arr):
    min_length = len(arr)
    start_index, sum_window= 0,0 

    for end_index in range(len(arr)):
        #end_index starts first from 0 and add to sum window
        sum_window += arr[end_index]

        while sum_window >= s:
            #end_index - start_index + 1 is the len of window
            min_length = min(min_length, end_index - start_index + 1 )
            #start sliding window by subtracting the start_index number from sum
            sum_window -= arr[start_index]
            start_index += 1
    
    if min_length == len(arr):
        return 0
    return min_length

def main():
    print("Small subarr length: " +str(smallest_subarray_with_given_sum_array(7,[2,1,5,2,3,2])))
    print("Small subarr length: " +str(smallest_subarray_with_given_sum_array(7,[2,1,5,8,2])))

main()

### time: O(N + N) outer loop loops N times, while the inner loop loops each element of the array once no matter what, therefore it's PLUS N NOT N2.
