# 导入所需类
from image_uploader import ImageUploader
from qr_decoder import QRCodeDecoder
from web_form_filler import FormFiller
import sys
from PyQt5.QtWidgets import QApplication
import time

def main():
    dc = my_dict = {'':''}

    print('##########上传二维码图片#############')
    # 创建应用程序
    app = QApplication(sys.argv)

    # 创建图片上传窗口
    uploader = ImageUploader()
    uploader.show()

    # 运行应用程序，等待上传图片
    app.exec_()

    #记录时长
    start_time = time.time()

    print('###########解码中###########\n')
    # 创建二维码解码器
    decoder = QRCodeDecoder()

    # 解码图片中的二维码
    url = decoder.decode_qrcode('1.png')

    print('****************自动填写中****************\n')
    # 创建Web表格自动填写器，并填写表格
    form_filler = FormFiller(url,dc=dc)
    form_filler.fill_form()

    print('\n自动填写完成！！')
    end_time = time.time()

    elapsed_time = end_time - start_time
    print("程序运行总时长为：{:.2f}秒".format(elapsed_time))

if __name__ == "__main__":
    main()
