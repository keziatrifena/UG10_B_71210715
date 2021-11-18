#Data
a=("85 - 100")
aMin=("80 - 84")
bPlus=("75 - 79")
b=("70 - 74")
bMin=("65 - 69")
cPlus=("60 - 64")
c=("55 - 59")
d=("45 - 54")
e=("0")

kode = str(input("Masukan nilai huruf PrakTekKom anda: "))
print("=========================")

if(kode)=="A":
    print("Rentang nilai PrakTekKom anda adalah",a)
elif(kode)=="A-":
    print("Rentang nilai PrakTekKom anda adalah",aMin)
elif(kode)=="B+":
    print("Rentang nilai PrakTekKom anda adalah",bPlus)
elif(kode)=="B":
    print("Rentang nilai PrakTekKom anda adalah",b)
elif(kode)=="B-":
    print("Rentang nilai PrakTekKom anda adalah",bMin)
elif(kode)=="C+":
    print("Rentang nilai PrakTekKom anda adalah",cPlus)
elif(kode)=="C":
    print("Rentang nilai PrakTekKom anda adalah",c)
elif(kode)=="D":
    print("Rentang nilai PrakTekKom anda adalah",d)
elif(kode)=="E":
    print("Rentang nilai PrakTekKom anda adalah",e)
else:
    print("Inputan anda salah atau nilai huruf tidak ada pada Standar Nilai")

