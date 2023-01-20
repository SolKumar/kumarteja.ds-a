def timeConversion(s:str):
    """Accepts time string in 12 hours and returns the string in 24 hour format"""
    # Write your code here
    hours = int(s[0:2])
    minutes = int(s[3:5])
    seconds = int(s[6:8])
    if ( hours < 0 or hours > 12 ) or ( minutes < 0 or minutes > 60 ) or ( seconds < 0 or seconds > 60 ):
        raise ValueError("Time not as per required format")
    end = s[-2::]
    militay_time = ""
    if end == "AM" and hours == 12:
         militay_time = "00" + s[2:-2]
    elif end == "PM" and hours != 12:
        militay_time = str(int(s[0:2]) + 12) + s[2:-2]
    else: # AM and for 12 PM
        militay_time = s[:-2]
    return militay_time

time = "12:48:36AM"
print(f"Time in 12H format:{time}\nTime in 24H format:{timeConversion(time)}")