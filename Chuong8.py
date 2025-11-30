#cau1
from tkinter import *

root = Tk()

def GiaiTiep():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

def GiaiPhuongTrinh():
    a=float(stringHSA.get())
    b=float(stringHSB.get())
    if a == 0 and b==0:
        stringKQ.set("Vô số nghiệm")
    elif a==0 and b!=0:
        stringKQ.set("Vô nghiệm")
    else:
        stringKQ.set("x="+str((-b/a)))

stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

root.title("PTB1")
root.minsize(height = 130, width = 250)
root.resizable(height = True, width = True)
lblTieuDe = Label(root, text = "Phương trinh bậc nhất", fg="red", font=("Tohama", 16), justify = CENTER). grid(row=0, column=0, columnspan=2)
lblHeSoA = Label(root, text = "Hệ số a").grid(row=1, column=0)
lblHeSoB = Label(root, text="Hệ số b").grid(row=2, column=0)

entHeSoA = Entry(root, width=30, textvariable = stringHSA).grid(row=1, column=1)
entHeSoB = Entry(root, width =30, textvariable=stringHSB).grid(row=2, column=1)

frameButton = Frame()
btnGiai = Button(frameButton, text="Giải", command=GiaiPhuongTrinh).pack(side=LEFT)
btnTiep = Button(frameButton, text="Tiếp", command=GiaiTiep).pack(side=LEFT)
btnThoat = Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=3, columnspan = 2)

lblKq = Label(root, text="Kết quả").grid(row=4, column=0)
txtKq = Entry(root, width =30, textvariable=stringKQ).grid(row=4, column=1)

root.mainloop()
#cau2
from tkinter import *
import math 

root = Tk()
stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ = StringVar()

def GiaiTiep():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

def GiaiPT():
    a = float(stringHSA.get())
    b = float(stringHSB.get())
    c = float(stringHSC.get())
    if(a==0):
        if(b==0):
            if(c==0):
                stringKQ.set("Vô số nghiệm")
            else:
                stringKQ.set("Vô nghiệm")
        else:
            stringKQ.set("x="+str((-c/b)))
    else:
        delta = b**2 - 4*a*c
        if(delta < 0):
            stringKQ.set("Vô nghiệm")
        elif(delta == 0):
            stringKQ.set("Nghiệm kép"+str((-b/2*a)))
        else:
            x1 = (-b - math.sqrt(delta))/ (2*a)
            x2 = (-b + math.sqrt(delta)) /(2*a)
            stringKQ.set("x1="+str(x1) + ", x2="+str(x2))

root.title("PTB2")
root.minsize(height=150, width=250)
root.resizable(height=True, width=250)

lblTieuDe = Label(root, text="Phương Trình Bậc 2", fg = "blue", font=("Tohama", 16), justify = CENTER).grid(row=0, columnspan=2)

lblHeSoA = Label(root, text="Hệ số a").grid(row=1, column=0)
lblHeSoB = Label(root, text="Hệ số b").grid(row=2, column=0)
lblHeSoC = Label(root, text="Hệ số c").grid(row=3, column=0)

entHeSoA = Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)
entHeSoB = Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)
entHeSoC = Entry(root, width=30, textvariable=stringHSC).grid(row=3, column=1)

frameButton = Frame()
btnGiai = Button(frameButton, text="Giải", command=GiaiPT).pack(side=LEFT)
btnThiep=Button(frameButton, text="Tiếp", command=GiaiTiep).pack(side=LEFT)
btnThoat=Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT)
frameButton.grid(row=4, columnspan=2)

lblKetQua = Label(root, text = "Kết quả").grid(row=5, column=0)
entKQ = Entry(root, width=30, textvariable=stringKQ).grid(row=5, column=1)

root.mainloop()
#cau3
from tkinter import *

root = Tk()

def TinhCong():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a+b))

def TinhTru():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a-b))

def TinhNhan():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a*b))

def TinhChia():
    a=float(stringA.get())
    b=float(stringB.get())
    stringKQ.set(str(a/b))

stringA = StringVar()
stringB = StringVar()
stringKQ = StringVar()

root.title("Cộng trừ nhân chia")
root.minsize(height=150, width=260)
root.resizable(height=True, width=True)

lblTieuDe = Label(root, text="CỘNG TRỪ NHÂN CHIA", font=("Tohama", 16)).grid(row=0, columnspan=3)

frameButton=Frame()
btnCong = Button(frameButton, text="Cộng", width=10, command=TinhCong).pack(side=TOP, fill=X)
btnTru = Button(frameButton, text="Trừ", width=10, command=TinhTru).pack(side=TOP, fill=X)
btnNhan = Button(frameButton, text="Nhân", width=10, command=TinhNhan).pack(side=TOP, fill=X)
btnChia = Button(frameButton, text="Chia", width=10, command=TinhChia).pack(side=TOP, fill=X)
frameButton.grid(row=1, column=0, rowspan=4)

lblSoA = Label(root, text="sô a").grid(row=1, column=1)
lblSoB = Label(root, text="số b").grid(row=2, column=1)
lblKetQua = Label(root, text="kết quả").grid(row=3, column=1)

entSoA = Entry(root, textvariable = stringA, width=20).grid(row=1, column=2)
entSoB = Entry(root, textvariable=stringB, width=20).grid(row=2, column=2)
entKQ = Entry(root, textvariable=stringKQ, width=20).grid(row=3, column=2)

btnThoat = Button(root, text="Thoát", command = root.quit).grid(row=4, column=2)

root.mainloop()
#cau4
from tkinter import *

root = Tk()
stringKQ = StringVar()


def click_button(value):
    current = stringKQ.get()
    stringKQ.set(current + value)

def clear():
    stringKQ.set("")

def TinhToan():
    try:
        result = str(eval(stringKQ.get()))
        stringKQ.set(result)
    except:
        stringKQ.set("Lỗi")

#root.minsize(height = 180, width= 30)
root.resizable(height=True, width=True)

entKQ = Entry(root, textvariable=stringKQ, width=40).grid(row=0, columnspan=3, padx=10, pady=10)

frameButton1 = Frame()
btn1 = Button(frameButton1, text="1", width=10, command= lambda: click_button("1")).pack(side=LEFT)
btn2 = Button(frameButton1, text="2", width=10, command= lambda: click_button("2")).pack(side=LEFT)
btn3 = Button(frameButton1, text="3", width=10, command= lambda: click_button("3")).pack(side=LEFT)
frameButton1.grid(row=1, columnspan=3)

frameButton2 = Frame()
btn4 = Button(frameButton2, text="4", width=10, command= lambda: click_button("4")).pack(side=LEFT)
btn5 = Button(frameButton2, text="5", width=10, command= lambda: click_button("5")).pack(side=LEFT)
btn6 = Button(frameButton2, text="6", width=10, command= lambda: click_button("6")).pack(side=LEFT)
frameButton2.grid(row=2, columnspan=3)

frameButton3 = Frame()
btn7 = Button(frameButton3, text="7", width=10, command= lambda: click_button("7")).pack(side=LEFT)
btn8 = Button(frameButton3, text="8", width=10, command= lambda: click_button("8")).pack(side=LEFT)
btn9 = Button(frameButton3, text="9", width=10, command= lambda: click_button("9")).pack(side=LEFT)
frameButton3.grid(row=3, columnspan=3)

frameButton4 = Frame()
btngach = Button(frameButton4, text="_", width=10, command= lambda: click_button("_")).pack(side=LEFT)
btn0 = Button(frameButton4, text="0", width=10, command= lambda: click_button("0")).pack(side=LEFT)
btncham = Button(frameButton4, text=".", width=10, command= lambda: click_button(".")).pack(side=LEFT)
frameButton4.grid(row=4, columnspan=3)

frameButton5 = Frame()
btncong = Button(frameButton5, text="+", width=5, command= lambda: click_button("+")).pack(side=LEFT)
btntru = Button(frameButton5, text="-", width=5, command= lambda: click_button("-")).pack(side=LEFT)
btnnhan = Button(frameButton5, text="*", width=5, command= lambda: click_button("*")).pack(side=LEFT)
btnchia = Button(frameButton5, text="/", width=5, command= lambda: click_button("/")).pack(side=LEFT)
btnbang = Button(frameButton5, text="=", width=7, command=TinhToan).pack(side=LEFT)
frameButton5.grid(row=5, columnspan=3)

btnhuy = Button(root, text="Clr", width=33, command=clear).grid(row=6, columnspan=3)

root.mainloop()
#cau5
from tkinter import *

frmLogin = Tk()
frmLogin.title("Enter New Password")
frmLogin.minsize(height=50, width=70)
frmLogin.resizable(False, False)


Label(frmLogin, text="Old Password:", anchor="w", width=22).grid(row=0, column=0, padx=10, pady=5, sticky="w")
Label(frmLogin, text="New Password:", anchor="w", width=22).grid(row=1, column=0, padx=10, pady=5, sticky="w")
Label(frmLogin, text="Enter New Password Again:", anchor="w", width=22).grid(row=2, column=0, padx=10, pady=5, sticky="w")

Entry(frmLogin, show="*", width=25).grid(row=0, column=1, padx=5, pady=5)
Entry(frmLogin, show="*", width=25).grid(row=1, column=1, padx=5, pady=5)
Entry(frmLogin, show="*", width=25).grid(row=2, column=1, padx=5, pady=5)


frameButton = Frame()
Button(frameButton, text="OK", width=10).pack(side=LEFT, padx=5)
Button(frameButton, text="Cancel", width=10).pack(side=LEFT, padx=5)
frameButton.grid(row=3, column=0, columnspan=2, pady=10)

frmLogin.mainloop()
#cau6
from tkinter import *

root = Tk()
root.title("frame 2")


reliefs = ["raised", "sunken", "flat", "ridge", "groove", "solid"]


for b in range(5):
    Label(root, text=f"borderwidth = {b}", width=15).grid(row=b, column=0, padx=5, pady=5)
    for j, r in enumerate(reliefs):
        Button(root, text=r, relief=r, borderwidth=b, width=10).grid(row=b, column=j+1, padx=3, pady=3)

root.mainloop()
#cau7
from tkinter import *

root = Tk()
root.title("Chuyển năm Dương lịch sang Âm lịch")

root.configure(bg="yellow")

can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]

nam_duong = StringVar()
nam_am = StringVar()

def chuyen_doi():
    try:
        nam = int(nam_duong.get())
        can_index = nam % 10
        chi_index = nam % 12
        nam_am.set(can[can_index] + " " + chi[chi_index])
    except:
        nam_am.set("Lỗi nhập năm!")

Label(root, text="Nhập năm dương:", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
Entry(root, textvariable=nam_duong, width=10, fg="red", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10)

Button(root, text="Chuyển", command=chuyen_doi, bg="lightblue", font=("Arial", 10)).grid(row=1, column=1, pady=5)

Label(root, text="Năm âm:", bg="yellow", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky="e")
Entry(root, textvariable=nam_am, width=15, font=("Arial", 12), state="readonly").grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
#cau8
from tkinter import *

root = Tk()
root.title("Chuyển độ F sang độ C")

root.configure(bg="yellow")

do_F = StringVar()
do_C = StringVar()

def chuyen_doi():
    try:
        f = float(do_F.get())
        c = (f - 32) * 5 / 9
        do_C.set(f"{c:.2f}")
    except:
        do_C.set("Lỗi nhập!")

frame = Frame(root, bg="yellow", bd=2, relief="solid", padx=10, pady=10)
frame.pack(padx=20, pady=20)

Label(frame, text="Nhập độ F", bg="yellow", font=("Arial", 12)).grid(row=0, column=0, padx=5, pady=5)
Entry(frame, textvariable=do_F, width=10, fg="red", font=("Arial", 12)).grid(row=0, column=1, padx=5, pady=5)

Button(frame, text="Chuyển", bg="lightblue", font=("Arial", 11, "bold"), command=chuyen_doi).grid(row=1, column=1, pady=5)

Label(frame, text="Độ C", bg="yellow", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
Entry(frame, textvariable=do_C, width=15, font=("Arial", 12), state="readonly").grid(row=2, column=1, padx=5, pady=5)

root.mainloop()
#cau9
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Phần mềm tính BMI")
root.configure(bg="yellow")

chieucao = StringVar()
cannang = StringVar()
bmi_value = StringVar()
tinhtrang = StringVar()
nguyco = StringVar()

def tinh_BMI():
    try:
        cao = float(chieucao.get())
        nang = float(cannang.get())
        bmi = nang / (cao ** 2)
        bmi_value.set(f"{bmi:.2f}")
        
        if bmi < 18.5:
            tinhtrang.set("Gầy")
            nguyco.set("Thấp")
        elif bmi < 25:
            tinhtrang.set("Bình thường")
            nguyco.set("Trung bình")
        elif bmi < 30:
            tinhtrang.set("Hơi béo")
            nguyco.set("Hơi cao")
        else:
            tinhtrang.set("Béo phì")
            nguyco.set("Rất cao")
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập đúng số!")

def thoat():
    root.destroy()

frame = Frame(root, bg="yellow", bd=2, relief="solid", padx=15, pady=15)
frame.pack(padx=20, pady=20)

Label(frame, text="Nhập chiều cao:", bg="yellow", font=("Arial", 11)).grid(row=0, column=0, sticky="e", pady=3)
Entry(frame, textvariable=chieucao, width=10, fg="red", font=("Arial", 12)).grid(row=0, column=1, pady=3)

Label(frame, text="Nhập cân nặng:", bg="yellow", font=("Arial", 11)).grid(row=1, column=0, sticky="e", pady=3)
Entry(frame, textvariable=cannang, width=10, fg="red", font=("Arial", 12)).grid(row=1, column=1, pady=3)

Button(frame, text="Tính BMI", bg="lightblue", font=("Arial", 11, "bold"), command=tinh_BMI).grid(row=2, column=1, pady=6)

Label(frame, text="BMI của bạn:", bg="yellow", font=("Arial", 11)).grid(row=3, column=0, sticky="e", pady=3)
Entry(frame, textvariable=bmi_value, width=10, font=("Arial", 12), state="readonly").grid(row=3, column=1, pady=3)

Label(frame, text="Tình trạng của bạn:", bg="yellow", font=("Arial", 11)).grid(row=4, column=0, sticky="e", pady=3)
Entry(frame, textvariable=tinhtrang, width=15, font=("Arial", 12), state="readonly").grid(row=4, column=1, pady=3)

Label(frame, text="Nguy cơ phát triển bệnh:", bg="yellow", font=("Arial", 11)).grid(row=5, column=0, sticky="e", pady=3)
Entry(frame, textvariable=nguyco, width=15, font=("Arial", 12), state="readonly").grid(row=5, column=1, pady=3)

Button(frame, text="Thoát", bg="lightblue", font=("Arial", 11, "bold"), command=thoat).grid(row=6, column=1, pady=8)

root.mainloop()

