import numpy as np
import matplotlib.pyplot  as plt

fig = plt.figure(figsize=(10, 10))
ax1 = fig.add_subplot(1,1,1)
ax2 = fig.add_subplot(2,1,1)
ax3 = fig.add_subplot(3,1,1)
fig.subplots_adjust(hspace=.45)

m = float(input("Forneça a massa do bloco: "))
k = float(input("Forneça a constante elástica da mola: "))
phi = float(input("Forneça a fase em pi: "))
A = float(input("Forneça a amplitude: "))

T = float(2*np.pi*np.sqrt(m/k))
w = float(np.sqrt(k/m))

def position(t):
    global w,phi,A
    return A*np.cos((w*t)+(phi*np.pi))

def velocity(t):
    global w,phi,A
    return -A*w*np.sin((w*t)+(phi*np.pi))

def acceleration(t):
    global w,phi,A
    return -A*w**2*np.cos((w*t)+(phi*np.pi))

plt.subplot(311)
t = np.arange(0.0, 50, 0.01)
plt.plot(t,position(t))
plt.axhline(0, color='black')
plt.xlabel('Tempo')
plt.ylabel('Posição')
plt.title('Posição em função do tempo')

plt.subplot(312)
plt.plot(t,velocity(t))
plt.axhline(0, color='black')
plt.xlabel('Tempo')
plt.ylabel('Velocidade')
plt.title('Velocidade em função do tempo')

plt.subplot(313)
plt.plot(t,acceleration(t))
plt.axhline(0, color='black')
plt.xlabel('Tempo')
plt.ylabel('Aceleração')
plt.title('Aceleração em função do tempo')


plt.show()