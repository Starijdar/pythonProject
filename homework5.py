immutable_var = 1, 2, True, "Bread"
print(immutable_var)
#immutable_var [0] = 1 не будет выполнена т.к. не подлежит изменению, однако список внутри изменить можно, например
immutable_var_2 = [1, 2] , 1 , 2 , True , "Bread"
print(immutable_var_2)
immutable_var_2 [0] [1] = 1
print(immutable_var_2)
mutable_list = [1, 2, 2, 2]
print(mutable_list)
mutable_list [0] = 2
print(mutable_list)