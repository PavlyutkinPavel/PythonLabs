import re


def count_sentences(text):
    """Count the number of sentences in the given text"""
    return len(re.findall(r'[^.]{2}[.]\s', text)) + len(re.findall(r'[.]{3}\s', text))


def count_of_non_declarative_sentences(text):
    """Count the number of non-declarative sentences in the given text"""
    return len(re.findall(r'[?!]\s', text))


def average_sentence_length(text):
    """Calculate the average sentence length in characters"""
    sentences = re.findall(r'(?=\s[A-Z0-9]).*?(?=[.?!]\s)', text)
    count_of_sentences = len(sentences)
    count_char = 0

    if count_sentences == 0:
        return 0

    for sent in sentences:
        words = re.findall(r'(?=\w).*?(?=\W)', sent + ' ')
        for w in words:
            if len(w) == len(re.findall(r'\d', w)):
                continue
            count_char += len(w)

    return count_char / count_of_sentences


def average_word_length(text):
    """Calculate the average word length in characters"""
    words = re.findall(r'(?=\w).*?(?=\W)', text)
    count_words = len(words)
    count_char = 0

    for w in words:
        if len(w) == len(re.findall(r'\d', w)):
            continue
        count_char += len(w)

    return count_char / count_words


def top_ngrams(text: str, K=10, N=4):
    """Return the top k n-grams in the given text(words), by default K = 10 and N = 4"""
    n_grams: dict[str, int] = {}
    words = re.findall(r'(?=\w).*?(?=\W)', text.lower())

    for i in range(len(words) - N + 1):
        n_gram = ' '.join(x for x in words[i:i + N])
        if n_gram in n_grams:
            n_grams[n_gram] += 1
        else:
            n_grams[n_gram] = 1

    return sorted(n_grams.items(), reverse=True, key=lambda item: item[1])[:K]


input_text = 'This is a text that do not give you anything 123 a32 with some separators, and ' \
             'multiple sentences. Ba-ba-ba... Hello, my name is Pavel, what about you? Fuck ' \
             'Abbreviations can also appear a1b2c3, but remember not with numbers like 1234. ' \
             'Today i will pass you lab. 28! Hi there. Hi... There. Is anyone here? Yes   ' \
             'How are you? I am fine! Today i pass my lab that i wrote all weekends. Shizofreniya i have ! '

print("Count sentences:", count_sentences(' ' + input_text + ' '))
print("Count of non declarative sentences:", count_of_non_declarative_sentences(' ' + input_text + ' '))
print("Average sentence length:", average_sentence_length(' ' + input_text + ' '))
print("Average word length:", average_word_length(' ' + input_text + ' '))
print("Top ngrams:", top_ngrams(' ' + input_text + ' '))
