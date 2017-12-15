# import random
# from itertools import permutations

# print 'hey'
# def secret_santa(names):
#     '''Creates dictionary of pair for givers and receivers of gifts'''
# 	results = {}
# 	perms = list(permutations(names, len(names)))
# 	print(len(perms))
# 	sequence = random.choice(perms)

# 	for i, name in enumerate(sequence):
# 		try:
# 			results[name] = sequence[i + 1]
# 		except IndexError:
# 			results[name] = sequence[0]
# 	return results

# results = secret_santa(['John', 'Jeff', 'Jake', 'Ben', 'Carol', 'Jenny'])
# print(results)
print 'hey'