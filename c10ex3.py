import string

ten_file = input("Enter file name: ")
if len(ten_file) < 1:
    ten_file = "romeo.txt"  # file mẫu nhỏ để test

dem = {}

with open(ten_file) as f:
    for dong in f:
        dong = dong.translate(str.maketrans('', '', string.punctuation))  
        dong = dong.lower()                                               
        for ky_tu in dong:
            if ky_tu.isalpha():    
                dem[ky_tu] = dem.get(ky_tu, 0) + 1

ds = []
for ky_tu, so_lan in dem.items():
    ds.append((so_lan, ky_tu))

ds.sort(reverse=True)

for so_lan, ky_tu in ds:
    print(ky_tu, so_lan)