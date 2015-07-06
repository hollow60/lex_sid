__author__ = 'Siddharth'

import csv
import re

fin = open('H_short.csv')
fout = open('H_new.csv','wb')
writeH = csv.writer(fout, delimiter=',')
readH = csv.reader(fin)
for row in readH:
    if re.match('^111', ''.join(row)):
        writeH.writerow(row)
fin.close()
fout.close()