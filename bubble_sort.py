#!/usr/bin/python

def bubble_sort(numbers):
	for i in xrange(len(numbers) - 1, 0, -1):
		for j in xrange(i):
			if numbers[j] > numbers[j + 1]:
				numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
	return numbers


if __name__ == "__main__":
	question = [7,4,3,9,2,1,8]
	print question
	answer = bubble_sort(question)
	print answer

