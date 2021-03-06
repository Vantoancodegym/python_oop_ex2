# -----------------------------------------------------------
#Cafedev.vn - Kênh thông tin IT hàng đầu Việt Nam
#@author cafedevn
#Contact: cafedevn@gmail.com
#Fanpage: https://www.facebook.com/cafedevn
#Group: https://www.facebook.com/groups/cafedev.vn/
#Instagram: https://instagram.com/cafedevn
#Twitter: https://twitter.com/CafedeVn
#Linkedin: https://www.linkedin.com/in/cafe-dev-407054199/
#Pinterest: https://www.pinterest.com/cafedevvn/
#YouTube: https://www.youtube.com/channel/UCE7zpY_SlHGEgo67pHxqIoA/
# -----------------------------------------------------------

from shape import *
import math

class Hinh_Tam_Giac(Shape):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def tinh_chu_vi(self):
        return self.a + self.b + self.c

    def tinh_dien_tich(self):
        # Su dung cong thuc heron
        p = (self.a + self.b + self.c)/2
        s = math.sqrt(p*(p - self.a)*(p - self.b)*(p - self.c))
        return s
    
if __name__ == '__main__':
    HTamGiac = Hinh_Tam_Giac(2,3,4) 
    print("Ba canh cua tam giac: ", HTamGiac.a, HTamGiac.b, HTamGiac.c)
    print("Chu vi tam giac: ", HTamGiac.tinh_chu_vi())
    print("Dien tichtam giac: ", HTamGiac.tinh_dien_tich())
