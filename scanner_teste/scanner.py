import cv2
import numpy as np

def analisar_imagem(caminho):
    img = cv2.imread(caminho)

    if img is None:
        return "Erro ao carregar a imagem"

    # Converte para escala de cinza
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    total_pixels = gray.size

    # Pixels muito escuros (possíveis manchas)
    dark_pixels = np.sum(gray < 50)

    # Pixels muito claros (possíveis rasgos)
    white_pixels = np.sum(gray > 220)

    perc_dark = dark_pixels / total_pixels
    perc_white = white_pixels / total_pixels

    print(f"Porcentagem de manchas (escuro): {perc_dark:.2%}")
    print(f"Porcentagem de rasgos (claro): {perc_white:.2%}")

    if perc_dark > 0.10 or perc_white > 0.10:
        return "❌ Não recomendado para venda"
    elif perc_dark > 0.05 or perc_white > 0.05:
        return "⚠️ Estado regular"
    else:
        return "✅ Bom estado"


resultado = analisar_imagem("roupa.jpeg")  # ou roupa.jpg
print("\nResultado:", resultado)