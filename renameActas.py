import os
import cv2
from pyzbar.pyzbar import decode

def rename_acta(old_name, new_name,output):
    try:
        extension = os.path.splitext(old_name)[1]
        os.rename(old_name,output+new_name+extension)
    except Exception as e:
        print(f"Error: {e}")
def barcode_reader(path):
    try:
        img = cv2.imread(path)
        grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        bardata = []
        codes = decode(grayimg)

        if len(codes) > 0:
            for barcode in codes:
                bardata.append(('Barcode', barcode))
                bartype = barcode.type
                barcode_text = barcode.data.decode('utf-8')
                print(f"tipo: {bartype}, barcode: {barcode.data.decode('utf-8')}")
        if bardata != 'CODE128':
            return barcode_text
        else:
            return None

    except Exception as e:
        print(f"Error: {e}")


folder_path = '../data/actas/'
ouputpath = '../data/renombradas/'

if not os.path.exists(ouputpath):
    os.makedirs(ouputpath)
    print("Folder Creado: " + ouputpath)
if not os.path.exists(folder_path):
    os.mkdir(folder_path)
    print("Folder creado: ", folder_path)
print(f"Copiar los jpg de las actas en {folder_path}")

files_list = os.listdir(folder_path)
for file in files_list:
    new_name = barcode_reader(folder_path+file)
    if new_name != "":
        rename_acta(folder_path+file, new_name,ouputpath)
        print(f"renombrado\n{new_name}\n")