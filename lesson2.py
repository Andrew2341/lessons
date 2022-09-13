#Функции
def sum(a, b = 1):
    return a+b

print(sum(4, 4))
print(sum(14, 4))
print(sum(54, 4))

#userInput = int(input())
#print(sum(userInput, 4))

print(sum(4))

#Работа с файлами

# file = open("lore.txt")
# print(file.read())
#
# for line in file:
#     print(line)

# file = open("textnt.txt", "w")
# file.write("privet")
# file.close()

def record_to_file(add_to_file_that, file_name = "record.txt"):
    file = open(file_name, "a")
    file.write(add_to_file_that)
    file.close()

writing_in_file = str(input())

record_to_file(writing_in_file)
