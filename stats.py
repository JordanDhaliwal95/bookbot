def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        alpha = c.isalpha()
        if alpha and lowered in chars:
           chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sorted_chars_dict(chars_dict):
    sorted_chars = list(chars_dict.items())
    sorted_chars.sort(key=lambda item: item[1], reverse=True)
    [{only_chars, count} for only_chars, count in sorted_chars]
    for only_chars, count in sorted_chars:
        print(f"{only_chars}: {count}")
    

