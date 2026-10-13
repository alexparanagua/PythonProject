def fatorial(n):
    if n > 1 :
        return n * fatorial(n-1)
    else:
        return 1

print(fatorial(5))
print(fatorial(10))

#or
def fatorial2(n):
    return n*fatorial(n-1) if n>1 else 1

print(fatorial2(5))
print(fatorial2(10))
