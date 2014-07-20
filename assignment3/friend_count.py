import MapReduce
import sys

"""
Problem 3
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person A
    # value: person B
    personA = record[0]
    personB = record[1]
    mr.emit_intermediate(personA, 1)

def reducer(key, list_of_values):
    # key: person 
    # value: number of friends associated with person
    friend_count = 0
    for v in list_of_values:
      friend_count += v
    mr.emit((key, friend_count))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
