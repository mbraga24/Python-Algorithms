def twoNumberSum(array, targetNum):
  for i in range(len(array) - 1):
    firstNum = array[i]
    for j in range(i + 1, len(array)):
      secondNum = array[j]
      if firstNum + secondNum == targetNum:
        return [firstNum, secondNum]
  return []

def twoNumberSum(array, targetNum):
  nums = {}
  for num in array:
    potentialMatch = targetNum - num
    if potentialMatch in nums:
      return [potentialMatch, num]
    else:
      nums[num] = True
  return []

def twoNumberSum(array, targetNum):
  array.sort()
  left = 0
  right = len(array)- 1
  while left < right:
    currentSum = array[left] + array[right]
    if currentSum == targetNum:
      return [array[left], array[right]]
    elif currentSum < targetNum:
      left += 1
    elif currentSum > targetNum:
      right -= 1
  return []


print(twoNumberSum([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(twoNumberSum([1, 2, 3, 4, 5, 6, 7, 8, 9], 17))