# we have a string of and a value k we can change k alphabets into other alphabets give the longest substtring containing same aplabets

def longest_substring(s, k):
    max_length = 0
    max_count = 0
    char_count = {}
    left = 0

    for right, char in enumerate(s):
        char_count[char] = char_count.get(char, 0) + 1
        max_count = max(max_count, char_count[char])

        while (right - left + 1 - max_count) > k:
            char_count[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    result = longest_substring(s, k)
    print(f"The longest substring with at most {k} replacements is {result}.")
