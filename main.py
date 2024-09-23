import cv2
from pyzbar.pyzbar import decode


def barcode_reader(image_path):
    img = cv2.imread(image_path)

    detected_barcodes = decode(img)

    if not detected_barcodes:
        print("Barcode Not Detected or your barcode is blank/corrupted!")
    else:
        for barcode in detected_barcodes:
            if barcode.data != "":
                print(barcode.data.decode("utf-8"))
                print(barcode.type)


if __name__ == "__main__":
    path = 'images/08066961641.tif'
    barcode_reader(path)
