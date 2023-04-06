try:
    file = open('a_file.txt', 'r')
    dict_1 = {'key' : 1}
    print(dict_1['key'])
except FileNotFoundError as e:
    print(f'{e}\ntrying to create the file')
    file = open('a_file.txt', 'w')
    file.write('Something')
except KeyError as error:
    print(f"key {error} doesn't exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()