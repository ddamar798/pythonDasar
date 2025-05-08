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
angka = [1,2,3,4,5,6,7,8,9,10]

for item in angka:
    if item%2 == 0:   
        print('Angka {} adalah angka Genap!', format(item)) 
    else :
        print ('Angka {} adalah angka Ganjil!', format(item))


#=============================================
#                   WHILE
#=============================================