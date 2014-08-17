import MapReduce
import sys

"""
Problem 2
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: order ID
    # value: attributes
    origin_table = record[0]
    order_id = record[1]
    attributes = [origin_table, record[1:]]
    mr.emit_intermediate(order_id, attributes)

def reducer(key, list_of_values):
    # key: order ID
    # value: list of attribute list
    order_data = []
    for v in list_of_values:
      if v[0] == "order":
        order_data.append(v[0])
        for temp in v[1][0:]:
          order_data.append(temp)

    for v in list_of_values:
      if v[0] == "line_item":
        output = []
        for temp in order_data:
          output.append(temp)
        output.append(v[0])
        for temp in v[1][0:]:
          output.append(temp)
        mr.emit(output)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
