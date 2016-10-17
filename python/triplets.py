# http://stackoverflow.com/questions/40078532/python-why-are-some-test-cases-failing

a0,a1,a2 = input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

m = 0
n = 0
lst1 = a0,a1,a2
lst2 = b0,b1,b2

for x, y in zip(lst1, lst2):
    print(list(zip(lst1, lst2)))
    if x > y:
        m += 1
        print("x > y", x, y, m)

    if x < y:
        n += 1
        print("x < y", x, y, n)

    # else:
        # pass
        
    print('poop')
    print()

print(m, n)