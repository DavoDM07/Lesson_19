#Given two dictionaries, merge them into a new dictionary, excluding any keys
#that start with an underscore.

dict1 = {'a': 1, 'b': 2, '_c': 3}
dict2 = {'d': 4, '_e': 5, 'f': 6}

dicts = {k: v for d in (dict1, dict2) for k, v in d.items() if not k.startswith('_')}
print(dicts)