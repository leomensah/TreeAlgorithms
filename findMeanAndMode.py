def stats_finder(array):
  # Write your code here
  modeValue = findMode(array)
  meanValue = findMean(array)
  result = [meanValue, modeValue]
  return result
  
def findMode(lst):
  # Use a dictionary data structure
  # Use elements as keys and their counts as values
  # Find the number with a largest counter
  new_dict = {}
  for element in lst:
    if element in new_dict:
      new_dict[element] += 1
    else:
      new_dict[element] = 1
  modeValue = None
  for key, value in new_dict.items():
    if modeValue is None:
      modeValue = (key, value)
    else:
      if new_dict[key] > modeValue[1]:
        modeValue = (key, value)
      elif new_dict[key] == modeValue[1]:
        if key < modeValue[0]:
          modeValue = (key, value)
  return modeValue[0]

def findMean(lst):
  nLen = len(lst)
  nSum = sum(lst)
  return nSum / nLen
        
print(findMean([500, 400, 400, 375, 300, 350, 325, 300]))
print(findMode([500, 400, 400, 375, 300, 350, 325, 300]))
print(stats_finder([500, 400, 400, 375, 300, 350, 325, 300]))