import cv2
import sys
from time import sleep

class Video:
    def __init__ (self, bg_img, move_img, move_img_bin, move_img_bin_inv):
        self.bg_img = bg_img
        self.move_img = move_img
        self.move_img_bin = move_img_bin
        self.move_img_bin_inv = move_img_bin_inv

    def createVideo(self, path_out, fps, time):
        altura_bg, largura_bg, _ = self.bg_img.shape
        altura_move_img, largura_move_img, _ = self.move_img.shape
        x = 0
        max_x = largura_bg - largura_move_img
        frames = []
        
        while(x < max_x):
            bg_copy = self.bg_img.copy()
            bg_cut = bg_copy[int(altura_bg/2):altura_move_img +int(altura_bg/2) , x:largura_move_img + x]
            
            bg = cv2.bitwise_and(bg_cut, bg_cut, mask=self.move_img_bin_inv)
            move = cv2.bitwise_and(self.move_img, self.move_img, mask=self.move_img_bin)

            final_cut = cv2.add(bg, move)
            bg_copy[int(altura_bg/2):altura_move_img +int(altura_bg/2), x:largura_move_img + x] = final_cut
            x += 10
            
            video_size = (largura_bg, altura_bg)
            frames.append(bg_copy)
        
        total_records = 100
        for i in range (total_records):
            sys.stdout.write('\rUpdated record: ' + str(i) + ' of ' + str(total_records))
            sys.stdout.flush()
            sleep(0.05) 
        out = cv2.VideoWriter(path_out, cv2.VideoWriter_fourcc(*'mp4v'), fps, video_size)

        for i in range (len(frames)):
            out.write(frames[i])

        out.release()
        print('\nVideo pronto!')
