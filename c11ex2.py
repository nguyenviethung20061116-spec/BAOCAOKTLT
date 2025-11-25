import re

ten_file = input("Enter file: ")
if len(ten_file) < 1:
    ten_file = "mbox-short.txt"

tong = 0
dem = 0

with open(ten_file) as f:
    for dong in f:
        dong = dong.rstrip()
        
        x = re.findall('^New Revision: ([0-9]+)', dong)
        if len(x) == 1:
            so = int(x[0])
            tong += so
            dem += 1

if dem > 0:
    trung_binh = tong / dem
    print(trung_binh)