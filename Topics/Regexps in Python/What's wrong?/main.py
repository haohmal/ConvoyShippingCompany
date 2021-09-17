import re

w1 = input()
w2 = input()
result = re.match(w1, w2)
if result is not None:
    print(str(len(w1) * 2))
else:
    print('no matching')