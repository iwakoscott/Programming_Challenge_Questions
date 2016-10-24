# Generates all possible partitions of S.
def Generator(S, T):
	k, cur_size = 0, 0
	while cur_size < len(S):
		j = cur_size + len(T)
		yield S[k:(j + k)]
		k += 1
		if k + j > len(S):
			cur_size += 1
			k = 0

def Solution(S, T):
	list(T).sort()
	new_T = ''.join(T)

	s = Generator(S, T)

	while True:
		try:
			current = next(s)
			list_curr = list(current)
			intersect = [x for x in list(list_curr) if x in list(T)]
			intersect.sort()
			if new_T in ''.join(intersect):
				print current
				break
		except StopIteration:
			print ""
			break

# Change the values for S, T here!
S, T = "ADOBECODEBANC", "ABC"
Solution(S,T)