def test():
    print('Mencoba Function di Python!')

print(test)   


def perkalian(num1,num2):
    return num1*num2

'''
def dekteksiAngka(num1):
    if num1%2 == 0:
        print("Angka yang anda masukan adalah angka Genap")
    else :
        print("Angka yang anda masukan angka Ganjil")
'''

# TANTANGAN :
    # BUAT SEBUAH FUNGSI YG BISA MEMBERIKAN NILAI TRUE JIKA BISA MENEMUKAN KATA 'Python'!
'''  
masukanKata = input('Masukan Kalimat Yang Diminta :')
def trueORfalse(fungsi):
    
    if 'Python'.lower() in masukanKata:
        return True
    else:
        return False

print(trueORfalse(masukanKata))
'''
# !!!  TANTANGAN BERHASILL !!!
'''
# Lebih Ringkas :

masukan = input("masukan kata yang diminta:")
def masukanKata(kata):
    return 'Python'.lower() in kata
    
print(masukanKata(masukan))
'''