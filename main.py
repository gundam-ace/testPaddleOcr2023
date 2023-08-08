# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
import cv2 as opencv


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Paddleocr目前支持中英文、英文、法语、德语、韩语、日语，可以通过修改lang参数进行切换
# 参数依次为`ch`, `en`, `french`, `german`, `korean`, `japan`。
ocr = PaddleOCR(use_angle_cls=True, lang="ch")
# need to run only once to download and load model into memory
# img_path = 'UiCool_test.jpg'
# img_path = r"G:\Desktop202210\无线话筒1拖4订单信息.png"
img_path = r"D:\2023Python\QQ20220804092713.png"
result = ocr.ocr(img_path, cls=True)
for line in result:
    # print(line)
    for item in line:
        print(item)
# 显示结果


print("this is line[0]!!")
txts = [line[0][0] for line in result]
print("this is txts")
for item in txts:
    print(item)

from PIL import Image

image = Image.open(img_path).convert('RGB')
boxes = [detection[0] for line in result for detection in line]  # Nested loop added
txts = [detection[1][0] for line in result for detection in line]  # Nested loop added
scores = [detection[1][1] for line in result for detection in line]  # Nested loop added
im_show = draw_ocr(image, boxes, txts, scores)
im_show = Image.fromarray(im_show)
im_show.save('test.jpg')
# cv2.imshow('test.jpg')
img2 = opencv.imread('test.jpg')
opencv.imshow('windows', img2)
opencv.waitKey(0)