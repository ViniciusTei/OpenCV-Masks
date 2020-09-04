import cv2 as cv

class Image:
    def __init__ (self, src):
        self.img = cv.imread(src)

    def getSize(self):
        altura, largura, _ = self.img.shape
        return altura, largura

    def returnImgCinza(self):
        return cv.cvtColor(self.img, cv.COLOR_BGR2GRAY)

    def returnImgBinarizada(self, img_cinza):
        _, img_bin = cv.threshold(img_cinza, 192, 255, cv.THRESH_BINARY_INV)
        return img_bin