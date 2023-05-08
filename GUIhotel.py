from timeit import default_timer as timer
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import datetime
import csv

FileCustomer = "Customer.csv"
FileRoom = "Room.csv"
FileRegister = "RegisterHotel.csv"


def main():
    win = Tk()
    app = Login(win)
    win.mainloop()


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("600x800+0+0")

        self.var_Username = StringVar()
        self.var_Password = StringVar()

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Yanuar\Downloads\Swiss2.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="Black")
        frame.place(x=110, y=60, width=370, height=690)

        img1 = Image.open(r"C:\Users\Yanuar\Downloads\LogoLoginApp3.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg="Black", borderwidth=0)
        lblimg1.place(x=245, y=70, width=100, height=100)

        get_str = Label(frame, text= "Login", font=('Times New Roman',20,'bold'), bg="Black", fg="White")
        get_str.place(x=145, y=120)

         # Username
        username = Label(frame, text="Username", font=('Times New Roman',15,'bold'), bg="black", fg="white")
        username.place(x=70, y=185)
        self.txtuser = ttk.Entry(frame, textvariable=self.var_Username, font=('Times New Roman',15,'bold'))
        self.txtuser.place(x=40, y=210, width=270)

        # Password
        password = Label(frame, text="Password", font=('Times New Roman',15,'bold'), bg="black", fg="white")
        password.place(x=70, y=255)
        self.txtpass = ttk.Entry(frame, textvariable=self.var_Password, font=('Times New Roman',15,'bold'), show="*")
        self.txtpass.place(x=40, y=280, width=270)

        img2 = Image.open(r"C:\Users\Yanuar\Downloads\LogoLoginApp3.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        lblimg2.place(x=150, y=243, width=25, height=25)

        img3 = Image.open(r"C:\Users\Yanuar\Downloads\2341515.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        lblimg3.place(x=150, y=310, width=25, height=25)

        loginbtn = Button(frame, text="Login", command=self.Login, font=('Times New Roman',15,'bold'), bg="red", fg="white", bd=3, relief=RIDGE, activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=370, width=120, height=35)

        registerbtn = Button(frame, text="Register", command=self.register, font=('Times New Roman',10,'bold'), bg="black", fg="white",borderwidth=0, activeforeground="white", activebackground="black")
        registerbtn.place(x=-10, y=330, width=160)

        get_str = Label(frame, text= "Final Project ASD", font=('Segoe Script',15,'bold'), bg="Black", fg="White")
        get_str.place(x=75, y=600)

    def Login(self):
        try:
            with open(FileRegister, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                for isi in baca:
                    if self.txtuser.get() == isi['Username'] and self.txtpass.get() == isi['Password']:
                        messagebox.showinfo("Login", "Login Berhasil")
                        self.new_window = Toplevel(self.root)
                        self.app = MainMenu(self.new_window)
                        break

                if self.txtuser.get() == "" or self.txtpass.get() == "":
                    messagebox.showerror("Error", "Silahkan isi terlebih dahulu")

                elif self.txtuser.get() != isi['Username'] or self.txtpass.get() != isi['Password']:
                    messagebox.showerror("Error", "Username atau Password Salah")

                        
        except IOError as e:
            print(e)

    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


class RegisterNode(object):
    def __init__(self, data=None, next_node=None):
        self.menu = data['Register']
        self.next_node = next_node

class Register:
    def __init__(self, root, head=None, tail=None):
        self.head = head
        self.tail = tail

        self.root = root
        self.root.title("Register")
        self.root.geometry("600x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Yanuar\Downloads\Swiss2.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="Black")
        frame.place(x=110, y=60, width=370, height=690)

        get_str = Label(frame, text= "Register", font=('Times New Roman',20,'bold'), bg="Black", fg="White")
        get_str.place(x=125, y=120)

         # Username
        username = Label(frame, text="Username Baru", font=('Times New Roman',15,'bold'), bg="black", fg="white")
        username.place(x=50, y=185)
        self.txtuser = ttk.Entry(frame, font=('Times New Roman',15,'bold'))
        self.txtuser.place(x=40, y=210, width=270)

        # Password
        password = Label(frame, text="Password Baru", font=('Times New Roman',15,'bold'), bg="black", fg="white")
        password.place(x=50, y=255)
        self.txtpass = ttk.Entry(frame, font=('Times New Roman',15,'bold'), show="*")
        self.txtpass.place(x=40, y=280, width=270)

        loginbtn = Button(frame, text="Register", command=self.Login, font=('Times New Roman',15,'bold'), bg="red", fg="white", bd=3, relief=RIDGE, activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=370, width=120, height=35)

        registerbtn = Button(frame, text="Login", command=self.Logindestroy, font=('Times New Roman',10,'bold'), bg="black", fg="white",borderwidth=0, activeforeground="white", activebackground="black")
        registerbtn.place(x=-10, y=330, width=160)
    

    def InsertData(self):
        self.listSementara = []
        dataCS = {"Username": self.txtuser.get(), "Password": self.txtpass.get()}
        self.listSementara.append(dataCS)


    def TambahData(self, data):
        start = timer()
        try:
            listData = ['Username', 'Password']
            new_node = RegisterNode(data)

            with open(FileRegister, 'a', newline='') as fileTambah:
                tulis = csv.DictWriter(fileTambah, fieldnames=listData)
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                    tulis.writerows(new_node.menu)

                else:
                    self.tail.next_node = new_node
                    self.tail = new_node
                    tulis.writerows(new_node.menu)

        except IOError as e:
            print(e)
        end = timer()
        print("Waktu yang dibutuhkan untuk menambah data Register: ", end - start)

    def Logindestroy(self):
        self.root.destroy()


    def Login(self):
        self.InsertData()
        messagebox.showinfo("Success", "Registrasi anda telah berhasil", parent=self.root)
        self.TambahData({
            'Register': self.listSementara
        })
        self.root.destroy()


class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Menu")
        self.root.geometry("600x800+0+0")


        self.bgMainmenu = ImageTk.PhotoImage(file=r"C:\Users\Yanuar\Downloads\Bg.jpg")
        lbl_bg = Label(self.root, image=self.bgMainmenu)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="grey48")
        frame.place(x=110, y=60, width=370, height=690)

        imgCS = Image.open(r"C:\Users\Yanuar\Downloads\logoCS.png")
        imgCS = imgCS.resize((100, 100), Image.ANTIALIAS)
        self.photoimageCS = ImageTk.PhotoImage(imgCS)
        lblimgCS = Label(self.root, image=self.photoimageCS, bg="grey48", borderwidth=0)
        lblimgCS.place(x=245, y=75, width=100, height=100)

        CSbtn = Button(frame, text= "Customer", command=self.Customer_Window, font=('Times New Roman',12,'bold'), width=1, bg="black", fg="white")
        CSbtn.place(x=118, y=140, width=130, height=50)

        imgBuking = Image.open(r"C:\Users\Yanuar\Downloads\logoBuking2.jpeg")
        imgBuking = imgBuking.resize((100, 100), Image.ANTIALIAS)
        self.photoimageBuking = ImageTk.PhotoImage(imgBuking)
        lblimgBuking = Label(self.root, image=self.photoimageBuking, bg="grey48", borderwidth=0)
        lblimgBuking.place(x=245, y=290, width=100, height=100)

        Bookingbtn = Button(frame, text= "Booking", command=self.Booking_Window, font=('Times New Roman',12,'bold'), width=1, bg="black", fg="white")
        Bookingbtn.place(x=118, y=355, width=130, height=50)

        imgExit = Image.open(r"C:\Users\Yanuar\Downloads\logoExit.jpeg")
        imgExit = imgExit.resize((100, 100), Image.ANTIALIAS)
        self.photoimageExit = ImageTk.PhotoImage(imgExit)
        lblimgExit = Label(self.root, image=self.photoimageExit, bg="grey48", borderwidth=0)
        lblimgExit.place(x=245, y=530, width=100, height=100)

        get_str = Button(frame, text= "Exit", command=self.Exit, font=('Times New Roman',12,'bold'), width=1, bg="black", fg="white")
        get_str.place(x=118, y=595, width=130, height=50)

    def Customer_Window(self):
        self.new_window = Toplevel(self.root)
        self.app = Customer(self.new_window)

    def Booking_Window(self):
        self.new_window = Toplevel(self.root)
        self.app = Booking(self.new_window)

    def Exit(self):
        Exit = messagebox.askyesno("MyHotel", "Do you want to exit?", parent=self.root)
        if Exit > 0:
            self.root.destroy()
            return

class CustomerNode(object):
    def __init__(self, data=None, next_node=None):
        self.menu = data['Customer']
        self.next_node = next_node

class Customer:
    def __init__(self, root, head=None, tail=None):
        self.head = head
        self.tail = tail

        self.root = root
        self.root.title("Customer")
        self.root.geometry("600x800+0+0")
        self.root.configure(bg="grey70")

        self.var_FirstName = StringVar()
        self.var_LastName = StringVar()
        self.var_Address = StringVar()
        self.var_city = StringVar()
        self.var_gender = StringVar()
        self.var_NIK = StringVar()
        self.var_Phone = StringVar()
        self.var_Email = StringVar()

        Judul = Label(self.root, text="Customer Details", font=('Segoe Script',14,'bold'), fg="black", bg="grey70")
        Judul.place(x=215, y=20)

        lblFirstName = Label(self.root, text="First Name", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblFirstName.place(x=20, y=100)
        self.txtFirstName = Entry(self.root, textvariable=self.var_FirstName, font=('Times New Roman',14), width=33)
        self.txtFirstName.place(x=250, y=100)

        lblLastName = Label(self.root, text="Last Name", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblLastName.place(x=20, y=150)
        self.txtLastName = Entry(self.root, textvariable=self.var_LastName, font=('Times New Roman',14), width=33)
        self.txtLastName.place(x=250, y=150)

        lblAddress = Label(self.root, text="Address", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblAddress.place(x=20, y=200)
        self.txtAddress = Entry(self.root, textvariable=self.var_Address, font=('Times New Roman',14), width=33)
        self.txtAddress.place(x=250, y=200)

        lblCity = Label(self.root, text="City", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblCity.place(x=20, y=250)
        self.txtCity = ttk.Combobox(self.root, textvariable=self.var_city, font=('Times New Roman',14), state='readonly', width=31)
        self.txtCity['values'] = ("Jakarta", "Bandung", "Surabaya", "Malang", "Yogyakarta")
        self.txtCity.place(x=250, y=250)

        lblGender = Label(self.root, text="Gender", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblGender.place(x=20, y=300)
        self.txtGender = ttk.Combobox(self.root, textvariable=self.var_gender, font=('Times New Roman',14), state='readonly', width=31)
        self.txtGender['values'] = ('Female','Male')
        self.txtGender.place(x=250, y=300)

        lblNIK = Label(self.root, text="NIK", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblNIK.place(x=20, y=350)
        self.txtNIK = Entry(self.root, textvariable=self.var_NIK, font=('Times New Roman',14), width=33)
        self.txtNIK.place(x=250, y=350)

        lblPhone = Label(self.root, text="Phone", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblPhone.place(x=20, y=400)
        self.txtPhone = Entry(self.root, textvariable=self.var_Phone, font=('Times New Roman',14), width=33)
        self.txtPhone.place(x=250, y=400)

        lblEmail = Label(self.root, text="Email", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblEmail.place(x=20, y=450)
        self.txtEmail = Entry(self.root, textvariable=self.var_Email, font=('Times New Roman',14), width=33)
        self.txtEmail.place(x=250, y=450)


        img1 = Image.open(r"C:\Users\Yanuar\Downloads\BgHotelcu.jpeg")
        img1 = img1.resize((400, 220), Image.ANTIALIAS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(self.root, image=self.photoimage1, bg="Black", borderwidth=0)
        lblimg1.place(x=100, y=480, width=400, height=218)


        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=15, bg="grey80")
        Framebutton.place(x=0, y=700, width=600, height=60)

        btn = Button(Framebutton, text="Save", command=self.Savedata, font=('Times New Roman',12,'bold'), width=11, bg="black", fg="grey70")
        btn.grid(row=0, column=0, padx=40)


        btn = Button(Framebutton, text="Reset", command=self.Resetdata, font=('Times New Roman',12,'bold'), width=11, bg="black", fg="grey70")
        btn.grid(row=0, column=1, padx=30)

        btn = Button(Framebutton, text="Exit", command=self.Exit, font=('Times New Roman',12,'bold'), width=11, bg="black", fg="grey70")
        btn.grid(row=0, column=2,padx=30)

    def Savedata(self):
        self.InsertData()
        messagebox.showinfo("Success", "Data telah ditambahkan", parent=self.root)
        self.TambahData({
            'Customer': self.listSementara
        })
        self.Resetdata()

    def Resetdata(self):
        self.var_FirstName.set("")
        self.var_LastName.set("")
        self.var_Address.set("")
        self.var_city.set("")
        self.var_gender.set("")
        self.var_NIK.set("")
        self.var_Phone.set("")
        self.var_Email.set("")


    def InsertData(self):
        self.listSementara = []
        dataCS = {'FirstName': self.txtFirstName.get(), 'LastName': self.txtLastName.get(), 'Address': self.txtAddress.get(), 'City': self.txtCity.get(), 'Gender': self.txtGender.get(), 'NIK': self.txtNIK.get(), 'Phone': self.txtPhone.get(), 'Email': self.txtEmail.get()}
        self.listSementara.append(dataCS)


    def TambahData(self, data):
        start = timer()
        try:
            listData = ['FirstName', 'LastName', 'Address', 'City', 'Gender', 'NIK', 'Phone', 'Email']
            new_node = CustomerNode(data)

            with open(FileCustomer, 'a', newline='') as fileTambah:
                tulis = csv.DictWriter(fileTambah, fieldnames=listData)
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                    tulis.writerows(new_node.menu)

                else:
                    self.tail.next_node = new_node
                    self.tail = new_node
                    tulis.writerows(new_node.menu)

        except IOError as e:
            print(e)
        end = timer()
        print("Waktu yang dibutuhkan untuk menambah data Customer: ", end - start)


    def Exit(self):
        Exit = messagebox.askyesno("MyHotel", "Do you want to exit?", parent=self.root)
        if Exit > 0:
            self.root.destroy()
            return

class BookingNode(object):
    def __init__(self, data=None, next_node=None):
        self.menu = data['Room']
        self.next_node = next_node   

class Booking:
    def __init__(self, root, head=None, tail=None):
        self.head = head
        self.tail = tail

        self.root = root
        self.root.title("Booking")
        self.root.geometry("600x800+0+0")
        self.root.configure(bg="grey70")

        self.var_Phone = StringVar()
        self.var_CheckIn = StringVar()
        self.var_CheckOut = StringVar()
        self.var_RoomType = StringVar()
        self.var_Room = StringVar()
        self.var_Meal = StringVar()
        self.var_NoOfDays = StringVar()
        self.var_Tax = StringVar()
        self.var_Total = StringVar()
        self.var_Payment = StringVar()
        self.Taxlist = StringVar()

        Judul = Label(self.root, text="Booking Details", font=('Segoe Script',14,'bold'), fg="black", bg="grey70")
        Judul.place(x=215, y=20)

        lblPhone = Label(self.root, text="Phone", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblPhone.place(x=20, y=100)
        txtPhone = Entry(self.root, font=('Times New Roman',14), textvariable=self.var_Phone, width=33)
        txtPhone.place(x=250, y=100)

        lblCheckIn = Label(self.root, text="Check-In Date", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblCheckIn.place(x=20, y=150)
        txtCheckIn = Entry(self.root, font=('Times New Roman',14), textvariable=self.var_CheckIn, width=33)
        txtCheckIn.place(x=250, y=150)

        lblCheckOut = Label(self.root, text="Check-Out Date", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblCheckOut.place(x=20, y=200)
        txtCheckOut = Entry(self.root, font=('Times New Roman',14), textvariable=self.var_CheckOut, width=33)
        txtCheckOut.place(x=250, y=200)

        lblRoomType = Label(self.root, text="RoomType", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblRoomType.place(x=20, y=250)
        txtRoomType = ttk.Combobox(self.root, font=('Times New Roman',14), textvariable=self.var_RoomType, state='readonly', width=31)
        txtRoomType['values'] = ("Single", "Double", "Suite", "Luxury")
        txtRoomType.place(x=250, y=250)

        lblAvailableRoom = Label(self.root, text="Available Room", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblAvailableRoom.place(x=20, y=300)
        txtAvailableRoom = ttk.Combobox(self.root, font=('Times New Roman',14), textvariable=self.var_Room, state='readonly', width=31)
        txtAvailableRoom['values'] = ("101", "102", "103", "104", "105", "106", "107", "108", "109", "110", "201", "202", "203", "204", "205", "206", "207" ,"208", "209", "210")
        txtAvailableRoom.place(x=250, y=300)

        lblMeal = Label(self.root, text="Meal", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblMeal.place(x=20, y=350)
        txtMeal = ttk.Combobox(self.root, font=('Times New Roman',14), textvariable=self.var_Meal, state='readonly', width=31)
        txtMeal['values'] = ("Breakfast", "Lunch", "Dinner")
        txtMeal.place(x=250, y=350)

        lblNoOfDays = Label(self.root, text="NoOfDays", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblNoOfDays.place(x=20, y=400)
        txtNoOfDays = Entry(self.root, font=('Times New Roman',14), textvariable=self.var_NoOfDays, state='readonly', width=33)
        txtNoOfDays.place(x=250, y=400)

        lblTax = Label(self.root, text="Tax", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblTax.place(x=20, y=450)
        txtTax = Entry(self.root, font=('Times New Roman',14), textvariable=self.var_Tax, state='readonly', width=33)
        txtTax.place(x=250, y=450)

        lblActualTotal = Label(self.root, text="Actual Total", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblActualTotal.place(x=20, y=500)
        txtActualTotal = Entry(self.root, font=('Times New Roman',14), textvariable=self.var_Total, state='readonly', width=33)
        txtActualTotal.place(x=250, y=500)

        lblTotalPayment = Label(self.root, text="Total Payment", font=('Times New Roman',14,'bold'), fg="black", bg="grey70")
        lblTotalPayment.place(x=20, y=550)
        txtTotalPayment = Entry(self.root, font=('Times New Roman',14), textvariable=self.var_Payment, state='readonly', width=33)
        txtTotalPayment.place(x=250, y=550)



        btn = Button(self.root, text="Calculate", command=self.Calculate, font=('Times New Roman',12,'bold'), width=11, bg="black", fg="grey70")
        btn.place(x=250, y=600)

        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=15, bg="grey80")
        Framebutton.place(x=0, y=700, width=600, height=60)

        btn = Button(Framebutton, text="Save", command=self.Savedata, font=('Times New Roman',12,'bold'), width=11, bg="black", fg="grey70")
        btn.grid(row=0, column=0, padx=40)

        btn = Button(Framebutton, text="Reset", command=self.Resetdata, font=('Times New Roman',12,'bold'), width=11, bg="black", fg="grey70")
        btn.grid(row=0, column=1, padx=30)

        btn = Button(Framebutton, text="Exit", command=self.Exit, font=('Times New Roman',12,'bold'), width=11, bg="black", fg="grey70")
        btn.grid(row=0, column=2, padx=30)

        day1 = datetime.date.today()
        day2 = datetime.timedelta(days=1)
        day3 = day1 + day2

        self.var_CheckIn.set(day1)
        self.var_CheckOut.set(day3)

    def Savedata(self):
        self.InsertData()
        messagebox.showinfo("Success", "Data telah ditambahkan", parent=self.root)
        self.TambahData({
            'Room': self.listSementara
        })
        self.Resetdata()

    def Resetdata(self):
        self.var_Phone.set("")
        self.var_RoomType.set("")
        self.var_Room.set("")
        self.var_Meal.set("")
        self.var_NoOfDays.set("")
        self.var_Tax.set("")
        self.var_Total.set("")
        self.var_Payment.set("")


    def InsertData(self):
        self.listSementara = []
        dataCS = {'Phone': self.var_Phone.get(), 'CheckIn': self.var_CheckIn.get(), 'CheckOut': self.var_CheckOut.get(), 'RoomType': self.var_RoomType.get(), 'AvailableRoom': self.var_Room.get(), 'Meal': self.var_Meal.get(), 'NoOfDays': self.var_NoOfDays.get(), 'Tax': self.var_Tax.get(), 'ActualTotal': self.var_Total.get(), 'Payment': self.var_Payment.get()}
        self.listSementara.append(dataCS)

    def TambahData(self, data):
        start = timer()
        try:
            listData = ['Phone', 'CheckIn', 'CheckOut', 'RoomType', 'AvailableRoom', 'Meal', 'NoOfDays', 'Tax', 'ActualTotal', 'Payment']
            new_node = CustomerNode(data)

            with open(FileRoom, 'a', newline='') as fileTambah:
                tulis = csv.DictWriter(fileTambah, fieldnames=listData)
                if self.head is None:
                    self.head = new_node
                    self.tail = new_node
                    tulis.writerows(new_node.menu)

                else:
                    self.tail.next_node = new_node
                    self.tail = new_node
                    tulis.writerows(new_node.menu)

        except IOError as e:
            print(e)
        end = timer()
        print("Waktu yang dibutuhkan untuk menambah data Booking: ", end - start)


    def Calculate(self):

        inDate = self.var_CheckIn.get()
        outDate = self.var_CheckOut.get()
        inDate = datetime.datetime.strptime(inDate, "%Y-%m-%d")
        outDate = datetime.datetime.strptime(outDate, "%Y-%m-%d")
        diff = (outDate - inDate).days
        self.var_NoOfDays.set(diff)

        if self.var_RoomType.get() == "Single" and self.var_Meal.get() == "Breakfast":
            HargaRoom = 100000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 85000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)

        elif self.var_RoomType.get() == "Single" and self.var_Meal.get() == "Lunch":
            HargaRoom = 100000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 85000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)
        
        elif self.var_RoomType.get() == "Single" and self.var_Meal.get() == "Dinner":
            HargaRoom = 100000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 85000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)

        elif self.var_RoomType.get() == "Double" and self.var_Meal.get() == "Breakfast":
            HargaRoom = 150000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 85000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)

        elif self.var_RoomType.get() == "Double" and self.var_Meal.get() == "Lunch":
            HargaRoom = 150000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 85000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)

        elif self.var_RoomType.get() == "Double" and self.var_Meal.get() == "Dinner":
            HargaRoom = 150000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 85000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)

        elif self.var_RoomType.get() == "Suite" and self.var_Meal.get() == "Breakfast":
            HargaRoom = 200000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 95000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)

        elif self.var_RoomType.get() == "Suite" and self.var_Meal.get() == "Lunch":
            HargaRoom = 200000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 95000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)

        elif self.var_RoomType.get() == "Suite" and self.var_Meal.get() == "Dinner":
            HargaRoom = 200000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 95000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)

        elif self.var_RoomType.get() == "Luxury" and self.var_Meal.get() == "Breakfast":
            HargaRoom = 250000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 100000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)

        elif self.var_RoomType.get() == "Luxury" and self.var_Meal.get() == "Lunch":
            HargaRoom = 250000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 100000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)

        elif self.var_RoomType.get() == "Luxury" and self.var_Meal.get() == "Dinner":
            HargaRoom = 250000
            HargaMeal = 50000
            HargaHari = int(self.var_NoOfDays.get()) * 100000
            HargaTax = (HargaRoom + HargaMeal + HargaHari) / 5
            HargaTotal = HargaRoom + HargaMeal + HargaHari * 7
            HargaPayment = HargaTotal + HargaTax
            HargaTaxx = "Rp " + str(HargaTax)
            HargaTotalx = "Rp " + str(HargaTotal)
            HargaPaymentx = "Rp " + str(HargaPayment)
            self.var_Tax.set(HargaTaxx)
            self.var_Total.set(HargaTotalx)
            self.var_Payment.set(HargaPaymentx)



    def Exit(self):
        Exit = messagebox.askyesno("MyHotel", "Do you want to exit?", parent=self.root)
        if Exit > 0:
            self.root.destroy()
            return      


if __name__ == "__main__":
    main()