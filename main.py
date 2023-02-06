"""
1.Python Fonksiyonlar Ödevi
"""
"""
Soru 1:
3 tane parametre alan bolunen_sayi_bulma isimli bir fonksiyon tanımlayınız.
Bu fonsiyon; min_sayi, max_sayi, bolen_sayi isimli parametreleri alsın.
Fonksiyon dışardan aldığı bu parametre değerlerini kullanarak, min_sayi ve max_sayi aralığındaki bolen_sayi 
değerine bölünen sayıları tam_bolunenler adlı bir diziye atayıp, listelesin.
tam_bolunenler dizisi ile min_sayi ve max_sayi arasındaki değerlerin sayısını return ile döndürsün.
"""
def bolunen_sayi_bulma(min_sayi, max_sayi, bolen_sayi):
    tam_bolunenler = []
    arasindaki_degerlerin_sayisi = 0
    for sayi in range(min_sayi, max_sayi):
        arasindaki_degerlerin_sayisi += 1
        if sayi % bolen_sayi == 0:
            tam_bolunenler.append(sayi)
    return print("Tam Bolunenler:", tam_bolunenler), print("Buyuk ve Kucuk Sayılar Arasındaki Değerlerin Sayısı:", arasindaki_degerlerin_sayisi)
bolunen_sayi_bulma(3, 9, 2)
"""
Soru 2:
sayi_atama ve sayi_okunusu isimli 2 tane fonksiyon tanımlayınız.
Bu fonksiyonlardan sayi_atama fonksiyonu 2 basamaklı bir sayıyı parametre olarak alsın ve fonksiyon içinde bu değer bir değişkene atansın.
Daha sonra sayi_atama fonksiyonu içinde sayi_okunusu isimli fonksiyon çağırılarak değişkene atanan sayının okunuşu string olarak verilsin.
sayi_atama fonksiyonu 2 basamaktan daha az yada daha fazla sayıyı kabul etmeyecektir.
"""
def sayi_atama(iki_basamakli_sayi):
    if iki_basamakli_sayi <= 99 and iki_basamakli_sayi >= 10:
        iki_basamakli_sayi_evet = iki_basamakli_sayi
    else:
        print("İki basamakli bir sayi girmediniz.")
        exit()
    return print(sayi_okunusu(iki_basamakli_sayi_evet))
def sayi_okunusu(iki_basamakli_sayi_evet):
    ilk_basamak = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmis", "Yetmis", "Seksen", "Doksan"]
    ikinci_basamak = ["", "Bir", "İki", "Üc", "Dort", "Bes", "Alti", "Yedi", "Sekiz", "Dokuz"]
    birler_basamak = iki_basamakli_sayi_evet % 10
    onlar_basamak = iki_basamakli_sayi_evet // 10
    return ilk_basamak[onlar_basamak] + " " + ikinci_basamak[birler_basamak]
sayi_atama(19)
"""
Soru 3:
Kullanıcının girdiği vize1, vize2, final notlarına göre harf notunu hesaplayınız.
-vize1 toplam notun %30'una etki edecektir.
-vize2 toplam notun %30'una etki edecektir.
-final toplam notun %40'ına etki edecektir.
Bu değerler 0-100 arası kabul edilmelidir!
Toplam Not >=  90 -----> AA
Toplam Not >=  85 -----> BA
Toplam Not >=  80 -----> BB
Toplam Not >=  75 -----> CB
Toplam Not >=  70 -----> CC
Toplam Not >=  65 -----> DC
Toplam Not >=  60 -----> DD
Toplam Not >=  55 -----> FD
Toplam Not <  55 -----> FF
"""
def harf_notu(vize1, vize2, final):
    toplam_not = ((vize1 * 30) /100) + ((vize2 * 30) /100) + ((final * 40) /100)
    if toplam_not >= 90:
        grade = "AA"
    elif toplam_not >= 85:
        grade = "BA"
    elif toplam_not >= 80:
        grade = "BB"
    elif toplam_not >= 75:
        grade = "CB"
    elif toplam_not >= 70:
        grade = "CC"
    elif toplam_not >= 65:
        grade = "DC"
    elif toplam_not >= 60:
        grade = "DD"
    elif toplam_not >= 55:
        grade = "FD"
    elif toplam_not < 55:
        grade = "FF"
    return print(grade)
harf_notu(90, 90, 80)