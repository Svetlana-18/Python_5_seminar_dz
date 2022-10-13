# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
# in
# Number of words: -1

# out
# The data is incorrect

from random import sample


def list_rand_words(count: int, alp: str = 'абв'):
    words_list = []
    for i in range(count):
        letters = sample(alp, 3)
        words_list.append("".join(letters))
    return " ".join(words_list)


# def list_rand_words(count: int, alp: str = 'абв'):
#     return " ".join("".join(sample(alp, 3)) for _ in range(count))


def simple_sentence(words: str) -> str:
    # return " ".join(words.replace("абв", "").split())
    return " ".join(i for i in words.split() if i != "абв")


all_list = list_rand_words(int(input("Number of words: ")))
print(all_list)
print(simple_sentence(all_list))