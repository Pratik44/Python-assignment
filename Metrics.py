def matrix_creation(rows,cols):
    matrix = []
    for i in range(rows):
        temp = [] 
        for j in range(cols): 
            temp.append(int(input("Enter Data [{0}][{1}]: ".format(i,j))))
        matrix.append(temp)
    return matrix

def addition(mat1, mat2):
    add_mat = []
    for i in range(len(mat1)):
        temp = []
        for j in range(len(mat1[0])):
            temp.append(mat1[i][j] + mat2[i][j])
        add_mat.append(temp)
    return add_mat

def multiply(mat1,mat2):
    mult_result = []
    for i in range(len(mat1)):
        temp = []
        for j in range(len(mat2[0])):
            sum = 0
            for k in range(len(mat2)):
                sum+=mat1[i][k]*mat2[k][j]
            temp.append(sum)

        mult_result.append(temp)
    return mult_result

def transpose(mat1):
    tran_mat = []
    for i in range(len(mat1)):
        temp = []
        for j in range(len(mat1[0])):
            temp.append(mat1[j][i])
        tran_mat.append(temp)
    return tran_mat

while True:
    print("Enter the rows and columns details fro Matrix: ")
    rows1 = int(input("Enter Rows: ")) 
    cols1 = int(input("Enter Columns: ")) 
    print("1. Matrix Addition.", "2. Matrix Multiplication.", "3. Matrix Transpose.", "4. Exit",sep='\n')
    choice = int(input("Enter your choice."))
    matrix1 = []
    matrix2 = []

    if choice == 4:
        break
    elif choice == 1:
        print("Please enter rows and columns for 2nd metrix: ")
        row2 = int(input("Enter Row :"))
        col2 = int(input("Enter Column: "))
        if rows1 == row2 and cols1 == col2:
            print("Enter data of first matrix: ")
            matrix1 = matrix_creation(rows1,cols1)
            print("Enter data of second matrix: ")
            matrix2 = matrix_creation(row2,col2)
            add_mat = addition(matrix1,matrix2)
            print(add_mat)
        else:
            print("for addition both metric should be of same size ")

    elif choice == 2:
        print("Please enter rows and columns for 2nd metrix: ")
        row2 = int(input("Enter Row :"))
        col2 = int(input("Enter Column: "))
        if cols1 == row2:
            print("Enter data of first matrix: ")
            matrix1 = matrix_creation(rows1,cols1)
            print("Enter data of second matrix: ")
            matrix2 = matrix_creation(row2,col2)
            result = multiply(matrix1, matrix2)
            print(result)

        else:
            print("for multiplication: column of first matrix should be same as row of second matrix")

    elif choice ==3:
        print("Enter data of matrix: ")
        matrix1 = matrix_creation(rows1,cols1)
        tran_result = transpose(matrix1)
        print(tran_result)
    else:
        print("invalid option")
