# assignment

old = "><"
new = "<>"
people= "><>><><>><>><<"


while True:
    print(people)
    people_new = people.replace(old, new)
    if people_new == people:
        break
    people = people_new


#------------------------------------------------------------------
# COUNT_NUMBER
i = 1
n = 10

s = 1
while True:
    if i >= n:
        break
    s = s * i
    i = i + 1



print(s)
#----------------------------------------------------
# for_else
lst = [199, 254, 343]

for i in lst:
    del lst
    lst = []
    print(i)
#----------------------------------------------------
# while_else
i = 0

while i < 5:
    print(i)
    i += 1
    if i == 7:
        break
else:
    print("I'm here dude!")
#----------------------------------------------------
# functions   assignment
def fact(n):
    out = 1
    for i in range(1, n + 1):
        out = out * i

    return out


def combination(m, n):
    res = fact(m) / (fact(m-n) * fact(n))
    return int(res)


def pascal_row(n):
    out = []
    for i in range(n+1):
        temp = combination(n, i)
        out.append(temp)

    return out


def pascal(rows):
    out = []
    for i in range(1, rows+1):
        temp = pascal_row(i)
        out.append(temp)

    return out

res= pascal(6)
print(res)
#------------------------------------------------
# def_keyword
# f = lambda x : x ** 2
def f(x):
    res = x ** 2
    res = res + x ** 3
    return res


y = f(10)
print(y)
#------------------------------------------------------------
# define_functions

f = lambda x: x ** 2
char_counter = lambda text: len(text)
word_counter = lambda text: len(text.split())
y = f(10)
print(y)


poem = "april is the cruelest month"
print(word_counter(poem), char_counter(poem))
# end