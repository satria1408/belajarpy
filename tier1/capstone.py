SYSTEM_INFO = ("SYS-2026-BDG", "Serba Ada Mart", 1.0)
sys_id, toko_nama, versi = SYSTEM_INFO

raw_transactions = [
    {"trx_id": "TRX-001", "item": "  kopi susu ", "harga_str": "18000", "qty": 2, "vip": True},
    {"trx_id": "TRX-002", "item": "roti tawar", "harga_str": "15000", "qty": 0, "vip": False},  
    {"trx_id": "TRX-003", "item": "MIE INSTAN ", "harga_str": "3500", "qty": 10, "vip": False},
    {"trx_id": "TRX-004", "item": "keju keju", "harga_str": "25000", "qty": 1, "vip": True},
    {"trx_id": "TRX-005", "item": " KOPI SUSU", "harga_str": "18000", "qty": 1, "vip": False},
]

raw_customer_logs = [101, 104, 102, 101, 105, 104, 102, 108]

print(f"=== {toko_nama.upper()} (SYSTEM: {sys_id} v{versi}) ===")
print("=" * 55)

unique_customers = set(raw_customer_logs)
print(f"[*] Total Log Masuk : {len(raw_customer_logs)} pengunjung")
print(f"[*] Total Unique Customer: {len(unique_customers)} orang {unique_customers}\n")

processed_data = []
item_terjual_set = set()
total_omset = 0

print("=== DETAIL PEMROSESAN TRANSAKSI ===")

for trx in raw_transactions:

    item_clean = trx["item"].strip().lower()

    harga_int = int(trx["harga_str"])
    qty = trx["qty"]

    if qty <= 0:
        print(f"[-] [{trx['trx_id']}] Item '{item_clean}' Dibatalkan (Qty: 0)")
        continue
    
    subtotal = harga_int * qty
    
    if trx["vip"] and subtotal >= 30000:
        diskon_rate = 0.15  # Diskon VIP 15%
        status_diskon = "VIP Promo (15%)"
    elif trx["vip"] or subtotal >= 30000:
        diskon_rate = 0.05  # Diskon Regular 5%
        status_diskon = "Promo Regular (5%)"
    else:
        diskon_rate = 0.0
        status_diskon = "Tanpa Diskon"
        
    potongan = subtotal * diskon_rate
    total_bayar = subtotal - potongan
    
    total_omset += total_bayar
    
    item_terjual_set.add(item_clean.title())
    
    processed_data.append({
        "id": trx["trx_id"],
        "item": item_clean.title(),
        "total": total_bayar
    })
    
print(f"[+] [{trx['trx_id']}] {item_clean.title():<12} | Qty: {qty:<2} | {status_diskon:<18} -> Rp {total_bayar:,.0f}")

print("=" * 55)

print("=== RINGKASAN AKHIR TIER 1 ===")
print(f"1. Total Omset Bersih : Rp {total_omset:,.0f}")
print(f"2. Jenis Barang Laku  : {', '.join(item_terjual_set)}") 

big_transactions = [item["id"] for item in processed_data if item["total"] >= 30000]
print(f"3. ID Transaksi Besar : {big_transactions}")