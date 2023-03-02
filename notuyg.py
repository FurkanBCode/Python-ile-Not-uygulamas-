def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(':')
    
    ogrenciAdi = liste[0]
    notlar = liste[1].split(',')
    
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    
    ortalama =  (not1 *0.4) + (not2 *0.6) 
    
    if ortalama>=90:
        harf = "AA"
    elif ortalama>=85 and ortalama<90:
        harf = "BA"
    elif ortalama>=68 and ortalama<85:
        harf = "BB"
    elif ortalama>=50 and ortalama<68:
        harf = "CC"
    elif ortalama>=45 and ortalama<50:
        harf = "DD"
    else :
        harf = "FF"
        
    return ogrenciAdi + ' : ' + harf + "\n"
    



def ort_oku():
    with open("sinav_notlari.txt","r", encoding="utf-8") as file:
        for satir in file:
            print(not_hesapla(satir))
        
def  not_gir():
        ad = input('Öğrenci adı: ')
        soyad =input('Öğrenci soyad: ')
        not1 = input('vize: ')
        not2 = input('final: ')
        
        
        with open("sinav_notlari.txt","a", encoding="utf-8") as file:
            file.write(ad+' '+ soyad+ ':'+not1+ ','+not2+'\n' )
        
def not_kyit():
    with open('sinav_notlari.txt',"r", encoding="utf-8") as file:
        liste = []
    
        for i in file:
            liste.append(not_hesapla(i))
        with open('sonuçlar.txt',"w", encoding="utf-8") as file2: 
            for i in liste:
                file2.write(i) 


while True:
    islem =input('1-Notları oku\n2-Notları gir\n3-Notları kaydet\n4-çıkış\n')
    
    if islem=='1' :
        ort_oku()
    elif islem=='2' :
        not_gir()
    elif islem=='3':
        not_kyit()
    else :
        break