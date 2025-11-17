City1 = {"Chennai","Madurai","trichy"}
city2=["Coimbathur","Salam","Namakal","Chennai","Madurai"]

City2=set(city2)

print(City1.union(City2))

print(City1.intersection(City2))

print(City1.difference(City2))

City1.add("Kanchipuram")
print(City1)