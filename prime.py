a=int(input('enter a no to check whether it is prime or not'))
for i in range(2,a):
    if a%i==0:
        print('not prime')
        break
else:
    print('prime')
