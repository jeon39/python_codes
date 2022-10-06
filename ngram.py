
"""
input : 입력된 문자열
count : 잘라 생성할 문자열의 길이
"""
def ngram(input, count):
    """

    for i in range(len(input) - count + 1):
        r.append(input[i:i+count])
    """

    rslt = [input[i:i+count] for i in range(len(input) - count + 1)]

    return rslt
