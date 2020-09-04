import numpy as np
import cv2
from module.Image import Image
from module.Video import Video

def redimensionarImagem(img, tam):
    altura, largura, _ = img.shape
    return cv2.resize(img, (int(largura * tam), int(altura * tam)))

logo = Image("assets/logo.png")
logo.img = redimensionarImagem(logo.img, 0.5)
logo_pretoebranco = logo.returnImgCinza()

logobin = logo.returnImgBinarizada(logo_pretoebranco)

logobininv = cv2.bitwise_not(logobin)

campus = Image("assets/Campus-Florestal.jpg")

video = Video(campus.img, logo.img, logobin, logobininv)

video.createVideo('D:/Documentos/Codigos/PDI/atividade1/assets/teste.avi', 15, 10)
