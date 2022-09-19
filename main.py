cook_book = {}

with open ('recipes.txt','r',encoding = 'utf-8') as recipe_list:
    for line in recipe_list:
        recipe_name = line.strip()
        recipe = {recipe_name:[]}
        ingridients_count = recipe_list.readline()
        for i in range(int(ingridients_count)):
            ingridients = recipe_list.readline()
            ingridient, count, si = ingridients.split(' | ')
            ingridient_dict = {'ingridient_name':ingridient, 'quantity':count, 'measure': si.strip()}
            recipe[recipe_name].append(ingridient_dict)
        recipe_list.readline()
        cook_book.update(recipe)



#////////////////////////////////////////////////////////////////////////////////////////

def get_shop_list_by_dishes(dishes, person_count):
    '''Function to count ingredients according to person'''
    for name, recipe in cook_book.items():
        if name in dishes:
            print(name)
            for ingridient in recipe:
                 print( {ingridient['ingridient_name']: {ingridient['measure'],(int(ingridient['quantity']) * person_count)}})
            return

get_shop_list_by_dishes("Омлет" , 5)

# ///////////////////////////////////////////////////////////////////////////////////////

class Book:
    def __init__(self, name):
        self.name = name
        self.text_list = []
        self.count = 0
        self.length_text = 0

    def open_file(self):
        '''Function for work with files'''
        with open(str(self.name), 'r', encoding='utf-8') as file:
            for line in file:
                self.count += 1
                string_file = [f'Строка номер {self.count} файла номер {self.name[0]} {line.strip()}']
                self.text_list.append(string_file)
            self.length_text = len(self.text_list)


    def __lt__(self, other):
        '''File length comparison function'''
        if not isinstance(other, Book):
            print('Ошибка файлов, указанный фаил отсутствует!')
            return
        return self.length_text < other.length_text

file_1 = Book('1.txt')
file_1.open_file()
file_2 = Book('2.txt')
file_2.open_file()
file_3 = Book('3.txt')
file_3.open_file()


total = []

if (file_1 > file_2) == True and (file_3 > file_2) == True:
    total.append(file_2.text_list)
    if file_1 > file_3:
        total.append(file_3.text_list)
        total.append(file_1.text_list)
    else:
        total.append(file_1.text_list)
        total.append(file_3.text_list)

elif  (file_1 < file_2) == True and (file_1 < file_3) == True:
    total.append(file_1.length_text)
    if file_2 > file_3:
        total.append(file_3.length_text)
        total.append(file_2.length_text)
    else:
        total.append(file_2.length_text)
        total.append(file_3.length_text)

elif (file_3 < file_2) == True and (file_1 > file_3) == True:
    total.append(file_3.length_text)
    if file_1 > file_2:
        total.append(file_2.length_text)
        total.append(file_1.length_text)
    else:
        total.append(file_1.length_text)
        total.append(file_2.length_text)

with open('new.txt', 'w', encoding = 'utf-8' ) as file_new:
    for arg in total:
        for k in arg:
            for l in k:
                l = l +'\n'
                file_new.write(l)





