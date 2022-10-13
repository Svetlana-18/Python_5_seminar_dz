# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'

# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ


from itertools import groupby, starmap
from os import path


def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text) and path.exists(code_text):
        with open(text) as my_f_1, \
                open(code_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write(
                    "".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
                print("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("The files do not exist in the system!")


def rle_decode(code_text="text_code_words.txt", decode_text="text_decode_words.txt"):
    if path.exists(code_text):
        with open(code_text) as my_f_2, \
                open(decode_text, "a") as my_f_3:
            n = ""
            for k in my_f_2:
                word_nums = []
                for i in k.strip():
                    if i.isdigit():
                        n += i
                    else:
                        word_nums.append([int(n), i])
                        n = ""
                print("".join(starmap(lambda x, y: x * y, word_nums)))
                my_f_3.write("".join(starmap(lambda x, y: x * y, word_nums)))
    else:
        print("The files do not exist in the system!")


rle_encode("text_words.txt", "text_code_words.txt")
rle_decode("text_code_words.txt", "text_decode_words.txt")
