# Variables

my_variable = "My string variable"
print(my_variable)

my_string_varialbe = "My string variable"
print(my_string_varialbe)

my_int_variable = 5
print(my_int_variable)

my_int_to_str_variable =  str(my_int_variable)
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))

my_bool_variable = False
print(my_bool_variable)

# Concatenación de variables en un print
print(my_int_variable, my_int_variable, my_bool_variable)

print("este es el valor de:", my_bool_variable)


# Algunas funciones del sistema
print(len(my_int_to_str_variable))

# Variables en una sola lines
name, surname, alias, age = "Abel", "Florido", "Abeloak","38"
print("Me llamo:", name, surname, "tengo", age, "y mi alias es:", alias)

# Imputs

name = input("¿Cuál es tu nombre?")
age = input("¿Cuantos años tiens?")
print(name)
print(age)
