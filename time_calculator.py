def add_time(time, duration, today=""):

    def zero_f(digit):
        if len(digit) == 1:
            digit = '0' + digit

        return digit

    def convert_12_24(time):
        time = time.split()
        time[0] = time[0].split(':')
        hour = int(time[0][0])

        if time[1] == "AM":
            if hour == "12":
                time[0][0] = "00"
        else:
            if hour != "12":
                time[0][0] = str(hour + 12)

        return f"{time[0][0]}:{time[0][1]}"

    def convert_24_12(time):
        time = time.split(':')
        hour = int(time[0])
        if hour < 12:
            time.append("AM")
            if hour == 0:
                time[0] = "12"
        else:
            time.append("PM")
            if hour != 12:
                time[0] = str(hour - 12)

        return f"{time[0]}:{time[1]} {time[2]}"

    def day_after(today, day_passed):
        days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]

        # case insensitive
        today = today.lower()

        day_passed += days.index(today)
        day_passed = day_passed % 7

        return days[day_passed]

    def time_sum(time, duration):
        time = time.split(':')
        duration = duration.split(':')

        minute = int(time[1]) + int(duration[1])
        hour = int(time[0]) + int(duration[0])
        if minute > 59:
            minute = minute - 60
            hour += 1

        minute = zero_f(str(minute))
        hour = str(hour)

        return f"{hour}:{minute}"

    def show_day_passed(day_passed):
        if day_passed == 1:
            return "(next day)"
        else:
            return f"({day_passed} days later)"

    time = time_sum(convert_12_24(time), duration)
    time = time.split(':')

    day_passed = int(int(time[0]) / 24)
    time[0] = str(int(time[0]) % 24)
    time = f"{time[0]}:{time[1]}"

    time = convert_24_12(time)

    if day_passed > 0:
        if len(today) > 0:
            return f"{time}, {day_after(today, day_passed).capitalize()} {show_day_passed(day_passed)}"
        else:
            return f"{time} {show_day_passed(day_passed)}"
    else:
        if len(today) > 0:
            return f"{time}, {day_after(today, day_passed).capitalize()}"
        else:
            return time

def main():
    print(add_time("3:00 PM", "3:10"))
    # Returns: 6:10 PM
    print(add_time("11:30 AM", "2:32", "Monday"))
    # Returns: 2:02 PM, Monday
    print(add_time("11:43 AM", "00:20"))
    # Returns: 12:03 PM
    print(add_time("10:10 PM", "3:30"))
    # Returns: 1:40 AM (next day)
    print(add_time("11:43 PM", "24:20", "tueSday"))
    # Returns: 12:03 AM, Thursday (2 days later)
    print(add_time("6:30 PM", "205:12"))
    # Returns: 7:42 AM (9 days later)
    print(add_time("11:59 PM", "24:05", "Wednesday"))
