capitals = {'USA': 'Washington DC',
            'India': 'New Deli',
            'China': 'Beijing',
            'Russia': 'Moscow'}


capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las-Vegas'})
capitals.pop('China')
# capitals.clear()

# print(capitals['China'])
# Выводит ошибку когда нету нужных данных

# print(capitals.get("China"))
# Выводит None когда нету нужных данных

# print(capitals.keys())
#  Only printout keys

# print(capitals.values())
# Prints only values

for key, value in capitals.items():
    print(value, key)
