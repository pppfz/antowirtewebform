import cv2
from pyzbar.pyzbar import decode


class QRCodeDecoder:
    @staticmethod
    def decode_qrcode(filename):
        # 读取图片
        image = cv2.imread(filename)

        # 解码二维码
        decoded = decode(image)

        # 获取解码结果
        url = None
        for d in decoded:
            url = d.data.decode()
            break

        return url
