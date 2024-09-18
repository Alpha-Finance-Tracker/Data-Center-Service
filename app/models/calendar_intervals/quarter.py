from calendar import Calendar
from datetime import datetime, timedelta

from sqlalchemy import func


class Quarter(Calendar):
    def interval(self):
        now = datetime.now()

        # Determine the start of the quarter
        quarter_start_month = (now.month - 1) // 3 * 3 + 1
        start_of_quarter = now.replace(month=quarter_start_month, day=1)

        # Determine the end of the quarter
        end_month = quarter_start_month + 2
        if end_month > 12:
            end_month -= 12
            end_year = now.year + 1
        else:
            end_year = now.year
        end_of_quarter = datetime(end_year, end_month, 1) - timedelta(days=1)

        return start_of_quarter, end_of_quarter
