def lengthOfLongestSubstring(s: str) -> int:
    seen = set()
    l,r = 0,0
    maxLength = 0
    
    while r < len(s):
        while s[r] in seen:
            seen.remove(s[l])
            l += 1
        seen.add(s[r])
        maxLength = max(maxLength, r-l+1)
        r += 1
    return maxLength

if __name__ == "__main__":
    print(lengthOfLongestSubstring("abcabcbb"))