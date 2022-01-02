def get_equal_slices(s, pattern):
    pattern_len = len(pattern)
    sequence_len = len(s)

    # If the length of the sequence is not a multiple of
    # the pattern this is not possible, since there cannot be leftovers.
    if sequence_len % pattern_len != 0:
        return 0

    while s != "":
        curr = s[:pattern_len]
        if curr != pattern:
            return 0
        s = s[pattern_len:] 

    return sequence_len / pattern_len


def solution(s):
    if len(s) < 2:
        return len(s)

    pattern = ""
    for c in s:
        if pattern != "" and c == pattern[0]:
            slices = get_equal_slices(s, pattern)
            if slices > 0:
                return slices
        pattern += c
    # There is always one way to cut a cake; the whole cake :)
    return 1

print(solution("abcabcabcabc"))
print(solution("abccbaabccba"))
print(solution("aa"))