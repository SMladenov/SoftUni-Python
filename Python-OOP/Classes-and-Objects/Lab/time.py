#Time

class Time:
    
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__ (self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time (self, hours, minutes, seconds):
        if 0 <= hours <= Time.max_hours:
            self.hours = hours
        if 0 <= minutes <= Time.max_minutes:
            self.minutes = minutes
        if 0 <= seconds <= Time.max_seconds:
            self.seconds = seconds

    def get_time (self):
        currentHours = ""
        currentMinutes = ""
        currentSeconds = ""
        
        if self.hours < 10:
            currentHours = f"0{self.hours}"
        else:
            currentHours = f"{self.hours}"
        if self.minutes < 10:
            currentMinutes = f"0{self.minutes}"
        else:
            currentMinutes = f"{self.minutes}"
        if self.seconds < 10:
            currentSeconds = f"0{self.seconds}"
        else:
            currentSeconds = f"{self.seconds}"
        return f"{currentHours}:{currentMinutes}:{currentSeconds}"


    def next_second(self):
        if self.seconds == 59:
            if self.minutes == 59:
                if self.hours < 23:
                    self.hours += 1
                elif self.hours == 23:
                    self.hours = 0
                self.minutes = 0
                self.seconds = 0
            else:
                self.minutes += 1
                self.seconds = 0
        else:
            self.seconds += 1

        return Time.get_time(self)
        
time = Time(9, 30, 59)

print(time.get_time())
print(time.next_second())

time = Time(10, 59, 59)

print(time.next_second())

time = Time(23, 59, 59)

print(time.next_second())
