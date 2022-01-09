def check(s) :
    result = []
    for i in s :
        if i not in result :
            result.append(i)
        else : return False
    return len(result) == 10

print(check('0123456789'))
print(check('01234'))
print(check('01234567890'))
