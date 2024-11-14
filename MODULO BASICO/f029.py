"""
While

"""


x = 0

while  x < 10:

    print(x)
    x = x + 1

print('Acabou')

#teste com continue , teste os codes separadamente

while  x < 10:
    if x == 3:
        x = x + 1
        continue

    print(x)
    x = x + 1

    #outro code
 
y = 0
m = 0

while x < 10:
    y = 0
     
    while y < 5:
       print(f'{m},{y}')
       y += 1


    x += 1

print('Acabou')
