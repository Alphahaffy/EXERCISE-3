#Half pyramid
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
   print('* '*i)

#Inverted Half Pyramid
rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
   print('*'*i)

#Hollow Inverted Half Pyramid
rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    if i == rows or i == 1:
        print('* ' * i)
    else:
        print('* ' + '  ' *(i-2)+'*')

        #Full pyramid
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    print(' ' * (rows -i)+'*'*i)

    #Inverted full pyramid
rows = int(input("Enter the number of rows: "))
for i in range(rows, 0, -1):
    print(' ' * (rows -i)+'*'*i)

    #Hollow full pyramid
rows = int(input("Enter the number of rows: "))
for i in range(1, rows + 1):
    if i == 1 or i == rows:
        print(' ' * (rows - i) + '* ' * i)
    else:
        print(' ' * (rows - i) + '* ' + ' ' * (2 *i-3)+'*')