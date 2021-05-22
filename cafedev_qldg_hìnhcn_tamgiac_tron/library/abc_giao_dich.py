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

import abc

class GiaoDich(abc.ABC):
    
    @abc.abstractclassmethod
    def __init__(self, ma, ngay, soluong, loai):
        pass

    @abc.abstractclassmethod
    def tinh_tien(self):
        pass

    @abc.abstractclassmethod
    def in_giao_dich(self):
        pass
    

    
