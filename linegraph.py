from pylab import plot, arange

x = arange(1, 5, 0.5)
y1 = arange(1, 5, 0.5)
y2 = y1 ** 2

plot(x, y1, 'og-')
plot(x, y2, 'hr:')
