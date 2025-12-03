s = "Sreedhar"
print(s)

print(f"s[0] = {s[0]}" )
print(f"s[-1]={s[-1]}")
print(f"s[-1]={s[-5]}")
print(f"rev : {s[::-1]}")
print(s[1:6])
print(s[:5])
print(s[4:])

p = "python"
for i in p:
    print(i)

ch = "Hello"
ch ='h' + ch[1:]
print(ch)

ch = ch + 'world'
print(ch)
print(len(ch))

n = "   new world  "
print(n.strip())
h = "hello"
w = "world"
c = h+" "+w
print(c)

print(h*3)

n = 55
st = str(n)
print(st, type(st))

f = "Welocme to New world"
nc = f.split()
print(nc)
l = list(s)
print(l)

a = 5
b = 10
b = a
print(a,b)