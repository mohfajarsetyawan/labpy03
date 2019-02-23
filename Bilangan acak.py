print('====== Bilangan Acak Yang Lebih Kecil Dari 0,5 ======')
print(' ')
import random
N = int(input("Masukan nilai N : "))
a = 0
for x in range(N):
        a += 1
        b = random.uniform(.0,.5)
        print('Data ke:',a,'==>',b)
print('Selesai')
print('')
jawab = 'lanjutan'
hitung = 0
while jawab == "lanjutan":
        hitung += 1
        jawab = input('Ingin Mengulang? (yes/no) : ')
        if jawab == "Lanjutkan":
            break
print('Total perulangan : ' + str (hitung))
