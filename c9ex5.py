ten_file = input("Enter a file name: ")

domain_count = {}  

with open(ten_file) as f:
    for dong in f:
        if dong.startswith("From "):
            tach = dong.split()
            email = tach[1]              
            domain = email.split("@")[1]  
            domain_count[domain] = domain_count.get(domain, 0) + 1

print(domain_count)