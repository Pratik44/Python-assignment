from com.pratik.utility import get_prime,verify_palindrom,pattern 

while True:
    number= int(input('1. To get Prime numbers.\n2. To verify Palindrom.\n3. Pattern Printing.\nEnter your choice: '))
    
    if number == 1:
        n= int(input("Enter the limit to get all Primes within: "))
        if n > 1:
           result = get_prime(n)
           print(result)
           break
        else:
            print("Number should be greater then 1.")
    elif number == 2:
        n= (input("Enter the string to verify palindrom: "))
        pal_result = verify_palindrom(n)
        print(pal_result)
        break
    elif number == 3:
        n = n= int(input("Enter the limit to print sequence: "))
        pattern(n)
        break
    else:
        print('--------------------------\nInvalid entry. Please try again.')
        
        
        