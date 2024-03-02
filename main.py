import math

def jump_search(a, n, key):
  i = 0
  m = int(math.sqrt(n))
  k = m
  while(a[m] <= key and m < n):
    i = m
    m += k
    if(m > n - 1):
      return -1
  for j in range(m):
    if(a[j] == key):
      return j
  return -1

collection = [3,12,22,29,34,36,39,90,100,120]
n = len(collection)
target = 39
pos = jump_search(collection, n, target)

if(pos >= 0):
  print("The value is found at index {0}".format(pos))









