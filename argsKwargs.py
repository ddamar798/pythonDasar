# Args dan Kwargs

#Args : Argumen dimana kita bisa memasukan sekian banyak Variable.
'''
def cekArgs(*args):
    return sum((args))

print(cekArgs(2,3)) # Menghasilkan 5
'''

# Kwargs : memasukan sekian banyak item Dictionary
def cekBerat(**kwargs):
    if 'Tono' in kwargs:
        print('Berat Tono Tergolong ke kategori {}'. format(kwargs['Tono']))
    else:
        print('Berat Tono tidak masuk dalam database kita!')

print(cekBerat(Tono='gemuk'))