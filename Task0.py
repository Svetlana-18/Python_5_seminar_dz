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


def text_creation(count: int, word: str = 'абв'):
    words_list = []
    for i in range(count):
        text = sample(word, 3)
        words_list.append("".join(text))
    return " ".join(words_list)


def word_deletion(words: str) -> str:
    return " ".join(i for i in words.split() if i not in "абв")


num = (int(input("Введите количество слов (положительное, целое число): ")))

if num <= 0:
    print('Некорректный ввод, введите целое, положительное число')
else:
    finall_list = text_creation(num)
    print(finall_list)
    print(word_deletion(finall_list))
