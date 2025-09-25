def ROI(dt,cp):
    return (dt - cp)/cp

def GoiYRoi(roi):
    if roi >= 0.75:
        print("==> Nên đầu tư - Chuong4_Bai4.py:6")
    else:
        print("==> Không nên đầu tư - Chuong4_Bai4.py:8")

print("Chương trình tính ROI - Chuong4_Bai4.py:10")
dt = int(input("Nhập doanh thu: "))
cp = int(input("Nhập chi phí: "))
roi = ROI(dt,cp)
print("Tỉ lệ ROI: - Chuong4_Bai4.py:14", roi)
GoiYRoi(roi)
