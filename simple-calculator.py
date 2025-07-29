a1=int(input("masukan angka pertama: "))
a2=int(input("masukan angka kedua: "))

op=input("pilih operasi +,-,*,/: ")

if op =="+":
    hasil=a1 + a2

elif op =="-":
    hasil=a1 - a2

elif op =="*":
    hasil=a1 * a2

elif op =="/":
    if a2 !=0:
        hasil=a1 // a2
    else:
        hasil="tidak bisa dibagi dengan 0"

else:
    hasil="operasi tidak dikenali"

print("hasil: ", hasil)
