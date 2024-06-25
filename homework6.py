my_dict = {'Ivan' : 2000, 'Daria' : 2003, 'Kirill' : 2001}
print(my_dict)
print(my_dict.get('Ivan'))
print(my_dict.get('Denis', 'Нет такого'))
my_dict.update({
                'Kto-to' : 1650,
                'Jesus' : 0})
print(my_dict)
a = my_dict.pop('Kto-to')
print(a)
print(my_dict)

my_set = {1, 1, 2 ,2 , 'String', 1, 10, 'String'}
print(my_set)
my_set.add(6)
my_set.add("Штринг")
print(my_set)
print(my_set.discard('String'))
print(my_set)