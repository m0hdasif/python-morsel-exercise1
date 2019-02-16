import calendar
import datetime

# bonus 3: create Weekday object for weekday constants
Weekday = calendar

def meetup_date(year, month, nth=4, weekday=Weekday.THURSDAY):
    month_matrix = calendar.monthcalendar(year, month)

    # adjust nth by whether the first occurrence was in the first week
    if nth > 0 and month_matrix[0][weekday]:
        nth -= 1

    date = month_matrix[nth][weekday]
    if not date:
        date = month_matrix[nth - 1][weekday]
    return datetime.date(year, month, date)
