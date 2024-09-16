from calendar import Calendar
from datetime import datetime

from sqlalchemy import func


class Month(Calendar):

    def interval(self):
        now = datetime.now()
        return func.extract('month', func.now()) == now.month