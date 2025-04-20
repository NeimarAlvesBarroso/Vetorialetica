import numpy as np
import matplotlib.pyplot as plt

# Tamanho do campo contínuo
dim = 100
campo = np.random.rand(dim, dim) * 0.3  # Campo de coerência inicial fraca

# Reator vetorial - zona de reorganização coerente
def reator(x, y, cx, cy, intensidade=1.0, raio=10):
    dx, dy = x - cx, y - cy
    r = np.sqrt(dx**2 + dy**2)
    return intensidade * np.exp(-r**2 / (2 * raio**2))

# Aplicar reatores ao campo
def aplicar_reatores(campo, centros, intensidade=1.0, raio=10):
    novo = np.copy(campo)
    for cx, cy in centros:
        for i in range(dim):
            for j in range(dim):
                novo[i, j] += reator(i, j, cx, cy, intensidade, raio)
    return np.clip(novo, 0, 1)

# Centros dos reatores (posições vetoriais indutoras)
centros = [(30, 30), (70, 70), (50, 50)]

# Aplicar múltiplos reatores
campo_reorganizado = aplicar_reatores(campo, centros, intensidade=0.8, raio=8)

# Visualização
plt.figure(figsize=(6, 6))
plt.imshow(campo_reorganizado, cmap='plasma', interpolation='nearest')
plt.title("Campo com Reorganização Vetorial por Reatores")
plt.colorbar(label="Nível de Coerência")
plt.axis('off')
plt.show()
