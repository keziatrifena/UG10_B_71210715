bil1=float(input("Masukkan bilangan pertama: "))
bil2=float(input("Masukkan bilangan kedua: "))
kal=str(input("Masukkan kalimat: "))

if "tambah" in kal:
        nilaiakhir = float(bil1+bil2)
        print("Hasil penjumlahan", bil1, "dengan", bil2, "adalah", float(nilaiakhir))
elif "kurang" in kal:
        nilaiakhir = float(bil1-bil2)
        print("Hasil pengurangan", bil1, "dengan", bil2, "adalah", float(nilaiakhir))
elif "kali" in kal:
        nilaiakhir = float(bil1*bil2)
        print("Hasil perkalian", bil1, "dengan", bil2, "adalah", float(nilaiakhir))
else:
        nilaiakhir = float(bil1/bil2)
        print("Hasil pembagian", bil1, "dengan", bil2, "adalah", float(nilaiakhir))
