import numpy as np
import cv2

def redimensionarImagem(img, tam):
    altura, largura = img.shape
    return cv2.resize(img, (int(largura * tam), int(altura * tam)))

#here im reading the image, the second argument set how the image is going to load
logo = cv2.imread("assets/logo.png")
print(logo.shape)
logo_pretoebranco = cv2.cvtColor(logo, cv2.COLOR_BGR2GRAY)

#get width and heigth of the logo
altura_logo, largura_logo, _ = logo.shape

#For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold, it is set to 0, otherwise it is set to a maximum value.
#necessary the underscore before because threshold function returns un array of arguments
# Params:
# image, threshold value, maximum value, type of thresholding
_, logobin = cv2.threshold(logo_pretoebranco, 192, 255, cv2.THRESH_BINARY_INV)

logobininv = cv2.bitwise_not(logobin)

campus = cv2.imread("assets/Campus-Florestal.jpg")
print(campus.shape)
altura_campus, largura_campus, _ = campus.shape
#cut image so it has the same width and heigth of the logo
#to use bitwise operation the arrays must have the same width
campus_cut = campus[0:altura_logo, 0:largura_logo]


#use the bitwise and to put images
fundo_campus = cv2.bitwise_and(campus_cut, campus_cut, mask=logobininv)
logo_fundo = cv2.bitwise_and(logo, logo, mask=logobin)

final_cut = cv2.add(fundo_campus, logo_fundo)

#put the final cut on the original background image
campus[0:altura_logo, 0:largura_logo] = final_cut
cv2.imshow("final", campus)
cv2.waitKey(0)
cv2.destroyAllWindows()
