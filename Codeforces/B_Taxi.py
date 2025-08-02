n = int(input())

students = [int(x) for x in input().split()]

c1, c2, c3, c4 = students.count(1), students.count(2), students.count(3), students.count(4)

cars = c4

cars += c3

c1 = max(0, c1 - c3)

cars += c2 //2

c2 = c2 % 2

if c2 == 1:
    cars += 1
    