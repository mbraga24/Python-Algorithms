# Solution 1:

# Time Complexity: O(nlogn)
  # Event though we loop over the given array in O(n) when we handle negative numbers the array will not
  # be in ascending order so we will need sort() the array before returning it.
  # This brute force approach in the end is: O(nlogn)
# Space Complexity: O(n)
  # The space complexity is O(n) because we are creating a new array to store the sorted squared values.

'''
def sortedSquaredArray(array): 
  sortedSquares = [0 for _ in array]

  for idx in range(len(array)):
    value = array[idx]
    sortedSquares[idx] = value * value

  sortedSquares.sort()
  return sortedSquares
'''

# Time Complexity: O(n)
#   We are performing a linear iteration in the given array from the largest value to the smallest value.
#   We iterate linearly while also sorting and assigning the squared values from the largest to the 
#   smallest value in the new sortedSquares array.

# Space Complexity: O(n)
  # We're still creating a new array to store the squared values.

def sortedSquaredArray(array):
  sortedSquares = [0 for _ in array]
  leftPointer = 0
  rightPointer = len(array) - 1

  for idx in reversed(range(len(array))):
    smallerValue = array[leftPointer]
    largerValue = array[rightPointer]

    if abs(smallerValue) > abs(largerValue):
      sortedSquares[idx] = smallerValue * smallerValue
      leftPointer += 1
    else:
      sortedSquares[idx] = largerValue * largerValue
      rightPointer -= 1

  return sortedSquares

print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
print(sortedSquaredArray([-3, -2, 0, 5, 6, 8, 9]))