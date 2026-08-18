transaksi = [
    {"nama": "Sepatu", "harga": 250000, "stok": 5, "member": True},
    {"nama": "Baju", "harga": 80000, "stok": 0, "member": False},
    {"nama": "Celana", "harga": 150000, "stok": 2, "member": True},
    {"nama": "Topi", "harga": 40000, "stok": 10, "member": False}
]

print("=== 1. HASIL FILTER & KATEGORISASI TRANSAKSI ===")

for item in transaksi:

    if item["stok"] == 0:
        print(f"[-] {item['nama']}: Stok Habis! (Transaksi Dibatalkan)")
        continue  
    
    if item["harga"] >= 100000 and item["member"]:
        diskon = 0.20
        label_diskon = "Diskon Member VIP (20%)"

    elif item["harga"] >= 150000 or item["member"]:
        diskon = 0.10
        label_diskon = "Diskon Reguler (10%)"
    else:
        diskon = 0.0
        label_diskon = "Tanpa Diskon"

    total_bayar = item["harga"] * (1 - diskon)
    
    print(f"[+] {item['nama']} | Harga: Rp {item['harga']:,} | Status: {label_diskon} -> Bayar: Rp {total_bayar:,.0f}")


print("\n=== 2. LIST COMPREHENSION (PEMROSESAN CEPAT) ===")

barang_ready = [item["nama"] for item in transaksi if item["stok"] > 0]
print(f"Daftar barang siap jual: {barang_ready}")

harga_pajak = [item["harga"] * 1.11 for item in transaksi]
print(f"Daftar harga + Pajak 11%: {harga_pajak}")