def no_dups(s):
    cache = {}
    str_list = s.split(" ")
    result = []
    for word in str_list:
        if word not in cache:
            cache[word] = True
            result.append(word)
    resultStr = " ".join(result)
    return resultStr


# no_dups("hello hello")


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
