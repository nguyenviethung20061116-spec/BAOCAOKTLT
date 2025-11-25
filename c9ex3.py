file_name = input("Enter file name: ")
try:
    with open(file_name, 'r') as file:
        email_counts = {}  
        
        for line in file:
            if line.startswith("From "):
                words = line.split()
                if len(words) >= 2:
                    email = words[1]
                    email_counts[email] = email_counts.get(email, 0) + 1
        
        print(email_counts)

except FileNotFoundError:
    print(f"File '{file_name}' not found.")