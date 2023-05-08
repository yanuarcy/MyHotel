import os
import datetime
import csv


DataGuest = 'Guest.csv'
DataBranch = 'FileBranch.csv'
DataBooking = 'FileBookingRoom.csv'


class MainMenu():
    def __init__ (self):
        self.a = None

    def ClearLayarTerminal(self): #fungsi ini digunakan untuk membuat menghapus layar agar output terlihat lebih rapi
        os.system('cls' if os.name == 'nt' else 'clear')

    def PilihanMainMenu(self):
        self.ClearLayarTerminal()
        print("=" * 32)
        print("""
    Selamat Datang Di Progam
Management Hotel BangJul Official""", "\n")
        print("=" * 32)
        print("")
        print('''1. Guest
2. Branch
3. Booking
4. Keluar

            ''')

        User = input("Masukkan Pilihan Anda : ")
        if User == '1':
            ChgeWindow = GuestWindow()
            ChgeWindow.menu()

        elif User == '2':
            ChgeWindow = BranchWindow()
            ChgeWindow.menu()

        elif User == '3':
            ChgeWindow = BookingRuangan()
            ChgeWindow.menu()
        
        elif User == '4':
            exit()


# =======================================================
# =======================================================
# =======================================================
# =======================================================



class GuestNode(object):
    def __init__(self, data=None, next_node=None):
        self.menu = data['GuestList']
        self.next_node = next_node

class GuestWindow(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.editFile = 1
        self.insertFile = 1

    def TambahData(self, data):

        try:
            listData = ['Tanggal', 'ID', 'Nama', 'Phone', 'Points']
            new_node = GuestNode(data)


            with open(DataGuest, 'a', newline='') as fileTambah:
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


    def ClearLayarTerminal(self): #fungsi ini digunakan untuk membuat menghapus layar agar output terlihat lebih rapi
        os.system('cls' if os.name == 'nt' else 'clear')

    def BackToMenu(self):
        print("")
        input("Tekan Enter untuk kembali ke menu")
        self.menu()

    def menu(self): #fungsi ini digunakan untuk menampilkan dan menginput data
        self.Bucket = []
        Luping = 1
        self.insertFile = 1
        self.ClearLayarTerminal()
        print("=" * 32)
        print("""
        Daftar Tamu""", "\n")
        print("=" * 32)

        while Luping == 1:
            x = datetime.datetime.now()
            self.tanggal = x

            print("")
            print('''1. Tampilan Data
2. Tambah Data
3. Hapus Data
4. Update Data
5. Search Data
0. Main Menu
            ''')
            Optionn = str(input("Pilih Menu : "))
            
            if Optionn == "1":
                self.insertFile = 2
                self.ShowData()
            elif Optionn == "2":
                self.ShowData()
            elif Optionn == "3":
                self.insertFile = 3
                self.ShowData()
            elif Optionn == "4":
                self.insertFile = 4
                self.ShowData()
            elif Optionn == "5":
                self.insertFile = 5
                self.ShowData()
            elif Optionn == "0":
                ChgeWindow = MainMenu()
                ChgeWindow.PilihanMainMenu()
            

            while True:
                ulang = str(input("Ada Lagi? [y/t] : "))

                if ulang == 'y':
                    self.InputData()
                elif ulang == 't':
                    Luping += 2
                    # if self.editFile == 1:
                    #     self.tulisData1()
                    if self.editFile == 1:
                        self.TambahData({
                            "GuestList": self.Bucket
                        })
                    elif self.editFile == 2:
                        self.TambahData({
                            "GuestList": self.Bucket
                        })
                    self.insertFile = 2
                    self.ShowData()
                    break
                else:
                    continue

    def InputData(self):
        print("")
        print("Masukkan Data Guest")
        print("==========================")
        self.IDGuest = int(input("Masukkan ID    \t\t  : "))
        self.Nama = str(input("Masukkan Nama  \t\t  : "))
        self.Phone = str(input("Masukkan Nomer Telepon    : "))
        self.Points = int(input("Poin Loyalitas  \t  : "))
        
        dataCSV = {'Tanggal':self.tanggal.strftime("%x,%X %p"), 'ID':self.IDGuest, 'Nama':self.Nama, 'Phone':self.Phone, 'Points':self.Points}
        self.Bucket.append(dataCSV)
        print(self.Bucket)
        print("")


    def ShowData(self): #fungsi ini digunakan untuk menampilkan data sementara yang sudah diinput
        self.ClearLayarTerminal()

        try:
            with open(DataGuest, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                
                
                for data in baca:
                    print(data)


        except IOError as e:
            print(e)

        if self.insertFile == 1:
            self.InputData()
        elif self.insertFile == 2:
            self.BackToMenu()
        elif self.insertFile == 3:
            self.hapusData()
        elif self.insertFile == 4:
            self.UpdateData()
        elif self.insertFile == 5:
            self.SearchData()

        

    def hapusData(self): #fungsi ini digunakan untuk menghapus salah satu data yang diinginkan pengguna
        listData = ['Tanggal', 'ID', 'Nama', 'Phone', 'Points']
        print("")
        hapus = input("Masukkan ID : ")
        daftarHapus = []
        daftarBaru = []
        self.insertFile = 2

        try:
            with open(DataGuest, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                for isi in baca:
                    if isi['ID'] == hapus:
                        daftarHapus.append(hapus)
                        continue
                    else:
                        daftarBaru.append(isi)
                if isi['ID'] != hapus:
                    input("ID tidak ditemukan")
                    self.insertFile = 3
                    self.ShowData()
        except IOError as e:
            print(e)

        if len(daftarHapus) == 0:
            print("Data belum di input")
        else:
            try:
                with open(DataGuest, 'w', newline='') as fileTulis:
                    tulis = csv.DictWriter(fileTulis, fieldnames=listData) 
                    tulis.writeheader()
                    tulis.writerows(daftarBaru)
                    print("")
                    print("Data Pesanan telah dihapus")
            except IOError as e:
                print(e)

            self.ShowData()

    def UpdateData(self):
        listdata = ['Tanggal', 'ID', 'Nama', 'Phone', 'Points']
        print("")
        update = input("Masukkan ID yang akan di update : ")
        daftarUpdate = []
        self.insertFile = 2
        apdet = 0

        try:
            with open(DataGuest, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                for isi in baca:
                    if isi['ID'] == update:
                        print("============================================")
                        isi['ID'] = input("Masukkan ID Baru \t\t: ")
                        isi['Nama'] = input("Masukkan Nama Baru \t\t: ")
                        isi['Phone'] = input("Masukkan Nomer Telepon Baru \t: ")
                        isi['Points'] = input("Masukkan Poin Loyalitas Baru \t: ")
                        apdet = 1
                    daftarUpdate.append(isi)

                # if isi['ID'] != update:
                #     input("ID tidak ditemukan")
                #     self.insertFile = 4
                #     self.ShowData()

        except IOError as e:
            print(e)
        
        
        
        if apdet == 0:
            input("ID tidak ditemukan")
            self.insertFile = 4
            self.ShowData()
            
        else:
            try:
                with open(DataGuest, 'w', newline='') as fileTulis:
                    tulis = csv.DictWriter(fileTulis, fieldnames=listdata) 
                    tulis.writeheader()
                    tulis.writerows(daftarUpdate)
                    print("")
                    print("Data Pesanan telah diupdate")
            except IOError as e:
                print(e)

            self.ShowData()

    def SearchData(self):
        print("")
        Searching = input("Masukkan ID yang ingin anda cari : ")
        found = 0

        try:
            with open(DataGuest, 'r') as filebaca:
                baca = csv.DictReader(filebaca, delimiter=',')
                for isi in baca:
                    if isi['ID'] == Searching:
                        print("Data ditemukan")
                        print("============================================")
                        print(isi)
                        

                        self.BackToMenu()
                        found = 1
        except IOError as e:
            print(e)

        if found == 0:
            input("Data tidak ditemukan")
            self.insertFile = 5
            self.ShowData()



# ================================================================================================================
# ================================================================================================================
# ================================================================================================================



# Branch
class BranchNode(object):
    def __init__(self, data=None, next_node=None):
        self.menu = data['Branch']
        self.next_node = next_node

class BranchWindow(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.editFile = 1
        self.insertFile = 1

    def TambahData(self, data):
        try:
            listData = ['Tanggal', 'ID', 'Address', 'Phone']
            new_node = BranchNode(data)

            with open(DataBranch, 'a', newline='') as fileTambah:
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

    def ClearLayarTerminal(self): #fungsi ini digunakan untuk membuat menghapus layar agar output terlihat lebih rapi
        os.system('cls' if os.name == 'nt' else 'clear')

    def BackToMenu(self):
        print("")
        input("Tekan Enter untuk kembali ke menu")
        self.menu()

    def menu(self): #fungsi ini digunakan untuk menampilkan dan menginput data
        self.Bucket = []
        Luping = 1
        self.insertFile = 1
        self.ClearLayarTerminal()
        print("=" * 32)
        print("""
        Branch Tamu""", "\n")
        print("=" * 32)

        while Luping == 1:
            x = datetime.datetime.now()
            self.tanggal = x

            print("")
            print('''1. Display
2. Insert
3. Remove
4. Modify
5. Find
0. Main Menu
            ''')
            Optionn = str(input("Pilih Menu : "))
            
            if Optionn == "1":
                self.insertFile = 2
                self.ShowData()
            elif Optionn == "2":
                self.ShowData()
            elif Optionn == "3":
                self.insertFile = 3
                self.ShowData()
            elif Optionn == "4":
                self.insertFile = 4
                self.ShowData()
            elif Optionn == "5":
                self.insertFile = 5
                self.ShowData()
            elif Optionn == "0":
                ChgeWindow = MainMenu()
                ChgeWindow.PilihanMainMenu()
            

            while True:
                ulang = str(input("Ada Lagi? [y/t] : "))

                if ulang == 'y':
                    self.InputData()
                elif ulang == 't':
                    Luping += 2
                    # if self.editFile == 1:
                    #     self.tulisData1()
                    if self.editFile == 1:
                        self.TambahData({
                            "Branch": self.Bucket
                        })
                    elif self.editFile == 2:
                        self.TambahData({
                            "Branch": self.Bucket
                        })
                    self.insertFile = 2
                    self.ShowData()
                    break
                else:
                    continue

    def InputData(self):
        print("")
        print("Masukkan Data Booking Room")
        print("==========================")
        self.IDBranch = int(input("Masukkan ID    \t\t  : "))
        self.Address = str(input("Masukkan Alamat   \t  : "))
        self.Phone = str(input("Masukkan Nomor Telepon    : "))
        
        dataCSV = {'Tanggal':self.tanggal.strftime("%x,%X %p"), 'ID':self.IDBranch, 'Address':self.Address, 'Phone':self.Phone}
        self.Bucket.append(dataCSV)
        print(self.Bucket)
        print("")

    def ShowData(self): #fungsi ini digunakan untuk menampilkan data sementara yang sudah diinput
        self.ClearLayarTerminal()

        try:
            with open(DataBranch, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                
                for data in baca:
                    print(data)


        except IOError as e:
            print(e)

        if self.insertFile == 1:
            self.InputData()
        elif self.insertFile == 2:
            self.BackToMenu()
        elif self.insertFile == 3:
            self.hapusData()
        elif self.insertFile == 4:
            self.UpdateData()
        elif self.insertFile == 5:
            self.SearchData()

    def hapusData(self): #fungsi ini digunakan untuk menghapus salah satu data yang diinginkan pengguna
        listData = ['Tanggal', 'ID', 'Address', 'Phone']
        print("")
        hapus = input("Masukkan ID : ")
        daftarHapus = []
        daftarBaru = []
        self.insertFile = 2

        try:
            with open(DataBranch, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                for isi in baca:
                    if isi['ID'] == hapus:
                        daftarHapus.append(hapus)
                        continue
                    else:
                        daftarBaru.append(isi)
                if isi['ID'] != hapus:
                    input("ID tidak ditemukan")
                    self.insertFile = 3
                    self.ShowData()
        except IOError as e:
            print(e)

        if len(daftarHapus) == 0:
            print("Pesanan belum di input")
        else:
            try:
                with open(DataBranch, 'w', newline='') as fileTulis:
                    tulis = csv.DictWriter(fileTulis, fieldnames=listData) 
                    tulis.writeheader()
                    tulis.writerows(daftarBaru)
                    print("")
                    print("Data Pesanan telah dihapus")
            except IOError as e:
                print(e)

            self.ShowData()

    def UpdateData(self):
        listdata = ['Tanggal', 'ID', 'Address', 'Phone']
        print("")
        update = input("Masukkan ID yang akan di update : ")
        daftarUpdate = []
        self.insertFile = 2
        apdet = 0

        try:
            with open(DataBranch, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                for isi in baca:
                    if isi['ID'] == update:
                        isi['ID'] = input("Masukkan ID Baru : ")
                        isi['Address'] = input("Masukkan Alamat Baru : ")
                        isi['Phone'] = input("Masukkan Nomor Telepon Baru : ")
                        apdet = 1
                    daftarUpdate.append(isi)


        except IOError as e:
            print(e)
        
        if apdet == 0:
            input("Data tidak ditemukan")
            self.insertFile = 4
            self.ShowData()
            
        else:
            try:
                with open(DataBranch, 'w', newline='') as fileTulis:
                    tulis = csv.DictWriter(fileTulis, fieldnames=listdata) 
                    tulis.writeheader()
                    tulis.writerows(daftarUpdate)
                    print("")
                    print("Data Pesanan telah diupdate")
            except IOError as e:
                print(e)

            self.ShowData()

    def SearchData(self):
        print("")
        Searching = input("Masukkan ID yang ingin anda cari : ")
        found = 0

        try:
            with open(DataBranch, 'r') as filebaca:
                baca = csv.DictReader(filebaca, delimiter=',')
                for isi in baca:
                    if isi['ID'] == Searching:
                        print("Data Ditemukan")
                        print("==========================================================")
                        print(isi)
                        

                        self.BackToMenu()
                        found = 1
        except IOError as e:
            print(e)

        if found == 0:
            input("Data tidak ditemukan")
            self.insertFile = 5
            self.ShowData()



# ================================================================================================================
# ================================================================================================================
# ================================================================================================================


class BookingRuanganNode(object):
    def __init__(self, data=None, next_node=None):
        self.menu = data['BookingRoom']
        self.next_node = next_node

class BookingRuangan(object):
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail
        self.editFile = 1
        self.insertFile = 1

    def TambahData(self, data):

        try:
            listData = ['Tanggal', 'ID', 'RoomNo', 'BedCount', 'SmokingRoom']
            new_node = BookingRuanganNode(data)

            with open(DataBooking, 'a', newline='') as fileTambah:
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


    def ClearLayarTerminal(self): #fungsi ini digunakan untuk membuat menghapus layar agar output terlihat lebih rapi
        os.system('cls' if os.name == 'nt' else 'clear')

    def BackToMenu(self):
        print("")
        input("Tekan Enter untuk kembali ke menu")
        self.menu()

    def menu(self): #fungsi ini digunakan untuk menampilkan dan menginput data
        self.Bucket = []
        Luping = 1
        self.insertFile = 1
        self.ClearLayarTerminal()
        print("=" * 32)
        print("""
          Booking Kamar""", "\n")
        print("=" * 32)

        while Luping == 1:
            x = datetime.datetime.now()
            self.tanggal = x

            print("")
            print('''1. Display
2. Insert
3. Remove
4. Modify
5. Find
0. Main Menu
            ''')
            Optionn = str(input("Pilih Menu : "))
            
            if Optionn == "1":
                self.insertFile = 2
                self.ShowData()
            elif Optionn == "2":
                self.ShowData()
            elif Optionn == "3":
                self.insertFile = 3
                self.ShowData()
            elif Optionn == "4":
                self.insertFile = 4
                self.ShowData()
            elif Optionn == "5":
                self.insertFile = 5
                self.ShowData()
            elif Optionn == "0":
                ChgeWindow = MainMenu()
                ChgeWindow.PilihanMainMenu()
            

            while True:
                ulang = str(input("Ada Lagi? [y/t] : "))

                if ulang == 'y':
                    self.InputData()
                elif ulang == 't':
                    Luping += 2
                    # if self.editFile == 1:
                    #     self.tulisData1()
                    if self.editFile == 1:
                        self.TambahData({
                            "BookingRoom": self.Bucket
                        })
                    elif self.editFile == 2:
                        self.TambahData({
                            "BookingRoom": self.Bucket
                        })
                    self.insertFile = 2
                    self.ShowData()
                    break
                else:
                    continue

    def InputData(self):
        print("")
        print("Masukkan Data Booking Ruanngan")
        print("==========================")
        self.IDGuest = int(input("Masukkan ID    \t\t  : "))
        self.RoomNo = int(input("Masukkan Nomer Ruangan    : "))
        self.BedCount = int(input("Masukkan Jumlah Kasur     : "))
        self.SmokingRoom = str(input("Smoking Room (Ya/Tidak)   : "))
        
        dataCSV = {'Tanggal':self.tanggal.strftime("%x,%X %p"), 'ID':self.IDGuest, 'RoomNo':self.RoomNo, 'BedCount':self.BedCount, 'SmokingRoom':self.SmokingRoom}
        self.Bucket.append(dataCSV)
        print(self.Bucket)
        print("")


    def ShowData(self): #fungsi ini digunakan untuk menampilkan data sementara yang sudah diinput
        self.ClearLayarTerminal()

        try:
            with open(DataBooking, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                for data in baca:
                    print(data)



        except IOError as e:
            print(e)

        if self.insertFile == 1:
            self.InputData()
        elif self.insertFile == 2:
            self.BackToMenu()
        elif self.insertFile == 3:
            self.hapusData()
        elif self.insertFile == 4:
            self.UpdateData()
        elif self.insertFile == 5:
            self.SearchData()
        

    def hapusData(self): #fungsi ini digunakan untuk menghapus salah satu data yang diinginkan pengguna
        listData = ['Tanggal', 'ID', 'RoomNo', 'BedCount', 'SmokingRoom']
        print("")
        hapus = input("Masukkan ID : ")
        daftarHapus = []
        daftarBaru = []
        self.insertFile = 2

        try:
            with open(DataBooking, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                for isi in baca:
                    if isi['ID'] == hapus:
                        daftarHapus.append(hapus)
                        continue
                    else:
                        daftarBaru.append(isi)
                if isi['ID'] != hapus:
                    input("ID tidak ditemukan")
                    self.insertFile = 3
                    self.ShowData()
        except IOError as e:
            print(e)

        if len(daftarHapus) == 0:
            print("Pesanan belum di input")
        else:
            try:
                with open(DataBooking, 'w', newline='') as fileTulis:
                    tulis = csv.DictWriter(fileTulis, fieldnames=listData) 
                    tulis.writeheader()
                    tulis.writerows(daftarBaru)
                    print("")
                    print("Data Pesanan telah dihapus")
            except IOError as e:
                print(e)

            self.ShowData()

    def UpdateData(self):
        listdata = ['Tanggal', 'ID', 'RoomNo', 'BedCount', 'SmokingRoom']
        print("")
        update = input("Masukkan ID yang akan di update : ")
        daftarUpdate = []
        self.insertFile = 2
        apdet = 0

        try:
            with open(DataBooking, 'r') as fileBaca:
                baca = csv.DictReader(fileBaca, delimiter=',')
                for isi in baca:
                    if isi['ID'] == update:
                        isi['ID'] = input("Masukkan ID Baru : ")
                        isi['RoomNo'] = input("Masukkan Ruangan Kamar Baru : ")
                        isi['BedCount'] = input("Masukkan Jumlah Kasur Baru : ")
                        isi['SmokingRoom'] = input("Masukkan Smoking Room Baru : ")
                        apdet = 1
                    daftarUpdate.append(isi)


        except IOError as e:
            print(e)
        
        
        
        if apdet == 0:
            input("Data tidak ditemukan")
            self.insertFile = 4
            self.ShowData()
            
        else:
            try:
                with open(DataBooking, 'w', newline='') as fileTulis:
                    tulis = csv.DictWriter(fileTulis, fieldnames=listdata) 
                    tulis.writeheader()
                    tulis.writerows(daftarUpdate)
                    print("")
                    print("Data Pesanan telah diupdate")
            except IOError as e:
                print(e)

            self.ShowData()

    def SearchData(self):
        print("")
        Searching = input("Masukkan ID yang ingin anda cari : ")
        found = 0

        try:
            with open(DataBooking, 'r') as filebaca:
                baca = csv.DictReader(filebaca, delimiter=',')
                for isi in baca:
                    if isi['ID'] == Searching:
                        print("Data ditemukan")
                        print("==========================")
                        print(isi)

                        self.BackToMenu()
                        found = 1
        except IOError as e:
            print(e)

        if found == 0:
            input("Data tidak ditemukan")
            self.insertFile = 5
            self.ShowData()


if __name__ == "__main__":
    l = MainMenu()
    l.PilihanMainMenu()
