def calculate_avg(values):
    return sum(values) / len(values)
digits = [72,55,101,90]
calculate_avg(digits)

stations = [
['A1', 62],
['B5', 97],
['C3', 155]
]

for x in stations:
   print(x[0], "→", x[1])
  
def report_status(stations, threshold):
   for [id, pm25] in stations:
      if pm25 < threshold:
         print(id, "→", pm25, "ug/m^3 : Safe")
      else:
         print("Danger!")
report_status(stations, 100)
