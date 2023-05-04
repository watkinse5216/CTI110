def days_in_feb(user_year):
    if user_year % 4 == 0:
        if user_year % 100 == 0:
            if user_year % 400 == 0:
                return 29
            else:
                return 28
        else:
            return 29
    else:
        return 28

# Example usage:
if __name__ == '__main__':
    year = int(input(""))
    days = days_in_feb(year)
    print(f"{year} has {days} days in February.")
