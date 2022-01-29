from tkinter import *

def LeftClickButton(event):
    print(textBox_Weight.get(),textBox_Height.get())
    BMI=int(textBox_Weight.get())/((int(textBox_Height.get())/100)**2)
    print("BMI= ", BMI)
    if BMI>30:
        BMIR="อ้วนมาก /โรคอ้วนระดับ 3"
        label_Result.configure(text=BMIR)
    elif (BMI>=25 and BMI<30) :
        BMIR = "อ้วน /โรคอ้วนระดับ 2"
        label_Result.configure(text=BMIR)
    elif (BMI >= 23 and BMI < 25):
        BMIR = "ท้วม /โรคอ้วนระดับ 1"
        label_Result.configure(text=BMIR)
    elif (BMI >= 18.5 and BMI < 23):
        BMIR = "ปกติ /สุขภาพดี"
        label_Result.configure(text=BMIR)
    else :
        BMIR = "น้ำหนักน้อย /ผอม"
        label_Result.configure(text=BMIR)


MainWindow=Tk()
label_Height=Label(MainWindow,text="ส่วนสูง(cm)")
label_Height.grid(row=0,column=0)

textBox_Height=Entry(MainWindow)
textBox_Height.grid(row=0,column=1)

label_Weight=Label(MainWindow,text="น้ำหนัก(kg)")
label_Weight.grid(row=1,column=0)

textBox_Weight=Entry(MainWindow)
textBox_Weight.grid(row=1,column=1)

CalculateButton=Button(MainWindow,text="คำนวณค่า")
CalculateButton.bind('<Button-1>',LeftClickButton)
CalculateButton.grid(row=2,column=0)

label_Result=Label(MainWindow,text="Your BMI")
label_Result.grid(row=2,column=1)

MainWindow.mainloop()