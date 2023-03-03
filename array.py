# #akses data
# a = [1,2,3,4,"well", "iya", True , 0.22]
# print(a)

# #menambah paling belakang
# a.append(100000)
# print(a)

# #mengubah data
# a.insert(6,"hooh")
# print(a)

# #menggabung 2 data list
# k = [300,2000,101]
# a.extend(k)
# print(a)

# #hapus menggunakan del
# del a[5]#menghapus bagian index
# print(a)

# #hapus menggunakan pop
# k.pop(1)#menghapus bagian index
# print(k)

# #hapus menggunakan remove
# k.remove(300)#menghapus variabel
# print(k)

# #list comprehesion

# # f = [
# #     "jamri kun",
# #     "jono joni",
# #     "yakub keo"
# # ]

# # namabelakang= [belakang.split(" ")[-1] for belakang in f]
# # print(namabelakang)

#tugas asd array
#disini kita menggunakan list dikarenakan python tidak dapat menggunakan array
thrift = ['Baju bekas', 'Sepatu bekas', 'Topi bekas', 'Celana bekas']

#metode append
#metode append adalah metode yang berfungsi untuk menambahkan index kedalam variabel
thrift.append('Kacamata vintange')
print(thrift)

#metode pop
#metode pop adalah metode yang dimana berfungsi untuk menghilangkan index didalam variabel
# thrift.pop(1)
# print(thrift)

#metode remove
#metode remove adalah metode yang berfungsi menghapus index sesuai nama index tersebut
thrift.remove('Baju bekas')
print(thrift)

#metode reverse
#metode reverse adalah metode yang berfungsi untuk membalik urutan index
thrift.reverse()
print(thrift)

#metode insert
thrift.insert(2,'Hoodie bekas')
print(thrift)

