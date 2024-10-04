# Standard Problem Set Version 1
# PROBLEM 1
## Write a function reverse_sentence() that takes in a string sentence and returns the sentence with the order of the words reversed. The sentence will contain only alphabetic characters and spaces to separate the words. If there is only one word in the sentence, the function should return the original string.
def reverse_sentence(sentence):
  words = sentence.split(" ")
  words = words[::-1]
  words = " ".join(words)
  print(words)
sentence = "tubby little cubby all stuffed with fluff"
reverse_sentence(sentence)
# PROBLEM 2
## In the extended universe of fictional bears, Goldilocks finds an enticing list of numbers in the Three Bears' house. She doesn't want to take a number that's too high or too low - she wants a number that's juuust right. Write a function goldilocks_approved() that takes in the list of distinct positive integers nums and returns any number from the list that is neither the minimum nor the maximum value in the array, or -1 if there is no such number.
def goldilocks_approved(nums):
  if len(nums) <= 2:
    return -1
  [maxNum, minNum] =[ max(nums), min(nums)]
  for i in range(len(nums)):
    if nums[i] != maxNum and nums[i] != minNum:
      return nums[i]
nums = [1,2,3,4,5,6,7,8,9]
print(goldilocks_approved(nums))
# Standard Problem Set Version 2
# Problem 1: String Array Equivalency
def are_equivalent(word1, word2):
  word1 = "".join(word1)
  word2 = "".join(word2)
  return word1 == word2
word1 = ["bat", "man"]
word2 = ["b", "atman"]
print(are_equivalent(word1, word2))

word1 = ["alfred", "pennyworth"]
word2 = ["alfredpenny", "word"]
print(are_equivalent(word1, word2))
#Advanced Problem Set Version 1
#Problem 1: Transpose Matrix
## Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.
def transpose(matrix):
  newMatrix = matrix
  for i in range(len(matrix)):
    for j in range(len(matrix[i])):
      newMatrix[i][j] = matrix[j][i]
  return newMatrix
matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]
print(transpose(matrix))
#Advanced Problem Set Version 2
#Problem 1: Matrix Addition
def add_matrices(matrix1, matrix2):
  '''if the matrices are not the same size, return None'''
  if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
    return None
  for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
      matrix1[i][j] += matrix2[i][j]
  return matrix1
matrix1 = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9]
]

matrix2 = [
  [9, 8, 7],
  [6, 5, 4],
  [3, 2, 1]
]
print(add_matrices(matrix1, matrix2))