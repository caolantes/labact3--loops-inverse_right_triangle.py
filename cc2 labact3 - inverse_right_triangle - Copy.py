# Number of rows
rows = 5

# Loop over number of rows 
for i in range(rows+1, 0, -1):
    
    # Nested reverse loop to handle number of columns
    for j in range(0, i-1):
        
        # Display pattern
        print(j+1, end=' ')
    print(" ")