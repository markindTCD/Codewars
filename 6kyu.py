#Username in codewars.com: markindTCD
#At this point, I have 6th Kyu


#Kata Permutations (4kyu): In this kata you have to create all permutations of a non empty input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.
#For example: With input 'aabb' -> Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
#Solution:
import itertools
def permutations(string):
    return list("".join(p) for p in set(itertools.permutations(string)))


#Kata Matrix determinant (4kyu): Write a function that accepts a square matrix (N x N 2D array) and returns the determinant of the matrix.
#Solution:
import numpy as np
def determinant(matrix):
  if len(matrix) == 1:return matrix[0][0]
  else: 
    det = 0
    for j in range(0, len(matrix[0])):
      new_matrix = np.delete(np.delete(matrix, 0, 0), j, 1)
      det += (-1)**(j+1+1) * matrix[0][j] * determinant(new_matrix)
    print(det)
  return det


#Kata Maximum subarray sum (5kyu): The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:
#Example: max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) -> should be 6: [4, -1, 2, 1]
#Solution:
from math import inf
maxint=inf
def max_sequence(a):
    size = len(a)
    max_so_far = -maxint - 1
    max_ending_here = 0
      
    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
 
        if max_ending_here < 0:
            max_ending_here = 0  
    if max_so_far <= 0:
        max_so_far =0
    
    return max_so_far


#Kata Rot13 (5kyu): ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. ROT13 is an example of the Caesar cipher.Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers or special characters included in the string, they should be returned as they are. Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
#Solution:
alphabet = 'abcdefghijklmnopqrstuvwxyz'
lower = [*alphabet]
higher = [*alphabet.upper()]

def rot13(message):
  string = []
  for letter in [*message]:
    i = 0
    if letter.islower():
      while lower[i] != letter: 
        i += 1
      j = i+13
      if j>=len(lower):
        j = 13 - (len(lower) - i)
      string.append(lower[j])
    elif letter.isupper():
      while higher[i] != letter: 
        i += 1
      j = i + 13
      if j>=len(higher):
        j = 13 - (len(higher) - i)
      string.append(higher[j])
    else:
      string.append(letter)
  return ''.join(string)

