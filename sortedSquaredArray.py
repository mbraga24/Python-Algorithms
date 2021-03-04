def sortedSquaredArray(array): 
  sortedSquared = [0 for _ in array]

  for idx in range(len(array)):
    value = array[idx]
    sortedSquared[idx] = value * value

  sortedSquared.sort()
  return sortedSquared



print(sortedSquaredArray([1, 2, 3, 5, 6, 8, 9]))
print(sortedSquaredArray([-3, -2, 0, 5, 6, 8, 9]))