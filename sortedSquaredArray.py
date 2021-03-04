# Solution 1:

# Time Complexity: O(nlogn)
  # Event though we loop over the given array in O(n) when we handle negative numbers the array will not
  # be in ascending order so we will need sort() the array before returning it.
  # This brute force approach in the end is: O(nlogn)
# Space Complexity: O(n)
  # The space complexity is O(n) because we are creating a new array to store the sorted squared values.

'''
def sortedSquaredArray(array): 
  sortedSquared = [0 for _ in array]

  for idx in range(len(array)):
    value = array[idx]
    sortedSquared[idx] = value * value

  sortedSquared.sort()
  return sortedSquared
'''

def sortedSquaredArray(array):
  sortedSquared = [0 for _ in array]
  leftPointer = 0
  rightPointer = len(array) - 1

  for idx in reversed(range(len(array))):
    smallestValue = array[leftPointer]
    highestValue = array[rightPointer]

    if abs(smallestValue) > abs(highestValue):
      sortedSquared


print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
print(sortedSquaredArray([-3, -2, 0, 5, 6, 8, 9]))