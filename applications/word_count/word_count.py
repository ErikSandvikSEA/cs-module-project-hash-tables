characters_to_ignore = '" : ; , . - + = / \ | [ ] { } ( ) * ^ & â € 1 ? ” ! '.split(" ")
# characters_to_ignore.append("'")


def sanitize(text):
    for letter in text:
        if letter in characters_to_ignore:
            text = text.replace(letter, "")
    text = text.lower()
    return text


def word_count(text):
    if text == "":
        return {}
    word_count_dict = {}
    sanitized = sanitize(text)
    arr = sanitized.split()
    for word in arr:
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    return word_count_dict


# print(word_count("Hello, my cat. And my cat doesn't say hello back."))
# print(word_count("Hello    hello"))

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )

