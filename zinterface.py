from tkinter import*
import smtplib
import sys





def email():
    print ("Note this requires internet")
    server =smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    username =input("input your username because you have selected email.: ")
    password = input("Input your password to login: ")
    text = input("email message here.: ")
    to = input("who are you sending this to: ")
    server.login(username,password)
    server.sendmail(username,to,text)

def deletebtn():
    tk2.destroy()



     
def newtk():
    tk2 =Tk()
    tk2.title("Something.")

    

def fow():
    fob=open('python/white letters','w')
    filetxt=input("what do you want to write to a white letters?:  ")
    fob.write(filetxt)


    
   
def canvastxt():
    fntsize = 0
    ctext=input("what would you like to write in the canvas?: ")
    fntsze=input("what size would you like big or small?: ")
    if fntsze=='small':
        fntsize=10
    if fntsze== 'big':
        fntsize = 30
    canvas = Canvas(tk, width=400, height=400)
    canvas.pack()
    canvas.create_text(150, 100, text=ctext,
                       font =fntsize)
    tk.title('canvastext')



    
tk = Tk()
canvas = Canvas(tk, width=500, height = 5)
canvas.pack()
btn1 = Button(tk, text="email", command=email)
btn1.pack()
tk.title("zinterface")
btn2 = Button(tk, text="write to file white letters  ", command = fow)
btn2.pack()
btn3 = Button(tk, text="write on a canvas", command=canvastxt)
btn3.pack()
btn4 = Button(tk, text= "exit", command = quit)
btn4.pack()
btn5 = Button(tk, text="something", command = newtk)
btn5.pack()
#btn6 = Button(tk, text = 'DELETE new window', command = deletebtn)
#btn6.pack()
photo = PhotoImage(file='plane_ship.png')
label9 = Label(tk, image=photo)
label9.pack()

