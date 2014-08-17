import MapReduce
import sys

"""
Problem 6
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

L = 5
M = 5
N = 5

def mapper(record):
    # key: (i, k)
    # value: (matrix i, j, value) tuple
    matrix = record[0]

    if matrix == "a":
      i = int(record[1])
      j = int(record[2])
      a_ij = int(record[3])

      for k in xrange(0, N):
        mr.emit_intermediate((i, k), (matrix, j, a_ij))
    elif matrix == "b":
      j = int(record[1])
      k = int(record[2])
      b_jk = int(record[3])
      
      for i in xrange(0, L):
        mr.emit_intermediate((i, k), (matrix, j, b_jk))

def reducer(key, list_of_values):
    # key: (i, k)
    # value: list of (matrix i, j, value) tuple
    # print key, list_of_values

    hash_a = {}
    hash_b = {}
    for v in list_of_values:
      if v[0] == "a":
        hash_a[v[1]] = v[2]
      elif v[0] == "b":
        hash_b[v[1]] = v[2]

    # print hash_a
    # print hash_b

    result = 0
    for j in xrange(0, M):
      if j in hash_a and j in hash_b:
        result = result + (hash_a[j] * hash_b[j])
    
    mr.emit((key[0], key[1], result))
    mr.result.sort()

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
