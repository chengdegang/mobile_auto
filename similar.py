import os
import shutil
import socket
import time
from pathlib import Path
import cv2
import numpy as np


"""
输入路径，支持判断两张图片是否相同，需要保证图片格式一致
"""
def similar(path1, path2):
    img1 = cv2.imread(path1, -1)
    img2 = cv2.imread(path2, -1)
    if (img1 is None):
        return False
    if (img2 is None):
        return False
    if (len(img1.shape) != len(img2.shape)):
        return False
    for i in range(len(img1.shape)):
        if (img1.shape[i] != img2.shape[i]):
            return False
    diff = np.sum(img1 - img2)
    if (diff > 1):
        return False
    return True

"""
jpg转png，并将转换过的jpg备份至新文件夹中
"""
def jpg_to_png(input_path):
    t = time.strftime("%Y_%m_%d_%H_%M", time.localtime())
    newdir = Path(f'{os.getcwd()}/images/backups/')
    if newdir.exists():
        print('cunz')
    else:
        newdir = os.mkdir(f'{os.getcwd()}/images/backups/')

    print(f'goal path: {newdir}/')
    for f_name in os.listdir(input_path):
        if '.jpg' in f_name:
            im = cv2.imread(input_path + f_name)  # 读取图片
            temname = f_name.split('.')[0]
            cv2.imwrite(input_path + temname + ".png", im)  # 保存为png
            #move
            shutil.move(str(f'{os.getcwd()}/images/{f_name}'),f'{newdir}/')
            #rename
            shutil.move(f'{newdir}/{f_name}',f"{newdir}/{f_name.split('.')[0]}_{t}.{f_name.split('.')[1]}")

if __name__ == '__main__':
    if similar('images/test_3.png','images/test_3的副本.png') ==True:
        print('图片相同')
    else:
        print('图片不同')

    # jpg_to_png(input_path='images/')



