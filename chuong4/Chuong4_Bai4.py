def ROI(dt,cp):
    return (dt - cp)/cp

def GoiYRoi(roi):
    if roi >= 0.75:
        print("==> Nên đầu tư ")
    else:
        print("==> Không nên đầu tư ")

print("Chương trình tính ROI ")
dt = int(input("Nhập doanh thu: "))
cp = int(input("Nhập chi phí: "))
roi = ROI(dt,cp)
print("Tỉ lệ ROI: ", roi)
GoiYRoi(roi)
