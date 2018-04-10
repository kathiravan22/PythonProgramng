num = int(input("Enter a number"))
if(num<20):
  factorial = 1
  for i in range(1,num+1):
    factorial = factorial*i
  print(factorial)
else:
  print("error")
