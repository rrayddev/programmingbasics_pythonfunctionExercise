def create_username(full_name, birth_year):
    first_name = full_name.split()[0].lower()
    last_two_digits = str(birth_year)[-2:]
    return first_name + last_two_digits
full_name = "Regith Rayabi"
birth_year = 2007
print(create_username(full_name, birth_year))