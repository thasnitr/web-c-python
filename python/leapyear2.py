import datetime
curr_year=datetime.date.today().year
fin_year=int(input("Enter the final year:"))
if fin_year<curr_year:
    print("Final year must be greater than or equal to the current year")
else:
    print(f"Leap years from {curr_year} to {fin_year}")
    for year in range(curr_year,fin_year+1):
        if(year%4==0 and year%100!=0)or(year%400==0):
            print(year)
