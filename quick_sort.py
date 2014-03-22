#!/usr/bin/python

def quick_sort(numbers):
	if len(numbers) <= 1:
		return numbers
	pivot = numbers.pop(0)
	left = []
	right = []
	for n in numbers:
		( left  if n <= pivot else right ).append(n)
	left = quick_sort(left)
	right = quick_sort(right)
	return left + [pivot] + right

if __name__ == "__main__":
	question = [7,4,3,9,2,1,8]
	print question
	answer = quick_sort(question)
	print answer

