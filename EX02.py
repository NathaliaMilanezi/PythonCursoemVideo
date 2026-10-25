n = input('Digite algo: ')

print(f'O tipo primitivo desse valor é {type(n)}')
print(f'Ele pode ser numérico?: {n.isnumeric()}')
print(f'Ele só tem espaços?: {n.isspace()}')
print(f'Ele está todo em letras maiúsculas?: {n.isupper()}')
print(f'Ele é alfabético e numérico?: {n.isalnum()}')

#tem muito mais ainda