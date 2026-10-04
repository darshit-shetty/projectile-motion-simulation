from numpy import sin, cos, radians
import matplotlib.pyplot as plt
import matplotlib.animation as animation

u = float(input("Enter initial velocity in m/s : "))
theta = radians(float(input("Enter launch angle with the horizontal : ")))
g = -9.81

T_flight = (-1)*(2*u*sin(theta)) / g
Range = (u*cos(theta)) * T_flight
H_max_height = (-1)*((u*sin(theta)) **2) / (2*g)

fig, ax = plt.subplots()

fig.patch.set_facecolor("#0EAEE6")
ax.set_facecolor("#89DAFF")

ax.set_xlim(-3, Range + 3)
ax.set_ylim(0, H_max_height + 3)

ax.set_aspect("equal")

ball, = ax.plot([], [], 'ro')

dt = 0.02
frames = int(T_flight / dt) + 1

def update(frame):
    time = frame * dt

    x = (u*cos(theta)) * time
    y = ((u*sin(theta)) * time) + (0.5 * g * time * time)

    ball.set_data([x], [y])

    return ball

ani = animation.FuncAnimation(fig, update, frames = frames, interval = dt * 1000, repeat = False)
# ani.save("preview.gif", writer="pillow", fps=50)

plt.show()