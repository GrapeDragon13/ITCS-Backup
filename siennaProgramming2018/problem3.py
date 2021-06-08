'''
works if second number is higher than first, cyclical iteration

1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
                      ->2...........1->                       (to start)

convert to lowest unit and work from there (minutes)
'''

h1, m1, h2, m2 = int(input()), int(input()), int(input()), int(input())

t1 = h1 * 60 + m1
t2 = h2 * 60 + m2
diff = t2 - t1 + 1440
h = (int(diff / 60)) % 24
m = diff % 60

print(h, m)

'''
def difference(h1, m1, h2, m2):
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2

    diff = t2 - t1 + 1440

    h = (int(diff / 60)) % 24
    m = diff % 60

    print(h, ':', m)

def main():
    difference(1, 00, 1, 00)

main()
'''