# http://stackoverflow.com/questions/39816176/how-to-make-an-one-liner-list-with-multiple-variables-in-python/39816291#39816291

ascii_printable = [chr(count) for count in range(32, 127)]
ascii_combinations = []

for x1 in ascii_printable:
    for x2 in ascii_printable:
        for x3 in ascii_printable:
            ascii_combinations.append(x1 + x2 + x3)
            
# print(ascii_combinations)


test = [x1+x2+x3 for x1 in ascii_printable for x2 in ascii_printable for x3 in ascii_printable]

print(test == ascii_combinations)