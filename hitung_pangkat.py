input_number = int(input("Insert Any Number: "))

for i in range(1, input_number + 1):
    hasil = i ** 3

    # untuk versi python 3.6 ke atas
    print(f"Current number is : {i} and the cube is {hasil}")

    # untuk versi python di bawah 3.6
    # output = "Current number is : {} and the cube is {}".format(i, hasil)
    # print(output)