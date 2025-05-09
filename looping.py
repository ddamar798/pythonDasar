# For loops digunakan untuk melakukan Literasi.
# Hampir semua objek di Python bisa diliterasi (iterable).

# Aturan Penulisan
# for (item) in (items):
#     esekusi perintah
#============================================================
# for i in 'Nama saya Damar':
#     #print(i)


# angka = [1,2,3,4,5,7,8,9]
# # for isi in angka:
# #     print(isi)

# jumlah = 0

# for isi in angka:
#     jumlah = jumlah + isi
#     print('Hasil dari looping ke {} adalah {}' . format(isi,jumlah))

#===============================================================
#           Penggunaan Looping dan conditionals
#===============================================================

# *Case mencari angka ganjol genap dalam variable angka.
# angka = [1,2,3,4,5,6,7,8,9,10]

# for item in angka:
#     if item%2 == 0:   
#         print('Angka {} adalah angka Genap!', format(item)) 
#     else :
#         print ('Angka {} adalah angka Ganjil!', format(item))


#=============================================
#                   WHILE
#=============================================
# Ada tiga Arumen yang bisa digunakan :
# 1. break = menghentikan looping
# 2. continue = melanjutkan looping ke iterator selanjutnya dan melewati iterator saat ini
# 3. pass = tidak melakukan apa apa

# CODE :
# while (sebuah kondisi = True):
#   esekusi

indeks = 0
while True:
    #print('Looping berhasil')
    indeks +=1
    if indeks == 10:
        break
        
x = 0

while x < 50:
    #print('Bilanganya adalah ', x)
    x += 5

number = [1,2,3,4,5,6,7,8,9,10]

# for item in number:
#     if item%2 == 0:
#         continue
#     else:
       # print('angka ganjil adalah ', item)

for item in number:
    if item%2 != 0:
        continue
    else:
        print('Ini adalah angka genap = ', item)