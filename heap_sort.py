#!/usr/bin/python

def heap_sort(aList):
	list_size = len(aList) - 1
	for i in range((list_size / 2), -1, -1):
		shift_down(aList, i, list_size)

	for i in range(list_size , 0, -1):
		if aList[0] > aList[i]:
			aList[0], aList[i] = aList[i], aList[0]
			shift_down(aList, 0, i - 1)
	return aList

def shift_down(aList, k, bottom):
	while k * 2 + 1 <= bottom:
		j = 2 * k + 1
	
		if j == bottom:
			child_max = j
		else:
			child_max = j if aList[j] >= aList[j + 1] else j + 1

		if aList[k] >= aList[child_max]:
			return
		else:
			aList[k], aList[child_max] = aList[child_max], aList[k]
			k = child_max
		



if __name__ == "__main__":
	question = [7,4,3,9,2,1,8]
	print question
	answer = heap_sort(question)
	print answer

