
def main():
  vals = [int(line.strip()) for line in open('IntegerArray.txt')]
  count, _ = count_inversions(vals)
  print(count)

def count_inversions(lst):
  length = len(lst)
  if length <= 1:
    return 0, lst

  middle = length // 2

  count_l, lst_l = count_inversions(lst[:middle])
  count_r, lst_r = count_inversions(lst[middle:])
  count_s, lst = count_split_inversions(lst_l, lst_r)
  return count_l + count_r + count_s, lst



def count_split_inversions(lst_l, lst_r):
  lst = []
  i = 0
  j = 0
  len_l = len(lst_l)
  len_r = len(lst_r)
  inv_count = 0

  while i < len_l and j < len_r:
    if lst_l[i] <= lst_r[j]:
      lst.append(lst_l[i])
      i += 1
    else:
      lst.append(lst_r[j])
      j += 1
      inv_count += len_l - i

  if i < len_l:
    lst.extend(lst_l[i:])
  elif j < len_r:
    lst.extend(lst_r[j:])

  return inv_count, lst



if __name__ == '__main__':
  main()