# 1. Bu açar-dəyər cütləri ilə bir **dictionary** yaradın:
#     - `"hava"` → `"Hava durumunu deyir"`
#     - `"tercume"` → `"Mətni tərcümə edir"`
# 2. `.items()` və `for` ilə alətləri belə çap edin:
# `Alət: hava | İş: Hava durumunu deyir`
# 3. `.get()` ilə `"musiqi"` adlı alət olub-olmadığını yoxlayın. Yoxdursa, `"Bu alət yoxdur"` çap edin.
# 4. Kataloqa yeni alət əlavə edin: `"axtaris"` → `"İnternetdə axtarış edir"`.
# 5. Bu listdəki təkrarları **set** ilə silin və çap edin:
# `["hava", "tercume", "hava", "axtaris"]`


weather = {
    "hava" : "hava durumunu deyir",
    "tercume" : "Metni tercume edin"    
}


# for i, (key, value) in enumerate(weather.items(), start=1):
#     print(f"{i}. {key} → {value}")

# if weather.get("musiqi") in weather:
#     print("Bu alet var")
# else:
#     print("Bu alet yoxdur")

# weather["axtaris"] = "Internetde axtaris edin"
# print(weather)

# txt = ["hava", "tercume", "hava", "axtaris"]
# txt2 = set(txt)
# print(txt2)


