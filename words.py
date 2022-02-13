from english_words import english_words_lower_alpha_set

def get_all_5_letter_words():
    words_5 = []

    for word in english_words_lower_alpha_set:
        if len(word) == 5:
            words_5.append(word)

    return words_5
