import csv
with open('years.csv','rt') as file:
    rows=csv.reader(file)
    for row in rows:
        print(row)
#
# data = ["Month", "1958", "1959", "1960"]
# x = [
# ["JAN", 340, 360, 417],
# ["FEB", 318, 342, 391],
# ["MAR", 362, 406, 419],
# ["APR", 348, 396, 461],
# ["MAY", 363, 420, 472],
# ["JUN", 435, 472, 535],
# ["JUL", 491, 548, 622],
# ["AUG", 505, 559, 606],
# ["SEP", 404, 463, 508],
# ["OCT", 359, 407, 461],
# ["NOV", 310, 362, 390],
# ["DEC", 337, 405, 432],
# ]
# y = "years.csv"
# with open(y, 'w') as work:
#    z = csv.writer(work)
#    z.writerow(data)
#    z.writerow(x)