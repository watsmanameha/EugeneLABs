import numpy as np
from scipy. integrate import odeint
import matplotlib.pyplot as plt


r = 1.5e-2
R = 4e-2
V = 8.5e6
L = 12e-2
m = 9.1e-31
q = 1.6e-19

time = L/V
U = -2*m*r*np.log(R/r)*(3*r-R)/(q*time*time)

P = U*q/(m*np.log(R/r))

 # create function

def f(y, t):
	y1, y2 = y
	return [y2, P*1/y1]

t = np.linspace( 0, time, 100) # vector of time
y0 = [(R+r)/2,0] # start value
w = odeint(f, y0, t) # solve eq.
y1 = w[:,0]
y2 = w[:,1]



fig1 = plt.figure(figsize=[10, 10])
x = np.linspace(0,L,100)

plt.plot(x, y1, 'r')
plt.ylabel("y,м")
plt.xlabel("x,м")
plt.grid(True)

fig2 = plt.figure(figsize=[10, 10])
plt.plot(t, abs(y2), 'g')
plt.ylabel("|Vy|,м/с")
plt.xlabel("t, сек")
plt.grid(True)

fig3 = plt.figure(figsize=[10, 10])
a = np.gradient(y2)
plt.plot(t, abs(a), 'g')
plt.ylabel("|ay|, $м/с^2$")
plt.xlabel("t,сек")
plt.grid(True)

fig4 = plt.figure(figsize=[10, 10])
plt.plot(t, y1, 'b')
plt.ylabel("y,м")
plt.xlabel("t,сек")
plt.grid(True)



plt.subplots_adjust(wspace=1, hspace=0.5)
plt.show() # display'

print('Конечная скорость по X:',V)
print('Конечная скорость по Y:',y2[len(y2)-1])
print('Модуль скорости в конечный момент времени:',np.sqrt(V**2+y2[len(y2)-1]*y2[len(y2)-1]),'м/с')
