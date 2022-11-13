def sort_dictionary(input):
  arr = list(input.items())
  arr.sort(key=lambda x: x[1][1])
  arr = [(i[0], i[1][0]) for i in arr]
  return arr
