import cv2
import numpy as np

resim1=cv2.imread("poo.jpg")
resim2=cv2.imread("ra.jpg")

"""
Sadece cv2.add() dersek iki resmin toplamını alıp bize veriyor.
Ama cv2.addWeighted(resim1,resim1'in ağırlığı, resim2, resim2'nin ağırlığı) dersek 
1. ve 2. resimden % kaç alacağını belirleyebiliyoruz.

weighted: ağırlıklı
**iki resmin de aynı boyutta olması gerekiyor.

"""
toplam=cv2.add(resim1,resim2)
cv2.imshow("toplamresim",toplam)
agirliklitoplama = cv2.addWeighted(resim1,0.3,resim2,0.7,0)
cv2.imshow("adi",agirliklitoplama)

cv2.waitKey(0)
cv2.destrroyAllWindows