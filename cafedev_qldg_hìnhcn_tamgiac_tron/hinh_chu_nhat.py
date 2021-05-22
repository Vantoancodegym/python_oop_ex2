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

from shape import*

class Hinh_Chu_Nhat(Shape):

    def __init__(self, chieudai, chieurong):
        self.chieudai = chieudai
        self.chieurong = chieurong

    def tinh_chu_vi(self):
        return (self.chieudai + self.chieurong)*2
    
    def tinh_dien_tich(self):
        return (self.chieudai* self.chieurong)

if __name__ == '__main__':
    HChuNhat = Hinh_Chu_Nhat(2,3)
    print("Chieu dai hinh chu nhat: ", HChuNhat.chieudai)
    print("Chieu rong hinh chu nhat: ", HChuNhat.chieurong)
    print("Chu vi hinh tron: ", HChuNhat.tinh_chu_vi())
    print("Dien tich hinh tron: ", HChuNhat.tinh_dien_tich())
