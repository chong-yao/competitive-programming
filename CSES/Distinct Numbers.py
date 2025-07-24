n = int(input())
integers = sorted(list(input().split()))

def count_distinct(arr):
    distinct = set(arr)
    return len(distinct)

print(count_distinct(integers))