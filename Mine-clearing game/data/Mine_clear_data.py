# import pygame


# SIZE = 20 # 格子大小
# face_size = int(SIZE * 1.25) # 笑脸大小

# pygame.init()
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# # 加载一堆图片
# # 点开后显示周围有几个雷的图片，注意重置图片尺寸大小
# img_amc0 = pygame.image.load('Mine-clearing game/data/pictures/0.bmp').convert()
# img_amc0 = pygame.transform.smoothscale(img_amc0, (SIZE, SIZE)) # 平滑缩放（这里可以用最近邻？或双线性）
# img_amc1 = pygame.image.load('Mine-clearing game/data/pictures/1.bmp').convert()
# img_amc1 = pygame.transform.smoothscale(img_amc1, (SIZE, SIZE))
# img_amc2 = pygame.image.load('Mine-clearing game/data/pictures/2.bmp').convert()
# img_amc2 = pygame.transform.smoothscale(img_amc2, (SIZE, SIZE))
# img_amc3 = pygame.image.load('Mine-clearing game/data/pictures/3.bmp').convert()
# img_amc3 = pygame.transform.smoothscale(img_amc3, (SIZE, SIZE))
# img_amc4 = pygame.image.load('Mine-clearing game/data/pictures/4.bmp').convert()
# img_amc4 = pygame.transform.smoothscale(img_amc4, (SIZE, SIZE))
# img_amc5 = pygame.image.load('Mine-clearing game/data/pictures/5.bmp').convert()
# img_amc5 = pygame.transform.smoothscale(img_amc5, (SIZE, SIZE))
# img_amc6 = pygame.image.load('Mine-clearing game/data/pictures/6.bmp').convert()
# img_amc6 = pygame.transform.smoothscale(img_amc6, (SIZE, SIZE))
# img_amc7 = pygame.image.load('Mine-clearing game/data/pictures/7.bmp').convert()
# img_amc7 = pygame.transform.smoothscale(img_amc7, (SIZE, SIZE))
# img_amc8 = pygame.image.load('Mine-clearing game/data/pictures/8.bmp').convert()
# img_amc8 = pygame.transform.smoothscale(img_amc8, (SIZE, SIZE))

# # 格子其他状态图
# img_ask = pygame.image.load('Mine-clearing game/data/pictures/ask.bmp').convert()
# img_ask = pygame.transform.smoothscale(img_ask, (SIZE, SIZE))
# img_explode = pygame.image.load('Mine-clearing game/data/pictures/explode.bmp').convert()
# img_explode = pygame.transform.smoothscale(img_explode, (SIZE, SIZE))
# img_flag = pygame.image.load('Mine-clearing game/data/pictures/flag.bmp').convert()
# img_flag = pygame.transform.smoothscale(img_flag, (SIZE, SIZE))
# img_mine = pygame.image.load('Mine-clearing game/data/pictures/mine.bmp').convert()
# img_mine = pygame.transform.smoothscale(img_mine, (SIZE, SIZE))
# img_normal = pygame.image.load('Mine-clearing game/data/pictures/normal.bmp').convert()
# img_normal = pygame.transform.smoothscale(img_normal, (SIZE, SIZE))
# img_wrong_mine = pygame.image.load('Mine-clearing game/data/pictures/wrong_mine.bmp').convert()
# img_wrong_mine = pygame.transform.smoothscale(img_wrong_mine, (SIZE, SIZE))

# # 经典笑脸
# img_face_fail = pygame.image.load('Mine-clearing game/data/pictures/face_fail.bmp').convert()
# img_face_fail = pygame.transform.smoothscale(img_face_fail, (face_size, face_size))
# img_face_normal = pygame.image.load('Mine-clearing game/data/pictures/face_normal.bmp').convert()
# img_face_normal = pygame.transform.smoothscale(img_face_normal, (face_size, face_size))
# img_face_success = pygame.image.load('Mine-clearing game/data/pictures/face_success.bmp').convert()
# img_face_success = pygame.transform.smoothscale(img_face_success, (face_size, face_size))
