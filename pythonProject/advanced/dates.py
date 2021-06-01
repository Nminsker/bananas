
month_names = ["January", "February", "March", "April", "May", "June",
               "July", "August", "September", "October", "November", "December"]
month_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days_per_month_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
YEAR = 2021

month_to_days = {month: days_per_month[i] for i, month in enumerate(month_names)}
month_to_days_leap = {month: days_per_month_leap_year[i] for i, month in enumerate(month_names)}


def get_num_of_days_in_month(month_name, year):
    calender = month_to_days_leap if is_leap_year(year) else month_to_days
    return calender.get(month_name, "Month doesn't exist")


def get_following_month(month_name):
    loc = month_names.index(month_name)
    return month_names[(loc + 1) % 12]


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def validate_params(d, m, y):
    if not isinstance(d, int) or not isinstance(m, int) or not isinstance(y, int):
        raise ValueError("Date must be a number")
    if y <= 0:
        raise ValueError("Not a valid year")
    if 1 > m or m > 12:
        raise ValueError("Month must be a number in range 1-12")

    days = get_num_of_days_in_month(month_names[m-1], y)
    if 1 > d or d > days:
        raise ValueError("For the given month and year, the day should be of range 1-{0}".format(days))


class Date(object):
    def __init__(self, day, month, year):
        try:
            validate_params(day, month, year)
            self.day = day
            self.month = month
            self.year = year
        except ValueError as e:
            print("Could not process date - {0}".format(e))

    def __str__(self):
        return "{0}-{1}-{2}".format(self.day, self.month, self.year)

    def __eq__(self, other):
        return self.year == other.year and self.month == other.month and self.day == other.day

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year and self.month > other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day > other.day:
            return True
        else:
            return False

    def __ge__(self, other):
        return self >= other

    def __lt__(self, other):
        return other > self

    def __le__(self, other):
        return other >= self


class Calender(object):
    def __init__(self):
        self.events = {}

    def get_date(self, name):
        """ given event name returns the date """
        return self.events.get(name, 'Event does not exist')

    def add_event(self, name, date):
        """ Add a new event to the calender"""
        self.events[name] = date

    def is_event(self, date):
        """ Check if there exist an event in this date"""
        return date in self.events.values()

    def get_all_events_in_month(self, month):
        """ Retrieves all the events in a certain month"""
        if month > 12 or month < 1:
            "Not a valid month"
        return {k: v for k, v in self.events.items() if v.month == month} or "No events for month {0}".format(month)

    def print_calender(self):
        for k, v in self.events.items():
            print("{0} : {1}".format(k, str(v)))
