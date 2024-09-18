from calendar import Calendar
from datetime import datetime, timedelta

from sqlalchemy import func


class Month(Calendar):

    def interval(self):
        now = datetime.now()
        start_of_month = now.replace(day=1)

        # Calculate the end of the month
        next_month = start_of_month.replace(day=28) + timedelta(days=4)  # Move to the next month
        end_of_month = next_month - timedelta(days=next_month.day)

        return start_of_month, end_of_month