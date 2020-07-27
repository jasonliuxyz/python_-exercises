# 回数：从左向右和从右向左读都是一样的数，例如 12321, 999，请利用filter函数

def equal(a, b):
    return a==b

def is_palindrome(n):
    s = str(n)
    for i in range(len(s)-1):
        if equal(s[i], s[len(s)-i-1]):
            continue
        else:
            return False
    return True

output = filter(is_palindrome, range(1, 100))
print(list(output))
