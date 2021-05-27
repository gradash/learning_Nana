calculation_to_seconds = 24 * 60 * 60
name_of_unit = "seconds"


def days_to_seconds(number_of_days):
    print(f"{number_of_days} days are {number_of_days * calculation_to_seconds} {name_of_unit}")
    print("All Good!")


days_to_seconds(30)

