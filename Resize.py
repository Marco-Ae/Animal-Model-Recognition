import os
from PIL import Image


class Path:
    def __init__(self, folder_path: str, format_im: str):
        self.folder_path = folder_path
        self.format_im = format_im
        self.file_list = sorted([f for f in os.listdir(self.folder_path) if f.endswith(self.format_im)]) #f sta per file
    
    def Resize(self, save_path: str, resize_h: int, resize_w: int):
        self.save_path = save_path
        self.resize_w = resize_w
        self.resize_h = resize_h
        os.makedirs(save_path, exist_ok = True) #se la cartella non esista la crea

        for file in self.file_list:
            full_path = os.path.join(self.folder_path, file)
            img = Image.open(full_path).convert("RGB")
            resized_img = img.resize((resize_w, resize_h)) #width, height
            resized_img.save(os.path.join(save_path, file)) #multipiattaforma 

            #resized_img.save(rf"{save_path}\{file}") #solo su windows, perche lo \ e per il path di windows crea problemi su altri OPSys
            #(Operative system)

#     /\     /\
#    {  `---'  }
#    {  O   O  }
#    ~~>  V  <~~
#     \  \|/  /
#      `-----'____
#      /  V   \    \_
#     {       }\  )_\_   
#     |  \_/  |/ /  \_\  
#      \__/  /(_/     \)
#        (__/