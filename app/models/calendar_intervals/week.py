from datetime import datetime

from sqlalchemy import func

from app.models.base_models.calendar import Calendar


class Week(Calendar):
    def interval(self):
        now = datetime.now()
        return func.extract('week', func.now()) == now.isocalendar().week - 1
