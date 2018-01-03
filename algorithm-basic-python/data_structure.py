## Palindrome means the word that have same sequence between original and reverser sequences

#Queue and Stack structure
def palindrome(s):
	qu, st = [], []

	for x in s:
		if x.isalpha():
			qu.append(x.lower())
			st.append(x.lower())

	while qu:
		if qu.pop(0) != st.pop():
			return False

	return True


from collections import deque
def palindrome_deque(s):
	qu, st = deque(), deque()

	for x in s:
		if x.isalpha():
			qu.append(x.lower())
			st.append(x.lower())
	while qu:
		if qu.popleft() != st.pop():
			return False

	return True