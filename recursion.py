def fibonacci(n, sec_last, last):
    if n-1 == 0:
        return sec_last
    
    else:
        new_last = second_last + last
        second_last = last
        return fibonacci(n-1,second_last,new_last)

def gcd(a,b):
    if a == 0:
        return b
    
    return gcd(b%a, a)


def compareTo(a,b):
    if a < b:
        return -1
    elif a > b:
        return -1
    else:
        return 0

if __name__ == "__main__":
    print(fibonacci(10,0,1))
    a=int(input())
    b=int(input())
    print(gcd(a,b))
    print(compareTo(a,b))