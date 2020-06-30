#Given a SORTED array and a target sum, find a pair in the array whose sum is equal to the given part:

#hashmap
#time complexity, space complexity ?
def pair_w_target_1(arr, sum):
    hash = {}
    for i, num in enumerate(arr):
        ##first check if it's in hash table BEFORE assigning
        target = sum - num
        if target in hash:
            return [hash[target], i]

        hash[num] = i

    return [-1, -1]

#two pointers, ONLY WORKS WHEN???? (hint below) 
#time and space
def pair_w_target_2(arr, sum):
    begin_i = 0
    end_i = len(arr) - 1
    while begin_i < end_i:
        curr_sum = arr[begin_i] + arr[end_i]
        if sum == curr_sum:
            return [begin_i, end_i]
        elif sum > curr_sum:
            begin_i += 1
        else:
            end_i -= 1

    return [-1, -1]


def main():
    print("Hashmap: ",pair_w_target_1([1,2,3,4,6], 6))
    ##two pointers only work in sorted arrays
    print("Two-pointers: ", pair_w_target_2([1,2,3,4,6], 6))

main()