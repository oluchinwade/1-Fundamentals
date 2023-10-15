inches_snow = {"Monday": 2, "Tuesday": 4, "Wednesday": 5}

def print_total_snaowfall(inches_snow):
    total_inches = 0
    for snow in inches_snow:
        total_inches = inches_snow[snow] + total_inches
    print(f'Total snowfall inches: {total_inches}')

print_total_snaowfall(inches_snow)
inches_snow["Thursday"] = int(input("How many inches of snow fell on Thursday?  "))

print_total_snaowfall(inches_snow)