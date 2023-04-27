# leia seu conteúdo
# calcule a porcentagem de livros em cada categoria em relação ao número total de livros.
# O resultado deve ser escrito em um arquivo no formato CSV como o exemplo abaixo.

import json
import csv


def get_category_list(book_list):
    category_list = {}

    for book in book_list:
        for category in book["categories"]:
            if not category_list.get(category):
                category_list[category] = 0

            category_list[category] += 1

    return category_list


def get_book_list_percentage(category_list):
    book_list_percentage = []

    for category, num_books_by_category in category_list.items():
        percentage = num_books_by_category / len(book_list)
        book_list_percentage.append([category, percentage])

    return book_list_percentage


with open("books.json") as file:
    book_list = json.load(file)
    category_list = get_category_list(book_list)
    book_list_percentage = get_book_list_percentage(category_list)


with open("report.csv", "w") as file:
    header = ["categoria", "percentagem"]
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(book_list_percentage)
