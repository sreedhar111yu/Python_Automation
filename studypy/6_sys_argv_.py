import sys

first_name = sys.argv[1]
last_name = sys.argv[2]

email = first_name.lower()+last_name + "@hecltech.com"

print("Generated email: ",email)