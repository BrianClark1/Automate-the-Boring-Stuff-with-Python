print('Enter a number to "Collatzify"')

def collatz(number):
        if number % 2 == 0:
            print(number // 2)
            return number // 2
        elif number % 2 == 1:
            print( 3 * number + 1)
            return 3 * number + 1 
        
value = input()

try:
    number = int(value)
    while number > 1:
        number = collatz(number)
        print(number)
    if number == 1:
        print(number)
        
except:
    value = str
    print('Enter an integer')
             


            
