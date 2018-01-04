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


## Find Same Name People with Dictionary data structure(not using set data structure)
# (d.s. like dictionary that correspond key and value: hash table. in C++: unordered_map, java: hashmap)
# construct dictionary counting the number of each name
'''
command:
>>> name = ["Tom", "Jerry", "Mike", "Tom"]
>>> print find_same_name(name)
{"Tom"}
>>> name = ["Tom", "Jerry", "Mike", "Tom", "Mike"]
{"Tome, Mike"}
'''

def find_same_name(a):
	#count dictionary
	name_dict = {} #or name_dict = dict()
	for name in a:
		if name in name_dict:
			name_dict[name] +=1
		else:
			name_dict[name] =1

	result = set()
	for name in name_dict:
		if name_dict[name] >=2:
			result.add(name)

	return result


## Find friend relationship using graph data structure. Graph is implemedted by dict() and list()
'''
- construct graph
>>> name_list = ['Summer' , 'John', 'Justin', 'Mike', 'May', 'Kim', 'Tom', 'Jerry']
>>> fr_info = {'Summer': [name_list[1],name_list[2],name_list[3]], 'John':[name_list[0],name_list[3]], 'Justin':[name_list[1],name_list[0],name_list[3],name_list[4]], 'Mike':[name_list[0],name_list[2]], 'May':[name_list[2],name_list[5]], 'Kim':[name_list[4]], 'Tom':[name_list[-1]], 'Jerry':[name_list[-2]]}
'''
#find all connected friend of "start"
'''
args
- g: graph information
- start: starting name
'''
def print_all_friends(g, start):
	qu = [] #people name queue to be processed. If name is here, will be procssed
	done = set() #people name set already added, preventing from redendant processing

	qu.append(start)
	done.add(start)

	# redundant check
	while qu:
		p = qu.pop(0)
		print p
		for x in g[p]:
			if x not in done:
				qu.append(x)
				done.add(x)

'''
>>> print_all_friends(fr_info, 'Summer')
Summer, John, Justin, Mike, May, Kim
'''

## Calculate each friends' the level of closeness
def print_all_friends_and_closeness(g, start):
	qu = []
	done = set()

	qu.append((start, 0))
	done.add(start)

	while qu:
		(p, d) = qu.pop(0)
		print (p,d)
		for x in g[p]:
			#if a person is not added yet, increase closeness of the person
			if x not in done:
				qu.append((x, d+1))
				done.add(x)







