def compress(input):
    _c=""
    cnt = 0
    result =""
    for c in input :
        if _c != c :
            _c = c
            if cnt : result += str(cnt)
            result += c
            cnt = 1 
        else : cnt+=1
    if cnt : result += str(cnt)
    return result 

print(compress(input('문자를 입력해주세요')))