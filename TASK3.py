# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc
#НЕКОРРЕКТНО РАБОТАЕТ С НЕВЕРНЫМ ВВОДОМ!
our_string = ''
path = r'text.txt'

data = open(path, 'r', encoding = 'UTF-8')
# for el in data:
#     our_string += el

our_string = data.readline()
res_string = ""
# print(our_string)
data.close()

path = r'text2.txt'

data = open(path, 'r', encoding = 'UTF-8')
our_string2 = data.readline()
data.close()



def zip_unzip(our_string):
    try:
        int(our_string[0])
        print("Восстанавливаем")
        for i in range(0, len(our_string)):
            try:
                for j in range(0,int(our_string[i])):
                    print(our_string[i+1], end = '')
            except:
                continue

    except:
        print("Сжимаем")
        count = 1
        j = 0
        i = 0
        for i in range(1,len(our_string)):
            if our_string[i] == our_string[i-1]:
                count += 1
            
            else:
                print(str(count) + our_string[i-1], end = '')
                count = 1

        print(str(count) + our_string[i])

zip_unzip(our_string)
zip_unzip(our_string2)