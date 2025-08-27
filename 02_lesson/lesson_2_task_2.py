def is_year_leap(year):
    return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
y = int(input("year: "))
print(is_year_leap(y))