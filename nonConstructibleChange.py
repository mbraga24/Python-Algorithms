# Time Complexity: O(nlogn)
  # Because we need to sort the coins array we will have O(nlogn) time. We will still iterate once 
  # over the coins array at O(n) time. The equation would be: O(n log n) + n
  # But since 'n' is less than 'n log n' time we remove 'n' and just describe the time complexity as
  # O(nlogn) time

# Space Complexity: O(1)
  # We are not using any extra space in memory to sort the coins array. We are sorting it in place.

def nonConstructibleChange(coins):
  coins.sort()

  currentChange = 0

  for coinValue in coins:
    if coinValue > currentChange + 1:
      return currentChange + 1

    currentChange += coinValue

  return currentChange + 1



print(nonConstructibleChange([5, 7, 1, 1, 2, 3, 22]))
print(nonConstructibleChange([1, 1]))
print(nonConstructibleChange([109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4]))
