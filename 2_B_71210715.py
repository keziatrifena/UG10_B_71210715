rsi=int(input("Masukkan besar RSI: "))
macd=str(input("Masukkan kondisi MACD: "))

jualR=("RSI lebih dari sama dengan 70")
beliR=("RSI kurang dari sama dengan 30")
jualM=("MACD Golden-cross")
beliM=("MACD Death-cross")

if(rsi)>=70 and (macd)=="death-cross":
       print(jualR, "dan", beliM, ", saatnya Jual")
elif(rsi)<=30 and (macd)=="golden-cross":
       print(beliR, "dan", jualM, ", saatnya beli")
elif(rsi)>=70 and (macd)=="golden-cross":
       print(jualR, "dan", jualM, ", Tunggu MACD sampai death-cross")
elif(rsi)<=30 and (macd)=="death-cross":
       print(beliR, "dan", beliM, ", Tunggu MACD sampai golden-cross")
else:
    print("RSI berada di area 31 - 69, Bukan saatnya untuk membeli maupun menjual")
