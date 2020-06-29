def longest_substring_with_k_distinct(str, k):
    max_length = 0
    chars_map = {}
    start_chr = 0

    for end_chr in range(len(str)):
        right_char = str[end_chr]
        if right_char not in chars_map:
            chars_map[right_char] = 0
       ##chars_map[right_char] = chars_map[right_char] or 0
        chars_map[right_char] += 1

        while len(chars_map) > k:
            left_char = str[start_chr]
            chars_map[left_char] -= 1
            if chars_map[left_char] == 0:
                del chars_map[left_char]
            start_chr += 1

        max_length = max(max_length, end_chr - start_chr + 1)

    return max_length

def main():
    print("Length of the longest substring: ", str(longest_substring_with_k_distinct("araaci", 2)))
    print("Length of the longest substring: ", str(longest_substring_with_k_distinct("araaci", 1)))
    print("Length of the longest substring: ", str(longest_substring_with_k_distinct("cbbebi", 3)))

main()

