rows = int(input("Enter the size of the pattern: "))

row = 0

while row < rows:
    
    star = 0
    
    while star < rows:
        print("*", end="")
        star += 1
        
    print()
    row += 1