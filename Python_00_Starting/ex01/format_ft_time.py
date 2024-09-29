import time as tm

seconds = tm.time()
print(f'Seconds since January 1, 1970: {seconds:,} or {seconds:.2e} in scientific notation')

current_date = tm.strftime("%b %d %Y")
print(current_date)
