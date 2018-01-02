## Selection sort
# input::: (list) a
# output::: None (input a is sorted)

def sel_sort(a):
	n = len(a)
	for i in range(n-1):
		#find minimum value index
		min_idx = i
		for j in range(i+1, n):
			if a[j] < a[min_idx]:
				min_idx = j
			#Swap minimum and current values
		a[i], a[min_idx] = a[min_idx], a[i]


## Insetion sort
# input::: (list) a
# output::: None (input a is sorted)

def ins_sort(a):
	n = len(a)
	for i in range(1, n):
		key = a[i] #save i-th  value in key
		j = i -1 # j is left index of i

		while j>=0 and a[j] > key:
			a[j+1] = a[j]
			j -=1

		a[j+1] = key


## Merge sort
# input::: (list) a
# output::: None (input a is sorted)

def merge_sort(a):
	n = len(a)

	#Ending condition
	if n<=1:
		return

	mid = n//2
	g1 = a[:mid]
	g2 = a[mid:]
	merge_sort(g1)
	merge_sort(g2)

	#Merge two groups
	i1 = 0
	i2 = 0

	ia = 0 

	while i1<len(g1) and i2 < len(g2):
		if g1[i1] < g2[i2]:
			a[ia] = g1[i1]
			i1 += 1
			ia += 1
		else:
			a[ia] = g2[i2]
			i2 += 1
			ia += 1

	#After finishing comparison, add rest of the components
	while i1 < len(g1):
		a[ia] = g1[i1]
		i1 += 1
		ia += 1
	while i2 < len(g2):
		a[ia] = g2[i2]
		i2 += 1
		ia += 1


## Quick sort
# input::: (list) a
# output: None (input a is sorted)

'''
args
- a : input list
- start: start index for sorting
- end: end index for sorting
'''

def quick_sort_sub(a, start, end):
	#Ending condition: No elements to sort
	if end-start <=0:
		return

	#Select pivot (in here, last value in list)
	pivot = a[end]
	i = start #index for pivot

	for j in range(start, end):
		if a[j] <= pivot:
			a[i], a[j] = a[j] , a[i]
			i +=1
	a[i], a[end] = a[end], a[i]

	quick_sort_sub(a, start, i-1)
	quick_sort_sub(a, i+1, end)

def quick_sort(a):
	quick_sort_sub(a, 0, len(a)-1)


## Binary Search
# input::: (list) a, search target x 
# output::: target's index (if not, return -1)

def binary_search(a,x):
	start = 0
	end = len(a) - 1

	while start <= end:
		mid = (start+end) // 2
		if x == a[mid]:
			return mid
		elif x > a[mid]:
			start = mid + 1
		else:
			end = mid -1
	return -1































