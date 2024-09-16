from calendar import Calendar

from sqlalchemy import text


class Total(Calendar):
    def interval(self):
        return text("1=1")  # No filter, always true
