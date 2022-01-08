
try:
    user_input = int(input("Please enter depth of the khayyam-pascal triangle = "))
except:
    print("try again invalid input")
    user_input = int(input("input integer please = "))

def Print_triangle(n:int):

    arr = [[0 for x in range(n)]
              for y in range(n)]

    for row in range (0, n):
        for i in range (0, row + 1):
            if(i == 0 or i == row):
                arr[row][i] = 1
                print(arr[row][i], end =" ")

            else:
                arr[row][i] = (arr[row - 1][i - 1] +
                               arr[row - 1][i])
                print(arr[row][i], end =" ")
        print("\n", end = "")


Print_triangle(user_input)
