#!/usr/bin/python

def selection_sort(numbers):
	n = len(numbers)
	for i in range(n - 1):
		minimum = i
		for j in range(i + 1, n):
			if numbers[j] < numbers[minimum]:
				minimum = j
		numbers[i], numbers[minimum] = numbers[minimum], numbers[i]
	return numbers


if __name__ == "__main__":
	question = [7,4,3,9,2,1,8]
	print question
	answer = selection_sort(question)
	print answer

