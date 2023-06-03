def timeConversion(s):
    # Split the s into components
    hour, minute, second = s.split(":")
    # Extract the AM/PM component
    am_pm = second[-2:]
    # Remove the AM/PM component from the second component
    second = second[:-2]
    # Convert the hour component to an integer
    hour = int(hour)
    # If the s is in PM and the hour component is not 12, add 12 to the hour component
    if am_pm == "PM" and hour != 12:
        hour += 12
    # If the s is 12 AM, set the hour component to 0
    elif hour == 12 and am_pm == "AM":
        hour = 0
    # Return the s in military (24-hour) format
    # return f"{hour:02f}:{minute:02f}:{second:02f}"
    return f"{hour:02d}:{minute}:{second}"

military_time = timeConversion("5:34:56PM")
print(military_time)  # Outputs "12:34:56"
