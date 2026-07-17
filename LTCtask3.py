warning = '5 cehdiniz var'
print(warning)
count = 0

#chbt = ["salam", "menyu", "sifaris", "qiymet"]

while count < 5:
    user_input = input("Mesajınızı daxil edin: ").lower()

    if ("salam" in user_input and 'sifaris'  in user_input) or ("salam" not in user_input and 'sifaris'  in user_input):
        print("Sifarişiniz qəbul edildi\nbuyurun menyunu seçin\nBu gün: plov, kabab, şorba")
        secim = input("Seçiminizi daxil edin: ").lower()
        if secim == "plov":
            print(f"Plov sifarişiniz qəbul edildi")
            break
        elif secim == "kabab":
            print(f"Kabab sifarişiniz qəbul edildi")
            break
        elif secim == "şorba":
            print(f"Şorba sifarişiniz qəbul edildi")
            break
        else:
            print("Başa düşmədim, zəhmət olmasa yenidən yazın")
            count += 1
            if count == 5:
                print("Cəhdləriniz bitdi. Zəhmət olmasa yenidən cəhd edin.")
            continue
    elif "menyu" in user_input:
        print("Bu gün: plov, kabab, şorba")
        secim = input("Seçiminizi daxil edin: ").lower()
        if secim == "plov":
            print("Plov sifarişiniz qəbul edildi")
            break
        elif secim == "kabab":
            print("Kabab sifarişiniz qəbul edildi")
            break
        elif secim == "şorba":
            print("Şorba sifarişiniz qəbul edildi")
            break
    elif "qiymet" in user_input:
        print("Orta çek 15 AZN-dir")
        count += 1
        if count == 5:
            print("Cəhdləriniz bitdi. Zəhmət olmasa yenidən cəhd edin.")
    elif "salam" in user_input and 'sifaris' not in user_input:
        print("Resteranımıza xoş gəldiniz!")
        count += 1
        if count == 5:
            print("Cəhdləriniz bitdi. Zəhmət olmasa yenidən cəhd edin.")
            break
        continue
    else:
        print("Başa düşmədim, zəhmət olmasa yenidən yazın")
        count += 1
        if count == 5:
            print("Cəhdləriniz bitdi. Zəhmət olmasa yenidən cəhd edin.")
        continue


