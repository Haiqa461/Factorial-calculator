print("This is factorial calculator")
n=int(input("Enter any number: "))

def fac(n):
   answer=1
   if n>1:
      for i in range(1,n+1):
         answer=answer*i   
      return answer
   else:
      print('Factorial Is 1')
   
   
print(fac(n))
