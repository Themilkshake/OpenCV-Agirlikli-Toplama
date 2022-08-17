import cv2
import numpy as np

bir = cv2.imread("ce.jpg")
iki = cv2.imread("il.jpg")

#o kısımlardaki farklı resimlerin iki pikselinin renk değerlerini topluyoruz. 
#(255,255,255) 255'den sonrası sıfırlanıyor (sıfırdan başlıyor).

print(bir[50,50])
print(iki[50,50])
print(bir[50,50] + iki[50,50] )

cv2.waitKey(0)
cv2.destroyAllWindows()
