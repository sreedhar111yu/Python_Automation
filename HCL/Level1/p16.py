def rev():

    x = int(input("enter four dig no : "))
    d1 = x // 1000
    d2 = (x // 100) % 10
    d3 = (x // 10) % 10
    d4 = x % 10

    y = d2*1000 + d1*100 + d3*10 +d4
    print(f"res : {y}" )
    print(f"d1 : {d1} , d2 : {d2} , d3 : {d3}, d4 : {d4}")

rev()

# enter four dig no : 95613
# res : 5961