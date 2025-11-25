ten_file = input("Enter a file name: ")
dem = {}

with open(ten_file) as f:
    for dong in f:
        if dong.startswith("From "):
            email = dong.split()[1]
            dem[email] = dem.get(email, 0) + 1

danh_sach = []
for email, so_luong in dem.items():
    danh_sach.append((so_luong, email))

danh_sach.sort(reverse=True)

print(danh_sach[0][1], danh_sach[0][0])