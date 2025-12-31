input_long = int(input())
people = int(input())

cake_long = [0] * input_long

many_people = 0
max_long = 0

ex_people = 0
ex_long = 0

for i in range(1, people + 1):
    people_long = 0
    start, end = map(int, input().split())
    if end - start > ex_long:
        ex_people = i
        ex_long = end - start

    for j in range(start - 1, end):
        if cake_long[j] == 0:
            cake_long[j] = i
            people_long += 1

    if max_long < people_long:
        many_people = i
        max_long = people_long

print(f'{ex_people}\n{many_people}')