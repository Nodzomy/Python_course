def from_file(file):
    dictionary = ""
    with open(file, 'r', encoding='utf-8') as data:
        dictionary = data.read()
    return dictionary