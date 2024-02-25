"Everything should work on other websites (Python Code Preview)"

n1 = int(input('Enter 1st number: '))
n2 = int(input('Enter 2nd number: ')

         
"Put numbers in place"


calculator = int(input('Enter 1,2,3,4 or 5'))

"1 doesnt work for now" 

"In calculator put 1 (adding) or 2 (calcullating sum of numbers from ... to ..."

if calculator == 1:
   print(n1+n2)
if calculator == 2:
   print(n1-n2)
if calculator == 3:
   print(n1xn2)
if calculator == 4:
   print(n1/n2)
if calculator == 5:
   x = n1
y = n2
sum = 0
for i in range(x, y+1):
   sum = sum + i
print(sum) 
if sum < 0:
   x = n2
y = n1
sum = 0
for i in range(x, y+1):
   sum = sum + i
   print(sum)
