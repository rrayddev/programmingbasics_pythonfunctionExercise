#diskon 15 rebu kalo punya kode "NONTONSERU" dan minimal beli 2 tiket
#buat fungsi dengan parameter: total_prices ticket_quantity, coupon_code.

ticket_prices = float(input("Harga Tiket (Rp): "))
ticket_quantity = int(input("Jumlah Tiket: "))
coupon_code = input("Masukan Kode Kupon: ")

coupon_code = coupon_code.upper()

def check_discount(ticket_prices, ticket_quantity, coupon_code):
    if ticket_quantity >= 2 and coupon_code == "NONTONSERU":
        total_ticket_prices = (ticket_prices * ticket_quantity) - 15000
        return total_ticket_prices
    else:
        total_ticket_prices = ticket_prices * ticket_quantity
        return total_ticket_prices
    

final_prices = check_discount(ticket_prices, ticket_quantity, coupon_code)
subtotal_normal = ticket_prices * ticket_quantity
potongan_diskon = subtotal_normal - final_prices

if coupon_code == "":
    status_kupon = "Tidak Menggunakan Kupon"
elif coupon_code == "NONTONSERU" and ticket_quantity >= 2:
    status_kupon = "Promo Berhasil Digunakan!"
elif coupon_code == "NONTONSERU" and ticket_quantity < 2:
    status_kupon = "Gagal: Minimal Pembelian 2 Tiket"
else:
    status_kupon = "Gagal: Kode Kupon Salah/Tidak Valid"

print("\n==========================================")
print("             CINEMA TICKET                ")
print("==========================================")
print(f"Harga / Tiket : Rp {ticket_prices:>10,.0f}")
print(f"Jumlah Tiket  : {ticket_quantity:>10} Tiket")
print("------------------------------------------")
print(f"Subtotal      : Rp {subtotal_normal:>10,.0f}")

if potongan_diskon > 0:
    print(f"Promo ({coupon_code}) : Rp -{potongan_diskon:>9,.0f}")

print("------------------------------------------")
print(f"TOTAL BAYAR   : Rp {final_prices:>10,.0f}")
print("==========================================")
print(f"Status Kupon  : {status_kupon}") 
print("==========================================")
print("       NIKMATI FILM ANDA & ENJOY!         ")
print("==========================================\n")