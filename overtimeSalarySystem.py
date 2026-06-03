# parameter: 1) base_salary 2) total_hours_worked
# jika total hour melebihi 40, hitung jam extra, kalikan 50.000 dan tambahkan hasil ke base salary
# jika tidak ada overtime, hanya menerima base salary
# formula: ((total jam kerja - 40) * 50000) + base salary

base_salary = float(input("Masukan Gaji Dasar: "))
total_hours_worked = float(input("Masukan Total Jam Kerja dalam Seminggu: "))


def total_salary(base_salary, total_hours_worked):
    if total_hours_worked > 40:
        total_extra_hour = total_hours_worked - 40
        hasil_lembur = (total_extra_hour* 50000)
        print("\n=======================================")
        print("              SLIP GAJI                ")
        print("=======================================")
        print(f"Gaji Pokok         : Rp {base_salary:}")
        print(f"Total Jam Kerja    : {total_hours_worked} Jam")
        print(f"Bonus Lembur       : Rp {hasil_lembur:,}")
        print("---------------------------------------")
        return base_salary + hasil_lembur
    else:
        print("\n=======================================")
        print("              SLIP GAJI                ")
        print("=======================================")
        print(f"Gaji Pokok         : Rp {base_salary:,}")
        print(f"Total Jam Kerja    : {total_hours_worked} Jam")
        print(f"Bonus Lembur       : Rp 0 (Tidak Lembur)")
        print("---------------------------------------")
        return base_salary

total_gaji = total_salary(base_salary, total_hours_worked)
print(f"TOTAL GAJI BERSIH  : Rp {total_gaji:,}")
print("=======================================\n")
