#!/usr/bin/python

def merge_sort(numbers):
	if len(numbers) <= 1:
		return numbers
	mid = len(numbers) // 2
	left = numbers[:mid]
	right = numbers[mid:]

	left = merge_sort(left)
	right = merge_sort(right)

	return merge(left, right)

def merge(left, right):
	merged_list = []
	while len(left) > 0 and len(right) > 0:
		min_element = ( left if left[0] <= right[0] else right ).pop(0)
		merged_list.append(min_element)
	merged_list += ( left if left else right )
	
	return merged_list

if __name__ == '__main__':
	question = [7,4,3,9,2,1,8]
	print question
	answer = merge_sort(question)
	print answer
