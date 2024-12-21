import os
import pytesseract
import cv2


# read:
try:
    img_name = input("Digite o nome do arquivo da imagem: ")
    if not os.path.exists(img_name):
        raise FileNotFoundError(f"Arquivo '{img_name}' não encontrado.")
    r_img = cv2.imread(img_name)

# pytesseract correction:
    path_ = r"C:\Program Files\Tesseract-OCR"

# transcription:
    pytesseract.pytesseract.tesseract_cmd = path_ + r"\tesseract.exe"
    text = pytesseract.image_to_string(r_img, lang="por")
    print(text)

except Exception as e:
    print(f"Um erro inesperado ocorreu: {e}")
