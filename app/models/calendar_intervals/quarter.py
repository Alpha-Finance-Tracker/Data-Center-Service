from calendar import Calendar
from datetime import datetime

from sqlalchemy import func


class Quarter(Calendar):
    def interval(self):
        now = datetime.now()
        quarter = (now.month - 1) // 3 + 1
        return func.extract('quarter', func.now()) == quarter
