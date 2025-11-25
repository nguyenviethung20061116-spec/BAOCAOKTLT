import re

ten_file = 'mbox.txt'          
regex = input("Enter a regular expression: ")

dem = 0
with open(ten_file) as f:
    for dong in f:
        dong = dong.rstrip()
        if re.search(regex, dong):
            dem += 1

print(f"{ten_file} had {dem} lines that matched {regex}")