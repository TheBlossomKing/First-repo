"""4.6 Дан текст из строчных латинских букв. Напечатать:
а) первые вхождения букв в текст, по возможности, сохраняя их исходный взаимный порядок;
б) все буквы, входящие в текст не менее двух раз;
в) все буквы, входящие в текст по одному разу.
"""

text = input("Введите текст:  ")
b = text.split()
c = text.lower()
for word in b:

    block1 = ''.join({v for i, v in enumerate(c) if v.isalpha() and v not in c[:i]})
    block2 = ''.join({letter for letter in c if c.count(letter) > 1 and letter != ' '})
    block3 = ''.join({letter for letter in c if c.count(letter) == 1 and letter != ' '})

a = {block1,block2,block3}
print(a)