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

from library.abc_giao_dich import*

class Giao_Dich_Vang(GiaoDich):

    def __init__(self, ma, ngay, soluong, loai, loai_vang, dongia):
        self.ma         = ma
        self.ngay       = ngay
        self.soluong    = soluong
        self.loai       = loai
        self.loai_vang  = loai_vang
        self.dongia     = dongia
    
    def tinh_tien(self):
        return self.soluong * self.dongia

    def in_giao_dich(self):
        result = ''
        result += str(self.ma) + ' - ' + str(self.ngay) + ' - ' + str(self.loai_vang)
        result += ' - ' + str(self.dongia) + ' - ' + str(self.soluong)
        result += ' - Thanh tien = ' + str(self.tinh_tien())
        return result
        
if __name__ == '__main__':

    giaodichvang = Giao_Dich_Vang(1,'12/12/12',2,1,'18k',123)
    print(giaodichvang.tinh_tien())
    print(giaodichvang.in_giao_dich())
