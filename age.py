umur=int(input("masukan tahun kelahiranmu: "))
age=int(2025)-int(umur)

if age >=18:
    print("umurmu", age,". ", "dan kamu sudah dewasa")

elif age <=12:
    print("umurmu", age,". ","dan kamu masih kecil")

else:
    print("umurmu", age , ".","kamu sudah remaja")