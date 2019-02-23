#labpy03Codingan 
print('====== Bilangan Acak Yang Lebih Kecil Dari 0.5 ======')
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
    jawab = 'lanjutkan'
    hitung = 0
    while jawab == "lanjutkan":
        hitung += 1
        jawab = input('Ingin Mengulang? (yes/no) : ')
        if jawab == "Lanjutkan":
            break
    print('Total perulangan : ' + str (hitung))
 
Contoh gambar dari codingannya
![](https://github.com/mohfajarsetyawan/labpy03/blob/master/Bilangan%20acak%202.png)


Latihan2
Pertama menentukan variabel untuk menghitung, dan menentukan kapan 
perulangan berhenti. kalau pengguna menjawab tidak maka perulangan akan 
terhenti.
jawab = 'ya' hitung = 0
Melakukan perulangan dengan while, kemudian menambah satu variabel 
hitung setiap kali mengulang. lalu menanyakan kepada pengguna, apakah 
mau berhenti mengulang atau tidak?
while(jawab == 'ya'): hitung += 1 jawab = raw_input("Ulang lagi tidak? 
") Setelah selesai mengulang, cetak berapa kali perulangan tersebut 
terjadi
Codingan
```#!/usr/bin/python3
print("\nMenentukan Bilangan Terbesar")
print("\n")
max=0
while True:
    a=int(input("Masukan Bilangan :"))
    if max < a:
        max = a
    if a==0:
        break
print("Bilangan Terbesar = ", max)
input("\n")
```
Contoh gambar codingan
![](https://github.com/mohfajarsetyawan/labpy03/blob/master/Latihan2.0.png)

Program1
Jika urutan berisi daftar ekspresi, itu dievaluasi terlebih dahulu. 
Kemudian, item pertama dalam urutan ditugaskan ke variabel iterating 
iterating_var . Selanjutnya, blok pernyataan dieksekusi. Setiap item 
dalam daftar ditugaskan ke iterating_var , dan blok pernyataan 
dieksekusi sampai seluruh urutan habis.

Codingan
```a=100000000
for x in range(0,9):
        if(x>0 and x<=2):
                b=a*0
                print("laba bulan ke-",x," :",b)
        if(x>=3 and x<=4):
                c=a*0.1
                print("laba bulan ke-",x," :",c)
        if(x>=5 and x<=7):
                d=a*0.5
                print("laba bulan ke-",x," :",d)
        if(x==8):
                e=a*0.2
                print("laba bulan ke-",x," :",e)
total = b+b+c+c+d+d+d+e
print("\ntotal : ", total)
input("\n")
```
Contoh gambar codingan
![](https://github.com/mohfajarsetyawan/labpy03/blob/master/Program1.0.png)
