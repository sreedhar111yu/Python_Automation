def sum_of_dig(n):
    return (n // 10) + (n % 10)

def main():
    for i in range(10, 100):
        if(i % 2 != 0):
            if(sum_of_dig(i) == 7):
                print(i, end=" ")

main()