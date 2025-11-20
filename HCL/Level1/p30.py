def main():

    x = int(input("enter a 4 dig_num : "))

    h = (x // 100) % 10
    t = (x // 10) % 10

    sum = h +t
    if(sum == 10) and (h > 7 or t > 7):
        print("SUCCESS")
    
    else:
        print("FAILURE")
main()

#     enter a 4 dig_num : 8286
# SUCCESS
    
# enter a 4 dig_num : 4649
# FAILURE