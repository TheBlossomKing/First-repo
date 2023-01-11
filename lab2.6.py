"""Написать программу, которая проверяет, можно ли из букв, входящих в слово А, составить слово В."""
from collections import Counter

while (word_a := input("Введите слово А: ").lower()) != "":
    word_b = input("Введите слово Б: ").lower()
    if Counter(word_b) - Counter(word_a):
        print('Нельзя')
    else:
        print('Можно')






