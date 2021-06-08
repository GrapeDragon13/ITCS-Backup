import matplotlib.pyplot as plt
#from pylab import randn
#X = randn(200)
#Y = randn(200)

def randomRange(seed, minimum, maximum):
    return seed % (maximum - minimum) + minimum


def random(minimum = 0, maximum = 100):
    random.seed = str(abs(hash(random.seed)))

    return randomRange(int(random.seed), minimum, maximum)


random.seed = 'seed'

X = []
Y = []

for i in range(100):
    X.append(i / 100)
    Y.append(random() / 100)

plt.scatter(X, Y, color = 'r')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()