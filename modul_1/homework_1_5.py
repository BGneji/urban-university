immutable_var = (1, 'str', [4, 5])
print('immutable_var', type(immutable_var))
print(immutable_var)
# immutable_var[0] = 3
# print(immutable_var)  # TypeError: 'tuple' object does not support item assignment
# кортеж не изменяемый тип данных


mutable_list = [1, 3, 'a', 'b']
print(mutable_list)
mutable_list[3] = 4
print(mutable_list)