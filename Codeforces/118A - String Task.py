vowels = 'aoyeui'
input = input().lower()
ans = [f".{i}" for i in input if i not in vowels]
print(''.join(ans))