from calendar import Calendar
from datetime import datetime


class Quarter(Calendar):
    def interval(self):
        return f"QUARTER(date) = {(datetime.now().month -1 ) // 3 + 1}"
