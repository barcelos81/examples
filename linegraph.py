from pylab import plot, arange

x1 = arange(1, 5, 0.5)
y1 = arange(1, 5, 0.5)
y2 = y1**2

plot(x1, y1, 'og-')
plot(x1, y2, 'hr:')
