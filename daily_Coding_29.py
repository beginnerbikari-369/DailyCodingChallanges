# Run-length encoding is a fast and simple method of encoding strings.
# The basic idea is to represent repeated successive characters as a
# single count and character. For example, the string "AAAABBBCCDAA"
# would be encoded as "4A3B2C1D2A".

s = input("enter any string:")
count = 0
res = ""
for i in range(len(s)):
    count += 1
    try:
        if s[i] != s[i+1]:
            res += str(count) + s[i]
            count = 0
    except IndexError:
        res += str(count) + s[i]
print(res)
