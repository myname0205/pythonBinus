#def return42():
#    return 42
#
#if return42() < 50:
#    print("Good")

#4.1
#print("Inisialisai sistem motor...")
#print("Jika sesuai ketik 'Sudah'")
#
#i = 0
#def CheckSystems(part):
#    global i 
#    check = input(part)
#    if check == "Sudah":
#        i += 1
#
#CheckSystems("Apakah kunci sudah dimasukan? ")
#CheckSystems("Apakah saklar mati dalam posisi 'stop'? ")
#CheckSystems("Apakah standar samping sudah terangkat? ")
#CheckSystems("Apakah kopling ditarik? ")
#
#if i == 4:
#    print("Motor menyala")
#else:
#    print("Motor mengalami kegagalan")

#Latihan
#import math
#
#def HitungLuasDanVolume(shape):
#    if shape == "persegi":
#        print("PERSEGI")
#        sisi = int(input("Sisi: "))
#        print("Keliling = ", sisi * 4)
#        print("Luas = ", sisi ** 2)
#    elif shape == "persegi panjang":
#        print("PERSEGI PANJANG")
#        panjang = int(input("Sisi:"))
#        lebar = int(input("Lebar:"))
#        print("Luas = ", panjang * lebar)
#        print("Keliling = ", 2 * panjang * + 2 * lebar)
#    elif shape == "lingkaran":
#        print("LINGKARAN")
#        r = int(input("Radius:"))
#        print("Luas = ", math.pi * r**2)
#        print("Keliling =", 2 * math.pi * r)
#
#HitungLuasDanVolume("persegi")
#HitungLuasDanVolume("persegi panjang")
#HitungLuasDanVolume("lingkaran")

#class Persegi:
#
#    def __init__(self, sisi):
#        self.sisi = sisi
#
#    def CalculateCircumfrence(self):
#        cir = self.sisi*4
#        return cir
#
#    def CalculateArea(self):
#        area = self.sisi ** 2
#        return area
#    
#if __name__ == "__main__":
#    sisi = int(input("Sisi:"))
#    persegi = Persegi(sisi)
#    print("Circumfrence =", persegi.CalculateCircumfrence())
#    print("Area =", persegi.CalculateArea())

#HW
#amount = int(input("Jumlah mahasiswa yang ingin didata:"))
#listMahasiswa = []
#
#class Mahasiswa:
#     def __init__(self, nama, nik, tahun, jurusan, kampus, info):
#          self.nama = nama
#          self.nik = nik
#          self.tahun = tahun
#          self.jurusam = jurusan
#          self.kampus = kampus
#          self.info = info
#
#     def Assign(self):
#          for i in range(amount):
#            print("Mahasiswa yang ke", i + 1)
#          
#            nama = input("Name:")
#            
#            nik = "text"
#            notFirstTimeNIK = False
#            while nik.isnumeric() == False:
#               if(notFirstTimeNIK == True):
#                    print("Not valid NIK. Please rewrite a valid NIK!")
#               nik = input("NIK:")
#               notFirstTimeNIK = True
#
#            while tahun.isnumeric() == False:   
#                tahun = input("Tahun Masuk:")
#
#            while jurusan.isalpha() == False:
#               jurusan = input("Jurusan:")
#
#            while nik.isalpha() == False:
#               kampus = input("Kampus:")
#
#            info = {"Nama": nama, "NIK": nik, "Tahun masuk": tahun, 
#             "Jurusan": jurusan, "Kampus": kampus}
#            listMahasiswa.append(info)  
#     
#     def Display(self):
#         for l in range(amount):
#            print("### Data Mahasiswa", l + 1, "###")
#            print("Nama:", listMahasiswa[l]["Nama"])
#            print("NIK:", listMahasiswa[l]["NIK"])
#            print("Tahun masuk:", listMahasiswa[l]["Tahun masuk"])
#            print("Jurusan:", listMahasiswa[l]["Jurusan"])
#            print("Kampus:", listMahasiswa[l]["Kampus"])
#
#if __name__ == "__main__":
#    mahasiswa = Mahasiswa("a", "b", "c", "d", "e", "f")
#    mahasiswa.Assign()
#    mahasiswa.Display()
        
    








