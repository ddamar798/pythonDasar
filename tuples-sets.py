keranjangT = (1,2,3,4,5,6,'a','c')  
cekTipe = type(keranjangT)

# Mengubah isi pada Tuple
t1 = (1,2,3)
t1 = t1[0],'rorr',t1[2] # Cara yng tdk efisien, Lebih baik menggunakan looping.
#print (t1)

# Methods di tuples    
x1 = (9,9,9,3,3,3,3,3)
#print( x1.count(9) ) # <- Fungsi x1.count adalah untuk menghitung jumlah isi di dalam tuples tersebut.

# Sets
# Sets adalah sebuah tipe data untuk elemen yang bersifat unik (tanpa duplikasi) dan tidak beraturan.
set_angka = [1,1,1,2,3,3,3,3,3,4,4,4,4,5,5,6,6,6,6,]
set_angka = set(set_angka)
print(set_angka)