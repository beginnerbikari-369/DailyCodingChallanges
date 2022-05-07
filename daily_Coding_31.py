# The edit distance between two strings refers to the minimum number
# of character insertions, deletions, and substitutions required to change
# one string to the other. For example, the edit distance between “kitten”
# and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”,
# and append a “g”.

def mindist(l1, l2):
    count = 0
    diff = len(l2) - len(l1)
    for i in range(len(l1)):
        if l1[i] != l2[i]:
            count +=1
    count += diff
    return count

if __name__ == "__main__":
    # enter small string first
    print(mindist("kitten", "sitting"))