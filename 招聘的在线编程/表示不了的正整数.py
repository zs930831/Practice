def singleNumber(string):
    num = [str(n) for n in range(10)]
    tempList ,isZero= [],0
    for s in string:
        if s not in tempList:
            tempList.append(s)
    tempList.sort()
    if tempList == num:
        return -1
    for i in num:
        if i not in tempList:
            if i == '0':
                isZero=1
                continue
            return i if isZero==1 else '10'


def leastNum(string):
    dic = dict((str(c),0)for c in range(10))
    for i in string:
        if i in dic.keys():
            dic[i] += 1
    max, result, num = 0, '', 0
    for i in '0123456789':
        if dic[i] > max:
            max = dic[i]
            result, num = i, max
    if result == '0':
        result = '0' * (num + 1)
        result = '1' + result
    else:
        result = result * (num + 1)
    return result, num


# print(singleNumber('01356789'))
if __name__ == '__main__':
    string = input('plz input num: ')
    if singleNumber(string) != -1:
        print(singleNumber(string))
    else:
        result, num = leastNum(string)
        print(result)
