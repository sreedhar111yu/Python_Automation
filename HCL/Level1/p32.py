def main():
    x = int(input("Enter two dif no x: "))
    y = int(input("Enter two dig no y : "))

    sum = x + y
    diff = x - y

    if(sum < 100):
        print(abs(sum))
    else:
        print(abs(diff))
main()

# Enter two dif no x: 56
# Enter two dig no y : 78
# 22

# Enter two dif no x: 14
# Enter two dig no y : 65
# 79