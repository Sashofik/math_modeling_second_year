import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
sun, = plt.plot([], [], 'o', color='orange')
edge = 2.5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)



class Planet(object):
    def __init__(self, R, angle_vel, sp):
        self.R = R
        self.angle_vel = angle_vel
        self.sp = sp

    def planet_move(self, t, n):
        alpha = self.angle_vel * (np.pi/180) * t + self.sp
        x = self.R*np.cos(alpha)
        y = self.R*np.sin(alpha)
        if n % 2 == 0:
            return -x, -y
        else:
            return x, y
cv = 0
for c in range(8):
    for i in range(49):
        exec("plane{}, = plt.plot([], [], 'o', color='green')".format(i+cv))
    cv += 49

def sun_animation():
    x = 0
    y = 0
    return x, y

def animate(i):
    plt.grid(True)
    cv = 0
    o = 1
    n = 1
    sun.set_data(sun_animation())
    for c in range(8):
        for k in range(49):
            if n % 2 == 0:
                globals()['planet' + str(k+cv)] = Planet(R=0.9+o-1, angle_vel = 1, sp = ((180/(52)) * k))
            else:
                globals()['planet' + str(k+cv)] = Planet(R=0.9+o-1, angle_vel = -1, sp = ((180/(52)) * k))
        for j in range(49):
            exec("plane{}.set_data(planet{}.planet_move(t = i, n = n))".format(j+cv,j+cv,j+cv))
        cv += 49
        n += 1
        o *= 1.09

ani = animation.FuncAnimation(fig, animate, frames=45, interval=10)
ani.save('project.gif')