# If a and b are integers such that a * b = 17, find the value of a + b.

num=17

for a in range(1, num+1):
  if num % a == 0:
    print(a, end'')
for b in range(a+1, num+1):
  if num % b == 0:
    print(b, end'')
    answer=a+b
    print(answer)
    
    
