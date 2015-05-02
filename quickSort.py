def main():
  vals = [int(line.strip()) for line in open('QuickSort.txt')]
  count = count_comparisons(vals)
  print(count)

def count_comparisons(l):
  a = 0
  b = len(l) - 1
  return quick_sort(l, a, b)

def quick_sort(l, a, b):
  count = b - a

  # base case
  if a >= b:
    return 0

  # choose the pivot
  #pivot = a
  #pivot = b
  pivot = median(l, a, b)

  pivot = partition(l, pivot, a, b)

  if pivot - 1 > 0:
    count += quick_sort(l, a, pivot - 1)

  if pivot + 1 < len(l) - 1:
    count += quick_sort(l, pivot + 1, b)

  return count


def partition(l, p, a, b):
  l[a], l[p] = l[p], l[a]
  i = a + 1

  for j in range(a + 1, b + 1):
    if l[j] <= l[a]:
      l[i], l[j] = l[j], l[i]
      i += 1

  l[a], l[i - 1] = l[i - 1], l[a]

  return i - 1


def median(l, a, b):
  m = (b - a) // 2 + a
  i = l[a]
  j = l[m]
  k = l[b]

  if i <= j and i >= k or i <= k and i >= j:
    return a
  elif j <= i and j >= k or j <= k and j >= i:
    return m
  else:
    return b

if __name__ == '__main__':
  main()
