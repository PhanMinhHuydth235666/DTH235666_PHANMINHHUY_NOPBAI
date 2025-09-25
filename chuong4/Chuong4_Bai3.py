def BMI(cao, nang):
    return cao/nang

def PhanLoai(bmi):
    if bmi < 18.5:
        return "Gầy"
    elif bmi <=24.9:
        return "Bình thường"
    elif bmi <= 34.9:
        return "Hơi béo"
    elif bmi <= 34.9:
        return "Béo phì cấp độ 1"
    elif bmi <= 39.9:
        return "Béo phì cấp độ 2"
    else:
        return "Béo phì cấp độ 3"
    
def NguyCoBenh(bmi):
    if bmi < 18.5:
        return "Thấp"
    elif bmi <=24.9:
        return "Trung Bình"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 34.9:
        return "Cao"
    elif bmi <= 39.9:
        return "Rất cao"
    else:
        return "Rất cao"

cao = float(input("Nhập vào chiều cao: "))
nang = float(input("Nhập vào cân nặng: "))

bmi = BMI(cao, nang)
print("BMI của bạn: ", bmi)
print("Phân loại của bạn: ", PhanLoai(bmi))
print("Nguy cơ bệnh của bạn: ", NguyCoBenh(bmi))
