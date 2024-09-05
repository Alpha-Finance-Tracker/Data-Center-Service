from calendar import Calendar
from datetime import datetime


class Year(Calendar):
    def interval(self):
        return f"YEAR(date) = {datetime.now().year}"
