#given assorted num array, remove all dups, no extra space, after removing all dups, return new length

# [2,2,3,5,5,7,9,9]
def remove_dups(arr):
    #the 0 index is the 0 index of the array, we're looking for the first non_dup_index, and then increase
    if len(arr) == 0:
        return 0

    non_dup_index = 1
    for i in range(1,len(arr)):
        #looking for the number that is different than the first 0 non_dup_index, else it will return 1
        if arr[i] != arr[non_dup_index - 1] :
            #this just switch the number and not the index
            arr[non_dup_index] = arr[i]
            non_dup_index += 1
    return non_dup_index

def remove_dups_2(arr):
    if len(arr) == 0:
        return 0

    slo = 0
    for fast in range(1,len(arr)):
        if arr[fast] != arr[slo]:
            slo += 1
            arr[slo] = arr[fast]
        
    return slo + 1

print("length: ", remove_dups([2,3,3,3,6,9,9]))
print("length2: ", remove_dups_2([2,3,3,3,6,9,9]))

