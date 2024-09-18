from calendar import Calendar
from datetime import datetime

from sqlalchemy import func


class Year(Calendar):
    def interval(self):
        now = datetime.now()
        start_of_year = now.replace(month=1, day=1)
        end_of_year = now.replace(month=12, day=31)
        return start_of_year, end_of_year
