# øvelser del 1 veriable udtryk
# opg 1
x = 17
y = 12.0
z = "4"

result1 = 2 * x  # 34 | int
result2 = x / 2.0  # 8.5 | float
result3 = x + y  # 29.0 | float
result4 = 1 + 2 * 3  # 7 | int
result5 = z * 4  # 4444 | sting


def print_result(res):
    print(res)
    print("int ", type(res) == int)
    print("float ", type(res) == float)
    print("str (string) ", type(res) == str)


# print_result(result5)


# opg 2
def opg_2():
    x = 1
    y = 2  # + 3
    # x = 5
    z = x + y
    print(z)

# output = 3


# opg 3
def opg_3():
    usr_intput1 = int(input("skriv et tal: "))
    usr_intput2 = int(input("skriv et andet tal: "))

    print("summmen : ", usr_intput1 + usr_intput2)


# opg 4
def opg_4():
    usr_intput1 = float(input("skriv et tal: "))
    usr_intput2 = float(input("skriv et andet tal: "))

    print("summmen : ", usr_intput1 + usr_intput2)


# opg 5
def opg_5():
    tal = [65, 81, 43, 63, 27, 69, 43, 68, 88, 76, 30, 99, 74, 11, 89, 38, 73, 9]

    print("sunmmen er : ", sum(tal))
    print("størst er : ", max(tal))

    biggetst_number = 0

    for index in tal:
        if index > biggetst_number:
            biggetst_number = index

    print(tal.index(biggetst_number))

    for index in tal:
        if 40 < index < 70:  # if index < 70 and index > 40:
            print(index)


# opg 6
def opg_6():
    total_cont = int(input("how manyt numbers do like add together : "))

    values = []
    for index in range(total_cont):
        values.append(int(input('Please enter a value : ')))

    print(sum(values))


# palindrome
n = input("Enter the word and see if it is palindrome: ")

if n == n[::-1]:
    print("This word is palindrome")
else:
    print("This word is not palindrome")
