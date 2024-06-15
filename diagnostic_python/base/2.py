def sleepover(*data):
    a = {}
    for words in data:
        word = words.lower()
        count = word.count('a')
        if count in a: a[count].append(words)
        else: a[count] = [words]
    for counts in a:
        a[counts].sort(reverse=True)
    return a

data1 = [
    'Hydrus', 'Pavo', 'Corvus', 'Gemini',
    'Andromeda', 'Antlia', 'Microscopium',
    'Musca', 'Delphinus'
]
data2 = [
    'Lynx', 'Orion', 'Piscis',
    'Lacerta', 'Indus',
    'Triangulum', 'Cepheus'
]

print(sleepover(*data1))
print(sleepover(*data2))