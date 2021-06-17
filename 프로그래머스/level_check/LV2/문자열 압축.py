import sys

def solution(s):
    min_len = sys.maxsize

    for filter_size in range(1, len(s) + 1):
        result = ''
        start = 0
        while start < len(s):
            end = start + filter_size
            chunk = s[start: end]

            i, count = 0, 1
            same = True
            while same:
                same = (chunk == s[end + i: end + i + filter_size])
                i += filter_size
                count += 1
            i -= filter_size
            count -= 1

            if count > 1:
                result += str(count) + chunk
                start += count * filter_size
            else:
                result += chunk
                start += filter_size
        min_len = min(len(result), min_len)
    return min_len