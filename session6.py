import os 

print("Insert three names:")
name1 = input("Name 1:")
name2 = input("Name 2:")
name3 = input("Name 3:")

file = open(r"E:\Python\files\names.txt", "w")
file.write(name1 + "\n")
file.write(name2 + "\n")
file.write(name3 + "\n")

file.close()

print("Please open the file to see the names")

# Fungsi untuk menambahkan data karyawan
#def add_employee():
#    try:
#        another = 'y'
#        employee_file = open('employees.txt','a')
#        while another == 'y' or another == 'Y':
#            print('Masukkan data karyawan berikut: ')
#            name = input('Nama: ')
#            id_number = input('Nomor ID: ')
#            department  = input('Departemen: ')
#            employee_file.write(name + '\n')
#            employee_file.write(id_number + '\n')
#            employee_file.write(department + '\n')
#            print('Apakah Anda ingin menambahkan catatan lain?')
#            another = input('Y = ya, lainnya = tidak: ')
#        employee_file.close()
#        print('Data ditambahkan ke employees.txt')
#    except IOError as e:
#        print(f"Terjadi kesalahan saat mengakses file: {e}")
#    except Exception as e:
#        print(f"Terjadi kesalahan yang tidak terduga: {e}")
## Fungsi untuk menampilkan data karyawan
#def show_employees():
#    try:
#        employee_file = open('employees.txt', 'r')
#        name = employee_file.readline()
#        while name != '':
#            id_number = employee_file.readline()
#            department = employee_file.readline()
#            name = name.rstrip('\n')
#            id_number = id_number.rstrip('\n')
#            department = department.rstrip('\n')
#            print('Nama:', name)
#            print('Nomor ID:', id_number)
#            print('Departemen:', department)
#            print() # Baris kosong untuk memisahkan antar record
#            name = employee_file.readline()
#        employee_file.close()
#    except FileNotFoundError:
#        print("File employees.txt tidak ditemukan.")
#    except IOError as e:
#        print(f"Terjadi kesalahan saat mengakses file: {e}")
#    except Exception as e:
#        print(f"Terjadi kesalahan yang tidak terduga: {e}")
## Fungsi untuk mencari data karyawan
#def search_employee():
#    try:
#        found = False
#        search = input('Masukkan nama untuk mencari: ')
#        employee_file = open('employees.txt', 'r')
#        name = employee_file.readline()
#        while name != '':
#            id_number = employee_file.readline()
#            department = employee_file.readline()
#            name = name.rstrip('\n')
#            id_number = id_number.rstrip('\n')
#            department = department.rstrip('\n')
#            if name == search:
#                print('Nama:', name)
#                print('Nomor ID:', id_number)
#                print('Departemen:', department)
#                print()
#                found = True
#            name = employee_file.readline()
#        employee_file.close()
#        if not found:
#            print('Karyawan tersebut tidak ditemukan dalam file.')
#    except FileNotFoundError:
#        print("File employees.txt tidak ada.")
#    except IOError as e:
#        print(f"Terjadi kesalahan saat mengakses file: {e}")
#    except Exception as e:
#        print(f"Terjadi kesalahan yang tidak terduga: {e}")
## Fungsi untuk mengubah catatan karyawan
#def modify_employee():
#    try:
#        found = False
#        search = input('Masukkan nama karyawan untuk mencari: ')
#        new_department = input('Masukkan departemen baru: ')
#        employee_file = open('employees.txt', 'r')
#        temp_file = open('temp.txt', 'w')
#        name = employee_file.readline()
#        while name != '':
#            id_number = employee_file.readline()
#            department = employee_file.readline()
#            name = name.rstrip('\n')
#            id_number = id_number.rstrip('\n')
#            department = department.rstrip('\n')
#            if name == search:
#                temp_file.write(name + '\n')
#                temp_file.write(id_number + '\n')
#                temp_file.write(new_department + '\n')
#                found = True
#            else:
#                temp_file.write(name + '\n')
#                temp_file.write(id_number + '\n')
#                temp_file.write(department + '\n')
#            name = employee_file.readline()
#        employee_file.close()
#        temp_file.close()
#        os.remove('employees.txt')
#        os.rename('temp.txt', 'employees.txt')
#        if found:
#            print('File telah diperbaharui.')
#        else:
#            print('Karyawan tersebut tidak ditemukan dalam file.')
#    except FileNotFoundError:
#        print("File employees.txt tidak ditemukan.")
#    except IOError as e:
#        print(f"Terjadi kesalahan saat mengakses file: {e}")
#    except Exception as e:
#        print(f"Terjadi kesalahan yang tidak terduga: {e}")
## Fungsi untuk menghapus data karyawan
#def delete_employee():
#    try:
#        found = False
#        search = input('Masukkan nama karyawan yang akan dihapus: ')
#        employee_file = open('employees.txt', 'r')
#        temp_file = open('temp.txt', 'w')
#        name = employee_file.readline()
#        while name != '':
#            id_number = employee_file.readline()
#            department = employee_file.readline()
#            name = name.rstrip('\n')
#            id_number = id_number.rstrip('\n')
#            department = department.rstrip('\n')
#            if name != search:
#                temp_file.write(name + '\n')
#                temp_file.write(id_number + '\n')
#                temp_file.write(department + '\n')
#            else:
#                found = True
#            name = employee_file.readline()
#        employee_file.close()
#        temp_file.close()
#        os.remove('employees.txt')
#        os.rename('temp.txt', 'employees.txt')
#        if found:
#            print('File telah diperbaharui.')
#        else:
#            print('Karyawan tersebut tidak ditemukan dalam file.')
#    except FileNotFoundError:
#        print('File employees.txt tidak ditemukan.')
#    except IOError as e:
#        print(f"Terjadi kesalahan saat mengakses file: {e}")
#    except Exception as e:
#        print(f"Terjadi kesalahan yang tidak terduga: {e}")
## Fungsi utama untuk menyediakan opsi kepada pengguna
#def main():
#    while True:
#        print('Manajemen Data Karyawan')
#        print('1. Tambah Karyawan')
#        print('2. Tampilkan Karyawan')
#        print('3. Cari Karyawan')
#        print('4. Ubah Karyawan')
#        print('5. Hapus Karyawan')
#        print('6. Keluar')
#        choice = input('Masukkan pilihan Anda: ')
#        try:
#            if choice == '1':
#                add_employee()
#            elif choice == '2':
#                show_employees()
#            elif choice == '3':
#                search_employee()
#            elif choice == '4':
#                modify_employee()
#            elif choice == '5':
#                delete_employee()
#            elif choice == '6':
#                break
#            else:
#                print('Pilihan tidak valid. Silahkan coba lagi.')
#        except Exception as e:
#            print(f"Terjadi kesalahan yang tidak terduga: {e}")
## Memanggil fungsi utama
#main()
