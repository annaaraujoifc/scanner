import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

modelo = tf.keras.models.load_model("modelo_brecho.h5")

classes = ['bom', 'regular', 'ruim']


def analisar_imagem(caminho):

    if not os.path.exists(caminho):
        return "Arquivo não encontrado."

    img = image.load_img(
        caminho,
        target_size=(224, 224)
    )

    img_array = image.img_to_array(img)

    img_array = np.expand_dims(img_array, axis=0)

    img_array = img_array / 255.0

    prediction = modelo.predict(img_array)
    breakpoint()
    resultado = classes[np.argmax(prediction)]

    confianca = np.max(prediction) * 100

    return f"""
Resultado: {resultado}
Confiança: {confianca:.2f}%
"""


resultado = analisar_imagem("../boa.webp")

print(resultado)