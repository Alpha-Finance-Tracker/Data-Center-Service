from calendar import Calendar
from datetime import datetime


class Quarter(Calendar):
    async def interval(self):
        return f"QUARTER(date) = {(datetime.now().month - 1) // 3 + 1}"
