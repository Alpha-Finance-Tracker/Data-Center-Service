from datetime import datetime

from app.models.base_models.calendar import Calendar


class Week(Calendar):
    async def interval(self):
        return f"WEEK(date) = {datetime.now().isocalendar().week - 1}"
