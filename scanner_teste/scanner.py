import cv2
import numpy as np
import os

def carregar_imagem(caminho):
    if not os.path.exists(caminho):
        return None, "Arquivo não encontrado."

    img = cv2.imread(caminho)

    if img is None:
        return None, "Formato de imagem inválido ou corrompido."

    return img, None


def analisar_imagem(caminho):
    img, erro = carregar_imagem(caminho)

    if erro:
        return f"⚠️ Não foi possível analisar a imagem: {erro}"

    img = cv2.resize(img, (400, 400))

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)

    v_blur = cv2.GaussianBlur(v, (7,7), 0)

    brilho_medio = np.mean(v_blur)
    if brilho_medio < 50:
        return "⚠️ Foto muito escura. Tire outra em local iluminado."

    total_pixels = v_blur.size

    dark_pixels = np.sum(v_blur < 20)
    white_pixels = np.sum(v_blur > 245)

    perc_dark = dark_pixels / total_pixels
    perc_white = white_pixels / total_pixels

    print(f"Manchas: {perc_dark:.2%}")
    print(f"Rasgos: {perc_white:.2%}")
    print(f"Brilho: {brilho_medio:.2f}")

    if perc_white > 0.06 or perc_dark > 0.10:
        return "❌ Não recomendado para venda"
    elif perc_white > 0.02 or perc_dark > 0.05:
        return "⚠️ Estado regular"
    else:
        return "✅ Bom estado"


resultado = analisar_imagem("sapato.jpg")
print("\nResultado:", resultado)