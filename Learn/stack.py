#stack

stack = [1,2,3,4]
print(stack[-1])  # accessing last element

stack.append(5) # insertion
print(stack)
print(stack[-1]) #accessing

stack.pop() # deletion
print(stack)
print(stack[-1])

from collections import deque

stack = deque([9,8,7,6])
print(stack)

print(stack[-1])
stack.pop()
print(stack)