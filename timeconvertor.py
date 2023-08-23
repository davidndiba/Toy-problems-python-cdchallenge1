def convert_to_24_hour(hour, minute, period):
    if period == "pm" and hour != 12:
        hour += 12
    elif period == "am" and hour == 12:
        hour = 0

    hour_str = str(hour).zfill(2)  
    minute_str = str(minute).zfill(2)  

    return hour_str + minute_str

print(convert_to_24_hour(8, 30, "am"))  
print(convert_to_24_hour(8, 30, "pm"))  
print(convert_to_24_hour(12, 15, "am"))  
print(convert_to_24_hour(12, 15, "pm"))  