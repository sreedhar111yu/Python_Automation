name = "Sreedhar"

print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

movie = "coolie is not bad"
print(f"movie {movie.title()} but is not lokesh style")

mobile_no = "9363294342"
masked = mobile_no[:2]+"******"+mobile_no[-2:]
print("your moblie No is:",masked)



message = "your booking id:UID7825. keep it safe"
booking_id = message.split(":")[1].split(".")[0]
print("your  id :", booking_id)

offer = "use coupon code Code60 get 60off"
if "Code60" in offer:
    print("offer applied")



word = 'god' 'is' 'good' 


if '0'in word:
    print(len(word.split()))



ch= "Chennai"
print(ch[::-1])

s = "Let's take LeetCode contest"
r =" ".join(word[::-1] for word in s.split() )
print(r)


variable = "Hello, World!"
print(variable + "\n")

variable = "Hello, World!"
print(variable, end="\n")

s = '0000001234'
res = s.lstrip("0")
print(res)