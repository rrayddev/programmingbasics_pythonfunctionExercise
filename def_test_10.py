def calculate_loyalty_points(total_transaction, member_status):
    loyalty_points = total_transaction // 20000
    if (member_status == False):
        loyalty_points = 0
    else:
        loyalty_points
    return loyalty_points
total_transaction = 60000
member_status = True
print("Poin member bertambah: ", calculate_loyalty_points(total_transaction, member_status))