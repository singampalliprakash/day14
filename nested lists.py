"""Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line."""
if __name__ == '__main__':
    x = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x.append([score, name])
x.sort()
minimum_score = x[0][0]
for a in x:
    if a[0] == minimum_score:
        x.remove(a)
second_minimum_score = x[0][0]
for b in x:
    if b[0] == second_minimum_score:
        print(b[1])