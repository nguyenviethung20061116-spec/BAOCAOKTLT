ten_file = input("Enter a file name: ")

with open(ten_file) as f:
    dem = {}  
    
    for dong in f:
        if dong.startswith("From "):    
            tach = dong.split()         
            email = tach[1]             
            dem[email] = dem.get(email, 0) + 1

nguoi_nhieu_nhat = None
so_luong_max = 0

for email, so_luong in dem.items():
    if so_luong > so_luong_max:
        so_luong_max = so_luong
        nguoi_nhieu_nhat = email

print(nguoi_nhieu_nhat, so_luong_max)