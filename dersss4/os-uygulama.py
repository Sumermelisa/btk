#klasör oluştur ama hata mesajı versin
import os
while True:
    try:
        os.mkdir("elma")
        break

    except FileExistsError:
        print("böyle bir dosya zaten bulunmaktadır.")
        break
