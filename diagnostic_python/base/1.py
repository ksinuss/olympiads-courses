def harvesting(data):
    strings = data.split('\n')
    words = [i.split()[-1] for i in strings]
    words = set(words)
    print(*sorted(words), sep='\n')
data1 = '''we have collected a lot of ripe melons
this year a large harvest of wheat
has been born a lot of potatoes
apple trees are bursting with apples
20 bags of wheat'''
data2 = '''15 buckets of cucumbers
a bag of onions
3 baskets of cabbage
5 cans tomato
bed of carrots'''
harvesting(data1)
print()
harvesting(data2)
