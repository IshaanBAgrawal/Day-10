def is_leap(yearss):
  if yearss % 4 == 0:
    if yearss % 100 == 0:
      if yearss % 400 == 0:
        return True
      else:
        return False
    else:
      return True
  else:
    return False

def days_in_month(years, months):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  months -= 1
  is_leap_year = is_leap(years)
  if is_leap_year == "Leap year." and months == 1:
    return month_days[months] + 1
  else:
    return month_days[months]



#🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
