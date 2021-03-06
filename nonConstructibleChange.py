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
