INFO_TOKO = (-6.9175, 107.6191, "Toko Serba Ada")  # (Lat, Long, Nama)
lat, long, nama_toko = INFO_TOKO  # Tuple Unpacking

print(f"=== BANNER SYSTEM: {nama_toko.upper()} ===")
print(f"Lokasi GPS: {lat}, {long}\n")

raw_visitor_ids = [101, 105, 102, 101, 108, 105, 102, 110]

unique_visitors = set(raw_visitor_ids)
print("=== 1. FILTERING DATA PENGUNJUNG (SET & LIST) ===")
print(f"Total Log Kunjungan : {len(raw_visitor_ids)} transaksi")
print(f"Pengunjung Unik (Set): {unique_visitors}")
print(f"Jumlah Pembeli Asli  : {len(unique_visitors)} orang\n")

katalog_produk = [
    {"id": "P01", "nama": "Kopi Hitam", "harga": 15000, "tag": {"minuman", "dingin", "kafein"}},
    {"id": "P02", "nama": "Roti Bakar", "harga": 20000, "tag": {"makanan", "manis", "hangat"}},
    {"id": "P03", "nama": "Es Teh Manis", "harga": 8000, "tag": {"minuman", "dingin", "manis"}}
]

print("=== 2. MANIPULASI KATALOG PRODUK (DICTIONARY) ===")
katalog_produk.append({
    "id": "P04", 
    "nama": "Cireng", 
    "harga": 10000, 
    "tag": {"makanan", "gurih", "hangat"}
})

for produk in katalog_produk:
    
    if "makanan" in produk["tag"]:
        produk["harga_promo"] = int(produk["harga"] * 0.9)
    else:
        produk["harga_promo"] = produk["harga"]

    print(f"[{produk['id']}] {produk['nama']} | Normal: Rp {produk['harga']:,} -> Promo: Rp {produk['harga_promo']:,}")

print("\n=== 3. OPERASI HIMPUNAN TAG (SET MATH) ===")
tag_p01 = katalog_produk[0]["tag"]  
tag_p03 = katalog_produk[2]["tag"] 
tag_sama = tag_p01.intersection(tag_p03)
print(f"Kemiripan antara '{katalog_produk[0]['nama']}' & '{katalog_produk[2]['nama']}': {tag_sama}")