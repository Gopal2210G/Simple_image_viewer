from tkinter import*
from PIL import ImageTk,Image

root=Tk()

root.title('Image Viewer App')
# root.iconbitmap('\Python\logo_gmail_lockup_default_1x_r5.png')

my_img1=ImageTk.PhotoImage(Image.open("img1.jpg"))
my_img2=ImageTk.PhotoImage(Image.open("img2.jpg"))
my_img3=ImageTk.PhotoImage(Image.open("img3.jpg"))
my_img4=ImageTk.PhotoImage(Image.open("img4.png"))
my_img5=ImageTk.PhotoImage(Image.open("img5.jpg"))
my_img6=ImageTk.PhotoImage(Image.open("img6.jpg"))
my_img7=ImageTk.PhotoImage(Image.open("img7.jpg"))

image_list=[my_img1,my_img2,my_img3,my_img4,my_img5,my_img6,my_img7]

status=Label(root,text="Image 1 of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
label=Label(image=my_img1)
label.grid(row=0,column=0,columnspan=3)



def forward(image_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))

    if image_number==7:
        button_forward=Button(root,text=">>",state=DISABLED)
    status=Label(root,text="Image "+ str(image_number)+" of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=E)
    label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)



def back(image_number):
    global label
    global button_forward
    global button_back

    label.grid_forget()
    label=Label(image=image_list[image_number-1])
    button_forward=Button(root,text=">>",command=lambda: forward(image_number+1))
    button_back=Button(root,text="<<",command=lambda:back(image_number-1))

    if image_number==0:
        button_forward=Button(root,text="<<",state=DISABLED)

    status=Label(root,text="Image "+ str(image_number)+" of "+str(len(image_list)),bd=1,relief=SUNKEN,anchor=E)
    status.grid(row=2,column=0,columnspan=3,sticky=E)
    label.grid(row=0,column=0,columnspan=3)
    button_back.grid(row=1,column=0)
    button_forward.grid(row=1,column=2)




button_back=Button(root,text="<<",command=lambda:back(0),state=DISABLED)
button_exit=Button(root,text="Exit Program",command=root.quit)
button_forward=Button(root,text=">>",command=lambda: forward(2))

button_back.grid(row=1,column=0)
button_exit.grid(row=1,column=1)
button_forward.grid(row=1,column=2,pady=7)

status.grid(row=2,column=0,columnspan=3,sticky=E)
root.mainloop()
