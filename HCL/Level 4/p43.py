def main():

    s = input("enter a string ")
  
    if(s.isdigit() or s.isalpha()):
        print(f"{s} is valid and lenght is {len(s)}")
    else:
        print("not valid")
main()