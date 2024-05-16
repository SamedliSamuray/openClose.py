with open('text.txt', 'w+', encoding='utf-8') as file:
    file.write('salam azerbaycan, salam naxcivan, salam culfa\n')
    file.write('salam backend, salam python, salam open\n')
    file.seek(0)
    content = file.readline().upper() + file.read()
with open('text.txt', 'w+', encoding='utf-8') as file:   
    file.write(content)
    file.seek(0)
with open('folder.txt', 'w', encoding='utf-8') as new_file:
    new_file.write(content)


