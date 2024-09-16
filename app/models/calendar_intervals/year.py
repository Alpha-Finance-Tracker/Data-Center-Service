from calendar import Calendar
from datetime import datetime

from sqlalchemy import func


class Year(Calendar):
    def interval(self):
        now = datetime.now()
        return func.extract('year', func.now()) == now.year
