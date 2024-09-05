from calendar import Calendar
from datetime import datetime

class Month(Calendar):

    async def interval(self):
        return f'MONTH(date) = {datetime.now().month}'