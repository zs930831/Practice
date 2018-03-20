'''
    动态规划——字符串的编辑距离
    s1 = "abc", s2 = "def"
    计算公式：
             | 0                                           i = 0, j = 0
             | j                                           i = 0, j > 0
    d[i,j] = | i                                           i > 0, j = 0
             | min(d[i,j-1]+1, d[i-1,j]+1, d[i-1,j-1])    s1(i) = s2(j)
             | min(d[i,j-1]+1, d[i-1,j]+1, d[i-1,j-1]+1)  s1(i) ≠ s2(j)
    定义二维数组[4][4]：
        d e f            d e f
    |x|x|x|x|        |0|1|2|3|
    a |x|x|x|x|  =>  a |1|1|2|3|  => 编辑距离d = [4][4] = 3
    b |x|x|x|x|      b |2|2|2|3|
    c |x|x|x|x|      c |3|3|3|3|
'''


def levenshtein(s1, s2):
    i = 0  # s1字符串中的字符下标
    j = 0  # s2字符串中的字符下标
    s1i = ""  # s1字符串第i个字符
    s2j = ""  # s2字符串第j个字符
    m = len(s1)  # s1字符串长度
    n = len(s2)  # s2字符串长度
    if m == 0:
        return n  # s1字符串长度为0，此时的编辑距离就是s2字符串长度
    if n == 0:
        return m  # s2字符串长度为0，此时的编辑距离就是s1字符串长度
    solutionMatrix = [[0 for col in range(n + 1)] for row in range(m + 1)]  # 长为m+1，宽为n+1的矩阵
    '''
             d e f
          |x|x|x|x|
        a |x|x|x|x|
        b |x|x|x|x|
        c |x|x|x|x|
    '''
    for i in range(m + 1):
        solutionMatrix[i][0] = i
    '''
             d e f
          |0|1|2|3|
        a |x|x|x|x|
        b |x|x|x|x|
        c |x|x|x|x|

    '''
    for j in range(n + 1):
        solutionMatrix[0][j] = j
    '''
        上面两个操作后，求解矩阵变为
             d e f
          |0|1|2|3|
        a |1|x|x|x|
        b |2|x|x|x|
        c |3|x|x|x|
        接下来就是填充剩余表格
    '''
    for x in range(1, m + 1):
        s1i = s1[x - 1]
        for y in range(1, n + 1):
            s2j = s2[y - 1]
            flag = 0 if s1i == s2j  else 1
            solutionMatrix[x][y] = min(solutionMatrix[x][y - 1] + 1, solutionMatrix[x - 1][y] + 1,
                                       solutionMatrix[x - 1][y - 1] + flag)

    return solutionMatrix[m][n]


def min(insert, delete, edit):
    tmp = insert if insert < delete else delete
    return tmp if tmp < edit else edit


s1 = "a"
s2 = "def"
distance = levenshtein(s1, s2)
print(distance)