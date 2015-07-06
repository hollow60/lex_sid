__author__ = 'Siddharth'

import csv
import re

fin = open('H_short.csv')
fout = open('x-y-z.csv', 'wb')
writeH = csv.writer(fout, delimiter=',')
readH = csv.reader(fin)

x = input('Enter first three numbers of the record and hit the return key every time:')
y = input()
z = input()

rowBegin = str(x)+str(y)+str(z)


for row in readH:
    if re.match('^'+rowBegin, ''.join(row)):
        writeH.writerow(row)
fin.close()
fout.close()
