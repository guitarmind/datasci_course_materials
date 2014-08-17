import MapReduce
import sys

"""
Problem 4
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person relation (A, B)
    # value: symmetric or not
    personA = record[0]
    personB = record[1]
    # mr.emit_intermediate(personA, personB);
    # mr.emit_intermediate(personB, personA);
    mr.emit_intermediate((personA, personB), 1);
    mr.emit_intermediate((personB, personA), -1);

def reducer(key, list_of_values):
    # key: person relation (A, B)
    # value: a list of friends associated with person
    # print key, list_of_values
    if len(list_of_values) > 0:
      total = 0
      for v in list_of_values:
        total += v
      if total == -1:
        if key not in mr.result:
          mr.emit(key)
    if (key[1], key[0]) in mr.intermediate:
      other_total = 0
      for temp in mr.intermediate[(key[1], key[0])]:
        other_total += temp
      if (total != 0 and other_total != 0) and ((total + other_total) == 0):
        if key not in mr.result:
          mr.emit(key)

    mr.result.sort()

    # friends = set()
    # for v in list_of_values:
    #   friends.add(v)
    # for friend in list_of_values:
    #   mr.emit((key, friend))
    #   if friend in mr.result:
    #     if key not in mr.result[friend]:
    #       mr.emit((friend, key))
    #   else:
    #     mr.emit((friend, key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
