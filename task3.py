def print_params(a=1,b='строка',c=True):
    print(a,b,c)
value_list=(3,'урбан',False)
print_params(*value_list)
values_dict={"a":"Строка",'b':52,'c':[1,2,3]}
print_params(**values_dict)
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)