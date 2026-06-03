# parameters: street, city, province, and postal_code
# required: return format address string (not just print)

street = input("Input Alamat: ")
city = input("Input Nama Kota: ")
province = input("Input Provinsi: ")
postal_code = input("Input Kode Pos: ")

def format_address(street, city, province, postal_code):
    address = (
        f"Alamat      : {street.title()}\n"
        f"Kota        : {city.title()}\n"
        f"Provinsi    : {province.title()}\n"
        f"Kode Pos    : {postal_code}"
    )
    return address

full_address = format_address(street, city, province, postal_code)
print("\n==========================================")
print("             LABEL PENGIRIMAN             ")
print("==========================================")
print(full_address)
print("==========================================\n")