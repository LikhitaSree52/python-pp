M1 = [[8, 14, -6], 
      [12,7,4], 
      [-11,3,21]]
M2 = [[3, 16, -6],
           [9,7,-4], 
           [-1,3,13]]
M3  = [[0,0,0],
       [0,0,0],
       [0,0,0]]
print("Method to print the sum using for loop")

matrix_length = len(M1)
for i in range(len(M1)):
    for k in range(len(M2)):
        M3[i][k] = M1[i][k] + M2[i][k]
print("The sum of Matrix M1 and M2 = ", M3)

