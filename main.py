calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_seconds(number_of_days, custom_message):
    print(f"{number_of_days} days are {number_of_days * calculation_to_seconds} {name_of_unit}")
    print(custom_message)


def scope_check(number_of_days):
    my_var = "variable defined inside function"
    print(name_of_unit)
    print(number_of_days)
    print(my_var)


days_to_seconds(10, "All Good!")
days_to_seconds(30, "It' Works!")

scope_check(22)


