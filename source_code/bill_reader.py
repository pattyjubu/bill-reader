import sys
import subprocess
import cv2
import os
import csv


def isfloat(x):
    try:
        a = float(x)
    except (TypeError, ValueError):
        return False
    else:
        return True


def read_image(image_path):
    subprocess.Popen(['tesseract', image_path, 'temp', '-l', 'tha+eng'])
    fid = open('temp.txt', 'r', encoding='utf-8')
    read_data = fid.read()
    return read_data


def preprocess_image(image_bill_path, parent, image_bill_filename):
    filename_clear = 'clear_' + image_bill_filename
    image_bill_path_clear = os.path.join(parent, filename_clear)

    image = cv2.imread(image_bill_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 0, 255,
                         cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    cv2.imwrite(image_bill_path_clear, gray)
    return image_bill_path_clear


def write_csv(bill_csv_path, order_list, price_list):
    with open(bill_csv_path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for idx in range(len(order_list)):
            if idx >= len(price_list):
                price = '0.00'
            else:
                price = price_list[idx]
            writer.writerow([order_list[idx], price])


def bill_reader(image_bill_path):
    parent, image_bill_filename = os.path.split(image_bill_path)
    image_bill_path_clear = preprocess_image(image_bill_path, parent, image_bill_filename)
    read_data = read_image(image_bill_path_clear)

    # print(read_data)

    read_data_list = read_data.split('\n')
    order_list = []
    price_list = []
    for line in read_data_list:
        if line.strip() == '':
            pass
        elif isfloat(line):
            price_list.append(line)
        elif line[0] == '(':
            pass
        else:
            order_list.append(line)

    bill_csv_filename = image_bill_filename.split('.')
    bill_csv_filename = bill_csv_filename[0] + '_order.csv'
    bill_csv_path = os.path.join(parent, bill_csv_filename)
    write_csv(bill_csv_path, order_list, price_list)
    print(parent)
    print(bill_csv_filename)


if __name__ == '__main__':
    # path = r"C:\Patty\Learn\BillReader\test_images\test_bill_crop.jpg"
    # text = bill_reader(path)
    text = bill_reader(sys.argv[1])

