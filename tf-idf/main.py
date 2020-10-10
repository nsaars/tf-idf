from math import log10
from collections import Counter
from os import listdir, getcwd
from string import punctuation  # строка пунктуционных символов


def compute_tfidf(corpus):  # corpus - список списков(текстов)
    def compute_tf(text):  # text - список слов
        tf_text = Counter(text)
        for i in tf_text:
            tf_text[i] = tf_text[i] / len(text)
        return tf_text

    def compute_idf(word, corpus):
        if len(corpus) == 1:
            return 1
        return log10(len(corpus) / sum([1.0 for i in corpus if word in i]))

    documents_list = []
    for text in corpus:
        tf_idf_dictionary = {}
        computed_tf = compute_tf(text)
        for word in computed_tf:
            tf_idf_dictionary[word] = computed_tf[word] * compute_idf(word, corpus)
        documents_list.append(tf_idf_dictionary)
    return documents_list  # documents_list - список словарей tf_idf_dictionary


folder = getcwd()  # путь к папке с исполняемым файлов


def usages():
    common_amount = 0
    for file in listdir(
            rf"{folder}\texts"):  # rf"{folder}\texts" - путь к папке texts,находящейся в папке с исполняемым файлов
        text = open(rf"{folder}\texts\{file}", "r", encoding="utf-8").read()
        amount = (len(text.split()) + len(text.split(".")) + len(text.split(",")) +
                  len(text.split("?")) + len(text.split("!")))
        common_amount += amount
        print(f"В тексте из файла '{file}'  {amount} словоупотреблений.")
    print(f"Всего {common_amount} словоупотреблений.\n\n")
    return common_amount


amount_of_texts = len(listdir(rf"{folder}\texts"))
main = int(input(f"Какой текст главный?\nОт 1 до {amount_of_texts}\n")) - 1
tran_tab = str.maketrans(dict.fromkeys(punctuation))
texts = [open(rf"{folder}\texts\{file}", "r", encoding="utf-8").read().translate(
    tran_tab).split() for file in listdir(rf"{folder}\texts")]  # .translate(tran_tab) убирает все знаки пунктуации

cti = compute_tfidf(texts)
main_cti = dict(
    sorted(cti[main].items(), key=lambda couple: (-couple[1], couple[0])))  # sorted_computed_tfidf_of_main_text


def print_cti():
    for couple in enumerate(main_cti, 1):
        print(couple, main_cti[couple[1]])  # так удобней читать просто



