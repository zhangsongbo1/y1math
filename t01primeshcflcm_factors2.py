# Generate a list containing factors of num.
#indicate variable "num"
num = 34
#extract number 1 to "num" using "i" and "for" circle
for i in range(1, num+1):  
  if num % i == 0:
    print(i, end=' ')
