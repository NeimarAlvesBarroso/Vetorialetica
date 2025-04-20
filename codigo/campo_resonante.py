import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Dimensão do campo
dim = 50
campo = np.random.rand(dim, dim) * 0.2  # Coerência inicial fraca

# Vetor indutor ressonante
def vetor_indutor(x, y):
    cx, cy = dim // 2, dim // 2
    dx, dy = x - cx, y - cy
    r = np.sqrt(dx**2 + dy**2) + 1e-6
    return np.cos(r / 5) * np.exp(-r / 20)

# Função de atualização do campo
def atualizar(campo):
    novo = np.copy(campo)
    for i in range(1, dim - 1):
        for j in range(1, dim - 1):
            influencia = vetor_indutor(i, j)
            vizinhos = np.mean(campo[i-1:i+2, j-1:j+2])
            novo[i, j] += 0.1 * (vizinhos - campo[i, j]) + 0.05 * influencia
    return np.clip(novo, 0, 1)

# Animação do campo
fig, ax = plt.subplots()
img = ax.imshow(campo, cmap='viridis', interpolation='nearest')

def animar(frame):
    global campo
    campo = atualizar(campo)
    img.set_data(campo)
    return [img]

ani = animation.FuncAnimation(fig, animar, frames=100, interval=100, blit=True)
plt.title("Evolução de Campo Ressonante Vetorialético")
plt.show()
