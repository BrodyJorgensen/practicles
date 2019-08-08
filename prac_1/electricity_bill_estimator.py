cent_per_KWH = int(input("how much doe it cost "))
daily_usage = float(input("what is the daily usage "))
number_of_days = int(input("how many days is it used "))
print("estinated bill: ${:.2f}".format((cent_per_KWH /100) * daily_usage * number_of_days))