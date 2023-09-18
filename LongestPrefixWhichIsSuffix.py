def longestPrefixSuffix(str: str) -> str:
    n = len(str)
    ans = ""
    for i in range(n-1, 0, -1):
        prefix = str[:i]
        suffix = str[-i:]
        if prefix == suffix:
            if len(prefix) > len(ans):
                ans = prefix
    return ans

def main():
    #
    str = input()
    print(longestPrefixSuffix(str))