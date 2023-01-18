our_string = ''
path = r'text.txt'

data = open(path, 'r', encoding='UTF-8')
# for el in data:
#     our_string += el

our_string = data.readline()
res_string = ""
data.close()

path = r'text2.txt'

data = open(path, 'r', encoding='UTF-8')
our_string2 = data.readline()
data.close()


our_string.replace(' ', '')
our_string2.replace(' ', '')

# print(our_string)


def unzip(our_string):
    num_string = ''
    letter_list = []
    for el in our_string:
        if el == '0':
            num_string += '0'
        else:
            try:
                if int(el):
                    num_string += el
            except:
                if el != ' ':
                    num_string += ' '
                    letter_list.append(el)
    num_list = num_string.split()
    for i in range(0, len(num_list)):
        for j in range(0, int(num_list[i])):
            print(letter_list[i], end='')


unzip(our_string2)
