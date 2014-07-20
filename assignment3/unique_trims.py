import MapReduce
import sys

"""
Problem 5
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: last 10 characters
    # value: nucleotides
    sequence_id = record[0]
    nucleotides = record[1]
    mr.emit_intermediate(nucleotides[-10:], nucleotides)

def reducer(key, list_of_values):
    # key: last 10 characters
    # value: list of nucleotides
    # print key
    for v in list_of_values:
      lastTenChars = v[-10:]
      if key == lastTenChars:
        output = v[:-10]
        if output not in mr.result:
          mr.emit(output)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
