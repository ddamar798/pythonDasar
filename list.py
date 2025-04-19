# keranjang = [1, 9.8, " Apel"]
# #len(keranjang)

# # for i in range (len(keranjang)) :
#     # print(keranjang[0])
# keranjang[0]="nanas"

# buahLain = ['jeruk', 'lemon', 'strawbery', 'mangga']
# keranjang = keranjang + buahLain
# len(keranjang)

# for x in range (len(keranjang)):
#     print(keranjang)

# ============================================================
#                    Memotong isi sebuah list

# makanan = ["ayam", "soto", "sop", "sate"]
# makanan.pop(2) # .POP digunakan untuk memotong sebuah List.
# print(makanan)

# =============================================================
#                      Mengurutkan List

daftarSiswa = ['Zidan', 'Zizah', 'Zahra', "Putra", "Putri", "Silvia", "Dewi", "Izana", "Otero", "Dimas", "Riski"]
#daftarSiswa.sort() # sort <- untuk mengurutkan dari yang terkecil.
# daftarSiswa.reverse() <- untuk mengurutkan lis dari yang terbesar ke terkecil.
# print(daftarSiswa)

nilai = [54,32,24,24,4.5,5.6,8.6,9.7,34.7]
# nilai.sort()
nilai.reverse() # <- Nilai yang bertipe Float akan didahulukan.
#print(nilai)

#==============================================================
#                         NESTED LIST   
     
nestedList = [1,2,3,4,[5,6,7,8]]
#print (nestedList[4][2])
contoh2 = [1,2,3,4,5,[6,7,8,[9,10,11,'target',12]]] # Case = Keluarkan 'target'.
print (contoh2[5][3][3])