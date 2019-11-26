
def get_prime(num):
    prime_list = [1]
    for num in range(2, num + 1):
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                prime_list.append(num)
    return prime_list
    

def verify_palindrom(n):
    new_str= n.replace(" ", "")
    if new_str == (new_str[::-1]):
        return 'It is Palindrom'
    else:
        return 'It is not Palindrom.'

def pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            if j==i:
                print(3*i,end=' ')
            else:
                print("_",end=' ')
        print('\n')
