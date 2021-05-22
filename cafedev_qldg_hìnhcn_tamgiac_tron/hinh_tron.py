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

class Hinh_Tron(Shape):

    def __init__(self, r):
        self.r = r
        
    def tinh_chu_vi(self):
        return 2*math.pi*self.r
    
    def tinh_dien_tich(self):
        return math.pi*math.pow(self.r,2)

if __name__ == '__main__':
    Htron = Hinh_Tron(1)
    print("Ban kinh hinh tron: ", Htron.r)
    print("Chu vi hinh tron: ", Htron.tinh_chu_vi())
    print("Dien tich hinh tron: ", Htron.tinh_dien_tich())
