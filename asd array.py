thrift = ['Baju bekas', 'Sepatu bekas', 'Topi bekas', 'Celana bekas']

#metode append
#metode append adalah metode yang berfungsi untuk menambahkan index kedalam variabel
def append():
    print('Data sebelum Append', thrift)
    barang = input("Masukkan nama barang Yang Ingin Ditambahkan: ")
    thrift.append(barang)
    print('Data sesudah Append : ', thrift)

#metode pop
#metode pop adalah metode yang dimana berfungsi untuk menghilangkan index didalam variabel
def pop():
    print('Data sebelum dihapus  :', thrift)
    index_ = int(input("masukan index barang yang anda ingin hapus :"))
    thrift.pop(index_)
    print('Data berhasil dihapus : ', thrift)

#metode sort
#metode sort adalah metode yang dimana berfungsi untuk mengurutkan list yang ada didalam variabel
def sort():
    print('Data sebelum terurut :', thrift)
    thrift.sort()
    print('Data setelah terurut : ', thrift)

#metode clear
#metode clear adalah metode yang berfungsi untuk menghapus isi variabel
def clear():
    thrift.clear()
    print('DATA KOSONG...', thrift)

#metode reverse
#metode reverse adalah metode yang berfungsi untuk membalik urutan index
def reverse():
    print('Data sebelum di reverse :', thrift)
    thrift.reverse()
    print('Data setelah di reverse :', thrift)

#metode remove
#metode remove adalah metode yang berfungsi menghapus index sesuai nama index tersebut
def remove():
    print('Data sebelum dihapus :', thrift)
    hapus = input("Masukkan nama barang Yang Ingin dihapus: ")
    thrift.remove(hapus)
    print('Data berhasil dihapus : ', thrift)

#metode count
#metode count adalah metode yang berfungsi untuk menghitung index yang ada didalam variabel
def count():
    print('Data :', thrift)
    hitung = input("Masukkan nama barang Yang Ingin dihitung: ")
    x = thrift.count(hitung)
    print(x)

#metode extend
#metode extend adalah metode yang berfungsi untuk menggabungkan list yang baru dengan yang lama
def extend():
    barang1 = ['Hoddie bekas', 'Crewneck', 'Kacamata']
    print('Sebelum di extend', thrift)
    print('Data List baru : ', barang1)
    thrift.extend(barang1)
    print('Setelah di extend', thrift)

#metode insert
#metode insert adalah metode yang berfungsi untuk menambahkan index baru pada posisi tertentu
def insert():
    print('Data Sebelum ditambah : ', thrift)
    p = input("ubah nama barang yang ingin ditambahkan : ")
    q = int(input("Masukkan index barang yang anda inginkan : "))
    thrift.insert(q, p)
    print('Data setelah ditambah : ',thrift)

def exit():
    print('Terimakasih')

def menu() :
        print(""""
        ======================================
        Selamat Datang Di Thrift Sumber Makmur
        ======================================
                1. .append
                2. .pop
                3. .sort
                4. .clear
                5. .reverse
                6. .remove
                7. .count
                8. .extend
                9. .insert
                10. exit
        =================================
        """)
        while True:
            x = input('Masukkan Pilihan (1/2/3/4/5/6/7/8/9/10): ')
            if x == '1':
                append()
                break
            elif x == '2':
                pop()
                break
            elif x == '3':
                sort()
                break
            elif x == '4':
                clear()
                break
            elif x == '5':
                reverse()
                break
            elif x == '6':
                remove()
                break
            elif x == '7':
                count()
                break
            elif x == '8':
                extend()
                break
            elif x == '9':
                insert()
                break
            elif x == '10':
                exit()
                break
            else :
                print('''yang anda ketik tidak terdapat!
                            Silahkan coba lagi
                ''')

            z = input('Apakah anda ingin melakukan lagi? (y/n):')
            if z == 'y':
                menu()
            elif z == 'n':
                exit()
            

menu()