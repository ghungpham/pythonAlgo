### Given a string, find the length of the longest substring which has no repeating chars:

def no_repeating_substrings(str):
    max_len = start = 0
    used = {}

    for i, char in enumerate(str):
        """check if the char is already in the hashmap, if it's in the map and that if the start index is behind
        the used dictionary, then we move the start index to the right one index from the used character --> giving 
        the substring non-repeating
        If the start index is higher than the used character index, we need to discount the old one and update with
        the new index
        """
        if char in used and start <= used[char]:
            start = used[char] + 1
        #set chars in the used index
        used[char] = i
        #find max_len for every end-window index
        max_len = max(max_len, i - start + 1)

    return max_len

def main():
    print(str(no_repeating_substrings("aabccbb")))
    print(str(no_repeating_substrings("abbbb")))
    print(str(no_repeating_substrings("abccde")))

main()
