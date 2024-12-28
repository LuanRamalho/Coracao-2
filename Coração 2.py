import tkinter as tk
import random

def draw_heart(canvas, x, y, size, color):
    """Desenha um coração no canvas."""
    points = [
        x, y + size // 2,  # Ponta inferior
        x - size // 2, y - size // 4,  # Curva esquerda
        x - size // 4, y - size,  # Topo esquerdo
        x, y - size // 2,  # Topo centro
        x + size // 4, y - size,  # Topo direito
        x + size // 2, y - size // 4  # Curva direita
    ]
    canvas.create_polygon(points, fill=color, outline="black", smooth=True)

def create_random_hearts():
    """Cria uma quantidade aleatória de corações com posições e cores aleatórias."""
    canvas.delete("all")
    num_hearts = random.randint(5, 20)  # Quantidade aleatória de corações
    colors = ["red", "pink", "purple", "orange", "blue", "yellow"]

    for _ in range(num_hearts):
        x = random.randint(50, 750)  # Posição x aleatória
        y = random.randint(50, 550)  # Posição y aleatória
        size = random.randint(20, 100)  # Tamanho aleatório
        color = random.choice(colors)  # Cor aleatória
        draw_heart(canvas, x, y, size, color)

# Configuração da janela principal
root = tk.Tk()
root.title("Corações Aleatórios")

canvas = tk.Canvas(root, width=800, height=600, bg="white")
canvas.pack()

# Botão para gerar novos corações
button = tk.Button(root, text="Gerar Corações", command=create_random_hearts)
button.pack()

# Desenho inicial
create_random_hearts()

# Inicia o loop principal
root.mainloop()
