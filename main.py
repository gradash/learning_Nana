calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_seconds(number_of_days):
    return f"{number_of_days} days are {number_of_days * calculation_to_seconds} {name_of_unit}"


user_input = input("Enter number of days: ")
user_input_cast_to_int = int(user_input)

calculated_value = days_to_seconds(user_input_cast_to_int)
print(calculated_value)
