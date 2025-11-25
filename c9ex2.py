file_name = input("Enter a file name: ")
try:
    with open(file_name, 'r') as file:
        day_counts = {}  
        
        for line in file:
            if line.startswith("From "):
                words = line.split()
                if len(words) >= 3:
                    day = words[2]
                    day_counts[day] = day_counts.get(day, 0) + 1
        
        print(day_counts)

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
