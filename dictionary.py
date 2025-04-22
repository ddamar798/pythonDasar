# PERBEDAAN DICTIONARY DENGAN LIST
              
# Dictionary
    # - Tidak memiliki urutan.
    # - Pengambilan item denggan cara menggunakan 'key'.
    # - Format -> dict1 = {'key1':item, 'key2':item, 'key3':item}

# List
    # - Memiliki urutan.
    # - Pemanggilan item dengan memanggil index-nya (urutan item).
    # - Format -> list1 = [item1,item2,item3].     

#==================================================================
    # Praktek

# Dictionary Biasa.
makanan = dict = {'burger':25000, 'piza':30000, 'ayamGoreng':1500, 'mieAyam':8000}
#print(makanan['mieAyam'])

# Mengabungkan Dictionary denggan List.

dict1 = dict = {'x1':'ayam', 'x2':45, 'x3':8.9,'bunga':['mawar', 'melati'], 'buah':{'b1':'apel', 'b2':'jeruk'}}
#print (dict1['buah']['b2'])

#print (makanan.keys()) <- Menampilkan keys

#print (makanan.values()) <- Menampilkan Value

#print (makanan.items()) <- Menampilkan Item

buah = (dict1['buah'])
bunga = (dict1['bunga'])

print(bunga)