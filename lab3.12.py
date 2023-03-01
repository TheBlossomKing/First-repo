"""3.12 Напишите программу, удаляющую «крайние» элементы списка"""

lst = input("Enter a list of enything: ").split()
print("Your list: ", lst)
lst.pop(-1)
lst.pop(0)
print("List after delete a word", lst)