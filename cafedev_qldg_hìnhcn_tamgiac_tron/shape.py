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

'''
Xây dựng lớp trừu tượng
Anstract Base Class (ABC)
'''

import abc
class Shape(abc.ABC):
    
    @abc.abstractclassmethod
    def tinh_chu_vi(self):
        pass
    
    @abc.abstractclassmethod
    def tinh_dien_tich(self):
        pass
