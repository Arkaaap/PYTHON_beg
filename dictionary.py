L = ['eat','ten','tan','ate','nat','bat']
empty_dict = {}

for string in empty_dict:
    key = ''.join(sorted(string))
    empty_dict[key].append(string)

print (empty_dict.values)