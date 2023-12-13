import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def RK4_step(y, t, f, dt):         #Для числовой части я использовал метод Рунге - Кутты
    k1 = dt * f(y, t)
    k2 = dt * f(y + 0.5 * k1, t + 0.5 * dt)
    k3 = dt * f(y + 0.5 * k2, t + 0.5 * dt)
    k4 = dt * f(y + k3, t + dt)

    return (t + dt, y + (k1 + 2. * (k2 + k3) + k4) / 6.)

G = 6.674e-11
m_s = 1.989e30
m_e = 5.972e24
m_m = 7.346e22

def derivative_fn(y, t):                 # Векторы, необходимые для 2 Закона Ньютона
    d1 = y[1] - y[0]
    vec01 = d1 / np.linalg.norm(d1) ** 3
    d2 = y[2] - y[0]
    vec02 = d2 / np.linalg.norm(d2) ** 3
    der = np.array([
        y[3],
        y[4],
        y[5],
        - G * m_s * y[0] / np.linalg.norm(y[0]) ** 3 + G * m_m * vec01,
        - G * m_s * y[1] / np.linalg.norm(y[1]) ** 3 - G * m_e * vec01,
        - G * m_s * y[2] / np.linalg.norm(y[2]) ** 3 - G * m_e * vec02])
    return der

def ind(y0, derivative_fn, step_fn, a, b, n):
    dt = (b - a) / (n - 1)
    t = a
    y = np.array(y0)

    res = [y]
    for _ in range(1, n):
        t, y = step_fn(y, t, derivative_fn, dt)
        res.append(y)
    return (np.linspace(a, b, n), np.array(res))

r_e0 = 1.519e11
v_e0 = np.sqrt(G * m_s / r_e0)
r_m0 = 1.521e11
v_m0 = np.sqrt(G * m_e / abs(r_m0 - r_e0))
r_a0 = 1e11
v_a0 = 31293  # m/s
y0 = np.array([[r_e0, 0.], [r_m0, 0.], [r_a0, 0.], [0., v_e0], [0., v_e0 + v_m0], [0., v_e0 + v_a0]])

n = 10000
ts, ys = ind(y0, derivative_fn, RK4_step, 0., 5.154e7, n)

r_earth = ys[:, 0, :]

fig, ax = plt.subplots()
ax.set_xlim([-0.3e12, 0.3e12])
ax.set_ylim([-0.3e12, 0.3e12])

sun, = ax.plot(0., 0., 'oy', ms=30)
earth, = ax.plot(r_earth[0, 0], r_earth[0, 1], 'og', ms=10)
moon, = ax.plot(0, 0, 'ob', ms=3)

num_frames = 100
frame_duration = n / num_frames

r = 0.4
def circle(phi, x, y):
    return np.array([r*np.cos(phi/2)* 100000000000, r*np.sin(phi/2)* 100000000000]) + np.array((x, y))


def animation_frame(frame):
    index = int(frame_duration * frame)
    earth.set_data(r_earth[index, 0], r_earth[index, 1])
    x,y = circle(frame, r_earth[index, 0], r_earth[index, 1]) 
    moon.set_data([x],[y])
    return  moon,

plt.grid() 
animation = FuncAnimation(fig, func=animation_frame, frames=range(num_frames), interval=1)

animation.save('vrty.gif')