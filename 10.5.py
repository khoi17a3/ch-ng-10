# xây dựng ctrinh kiem tra ma zip code
def kiem_tra_zip_code(zip_code):
    return len(zip_code) == 6 and zip_code.isdigit()
a=float(input("Nhập 6 số:"))
print(kiem_tra_zip_code('123456')) 
print(kiem_tra_zip_code('12345'))   
print(kiem_tra_zip_code('1234567'))  
print(kiem_tra_zip_code('12345a'))
#BÀI NÀY KHONGG BIẾT LÀM
def kiem_tra_ma_zip(z):
    if len(z)==6 and z.isdigit()==True:
        return True
    else:
        return False
z=input("Nhập mã zip :")
print(kiem_tra_ma_zip(z)) 
