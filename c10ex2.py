ten_file = input("Enter a file name: ")
gio_dem = {}

with open(ten_file) as f:
    for dong in f:
        if dong.startswith("From "):
            tach = dong.split()
            if len(tach) < 6: continue
            thoi_gian = tach[5]           
            gio = thoi_gian.split(":")[0] 
            gio_dem[gio] = gio_dem.get(gio, 0) + 1

for gio, so_luong in sorted(gio_dem.items()):
    print(gio, so_luong)