import re
s = input()
if re.match(r'.*h.*e.*l.*l.*o.*', s):
    print('YES')
else:
    print('NO')