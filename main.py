from csv import reader

#num1
cnt = 0
with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        if (len(row[1]) >= 30):
            cnt += 1
print('Количество записей, у которых в поле Название строка длиннее 30 символов:', cnt, '\n')


#num2
flag = 0
search = input('Search for: ')
with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        lower_case = row[2].lower()
        index = lower_case.find(search.lower())
        if index != -1:
            if (int(row[3]) >= 2018):
                flag = 1
                print(row[1], row[2], '\n')
if flag == 0:
    print('Nothing found', '\n')


#num3
num = 0
output = open('result.txt', 'w')
with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[1:21]:
        num += 1
        output.write(f'{num}. {row[2]}. {row[1]}. {row[3]}.\n')

output.close()


#add_num1
from itertools import groupby


publisher_mas = []
with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        publisher_mas.append(row[4])
    new_publisher_mas = [el for el, _ in groupby(publisher_mas)]
print(new_publisher_mas, '\n')


#add_num2
dict = {}
nums = 0
output = open('result_add.txt', 'w')
with open('books-en.csv', 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        dict[row[1], row[2]] = int(row[5])
    sorted_dict = sorted(dict.items(), key=lambda item: item[1], reverse=True)
    print(sorted_dict[:21])

output.close()