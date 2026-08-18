kode = "DATA-2026-BDG"
print(kode[0:4])

print(kode[5:9])

print(kode[10:13])

print(kode[::-1])

data_mentah ="bandung,jakarta,surabaya"
kota_list = data_mentah.lower().split(",")
print(kota_list)

gabung = " - ".join(kota_list)
print(gabung)