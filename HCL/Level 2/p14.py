def reverse(x):
    rev = 0
    dig = 1
    temp = x

    while temp > 0:
        rem = temp % 10
        rev = rem + rev * 10
        temp = temp // 10
        dig = dig * 10

    dig //= 10     
    return rev, dig

def main():
    x = int(input("enter num : "))
    rev, dig = reverse(x)
    last_dig = rev % 10
    first_dig = rev // dig

    new_rev,new_dig = reverse(rev)

    n_last = new_rev // 10
    n_last = n_last * 10 + last_dig

    n_first = n_last % new_dig
    res = first_dig*new_dig + n_first

    print(res)
    #---------------------------------------------
    s = str(x)
    str_res = s[-1] + s[1:-1] +s[0]
    print(f"str_res : {str_res}")
main()

# enter num : 1234
# 4231
# str_res : 4231

