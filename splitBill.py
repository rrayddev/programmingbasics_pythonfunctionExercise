#total bill
#number of people
#tip percentage

#required: final amount each person must pay

total_bill = float(input("Masukan Total Bill: "))
number_of_people = int(input("Jumlah Orang: "))
tip_percentage = float(input("Masukan Persentase Tip (%): "))

tip_percentage = tip_percentage / 100

#formula: total bill = ((total bill * tip percentage) + total bill ) / number of people

def total_each_person_must_pay(total_bill, number_of_people, tip_percentage):
    hasil = ((total_bill * tip_percentage) + total_bill)
    print("\n==============================")
    print("         STRUK TAGIHAN        ")
    print("==============================")
    print(f"Total Bill (+Tip) : Rp {hasil:,.0f}")
    print("------------------------------")
    return hasil / number_of_people

bayar = total_each_person_must_pay(total_bill, number_of_people, tip_percentage)
print(f"Bayar per Orang   : Rp {bayar:,.0f}")
print("==============================\n")