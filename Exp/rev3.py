
def rev(n):

    sign =1
    if n<0:
        sign =-1
        n=-n

    rev =0
    
    while n>0:
        rem =n%10
        rev =rev*10+rem
        n=n//10

    print(rev*sign)

   

rev (int(input()))