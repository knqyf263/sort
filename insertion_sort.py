#!/usr/bin/python

def insertion_sort(numbers):
	n = len(numbers)
	for i in range(1, n):
		for j in range(0, i + 1):
			if numbers[i] <= numbers[j]:
				numbers[j], numbers[j + 1 : i + 1] = numbers[i], numbers[j : i]
	return numbers


if __name__ == "__main__":
	question = [7,4,3,9,2,1,8]
	print question
	answer = insertion_sort(question)
	print answer

