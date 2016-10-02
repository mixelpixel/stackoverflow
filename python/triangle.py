# http://stackoverflow.com/questions/39816382/spacing-for-triangle-pattern-in-python
# https://pyformat.info/

def triangle(n): 
    s = ""
    for i in range(0,n):
        s +=  "{}".format((i+1)%10)
        j=s*1
        print( s,'*1=',j)


triangle(9)


print('{:^11}'.format('test'))

def triangle(n): 
    a = 0
    b = 1
    for i in range(1, n+1):
        a = 10*a + i
        print('{:{}d} * {} = {}'.format(a, n, b, a*b))

triangle(22)