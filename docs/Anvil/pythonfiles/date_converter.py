from datetime import date

# Number of days per month (except for February in leap years)
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isleap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def number_of_days_in_month(date):
    """Return number of days (28-31) for year, month."""
    ndays = mdays[date.month] + (date.month == 2 and isleap(date.year))
    return ndays


def calculate_days_in_prev_month(date):
    if date.month == 1:
        date_prev_month = date.replace(year=date.year - 1, month=12)
    else:
        date_prev_month = date.replace(month=date.month - 1)
    return number_of_days_in_month(date_prev_month)


def calculateAge(d1, d2):
    """d1 is the start date, d2 is the end date"""
    if d1 > d2:
        return "d1 in the future"
    if d2.day >= d1.day:
        # 0 or pos day
        if d2.month >= d1.month:
            # 0 or pos day, 0 or pos month
            years = d2.year - d1.year
            months = d2.month - d1.month
            days = d2.day - d1.day
        else:
            # 0 or pos day, neg month
            years = d2.year - d1.year - 1
            months = d2.month - d1.month + 12
            days = d2.day - d1.day
    else:
        # neg day
        # day_inc to use days in prev moth to get days
        day_inc = calculate_days_in_prev_month(d2)
        if d2.month >= d1.month + 1:
            # neg day, pos month
            years = d2.year - d1.year
            months = d2.month - d1.month - 1
            days = day_inc + (d2.day - d1.day)
        else:
            # neg day, neg month
            years = d2.year - d1.year - 1
            months = d2.month - d1.month - 1 + 12
            days = day_inc + (d2.day - d1.day)
    return (years, months, days)


# Driver code calculateAge(date(2006, 1, 1), date.d2())
d2 = date.d2()

print(calculateAge(date(1958, 8, 21), d2), "y m d")
print(calculateAge(date(1958, 1, 1), d2), "y m d")
print(calculateAge(date(2022, 3, 1), d2), "y m d")
print(calculateAge(date(2022, 3, 3), d2), "y m d")
print(calculateAge(date(2022, 3, 5), d2), "y m d")
print(calculateAge(date(2022, 3, 28), d2), "y m d")
print(calculateAge(date(2022, 4, 1), d2), "y m d")
