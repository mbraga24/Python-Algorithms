# Solution 1:

# Time Complexity: O(n)
# Space Complexity: O(1)

def validateSubsequence(array, sequence):
  arrIndex = 0
  seqIndex = 0
  while arrIndex < len(array) and seqIndex < len(sequence):
    if array[arrIndex] == sequence[seqIndex]:
      seqIndex += 1
    arrIndex += 1
  return seqIndex == len(sequence)

# Solution 2:

# Time Complexity: O(n)
# Space Complexity: O(1)

def validateSubsequence(array, sequence):
  seqIndex = 0
  for value in array:
    if seqIndex == len(sequence):
      break
    if value == sequence[seqIndex]:
      seqIndex += 1
  return seqIndex == len(sequence)

print(validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
print(validateSubsequence([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10, 11, 11, 11, 11]))