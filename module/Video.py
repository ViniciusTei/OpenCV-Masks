import cv2

class Video:
    def __init__ (self, bg_img, move_img, move_img_bin, move_img_bin_inv):
        self.bg_img = bg_img
        self.move_img = move_img
        self.move_img_bin = move_img_bin
        self.move_img_bin_inv = move_img_bin_inv

    def createVideo(self, path_out, fps, time):
        altura_bg, largura_bg, _ = self.bg_img.shape
        altura_move_img, largura_move_img, _ = self.move_img.shape
        x = largura_bg
        max_x = largura_bg - largura_move_img
        frames = []
        while(x > max_x):
            bg_copy = self.bg_img.copy()
            bg_cut = bg_copy[0:altura_move_img, int(largura_bg - x):largura_move_img + int(largura_bg - x)]
            
            bg = cv2.bitwise_and(bg_cut, bg_cut, mask=self.move_img_bin_inv)
            move = cv2.bitwise_and(self.move_img, self.move_img, mask=self.move_img_bin)

            final_cut = cv2.add(bg, move)
            bg_copy[0:altura_move_img, int(largura_bg - x):largura_move_img + int(largura_bg - x)] = final_cut
            x -= 10
            
            video_size = (largura_bg, altura_bg)
            frames.append(bg_copy)
        
        out = cv2.VideoWriter(path_out, cv2.VideoWriter_fourcc(*'mp4v'), fps, video_size)

        for i in range (len(frames)):
            out.write(frames[i])

        out.release()
        print('Video pronto!')