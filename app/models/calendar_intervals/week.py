from datetime import datetime, timedelta

from sqlalchemy import func

from app.models.base_models.calendar import Calendar


class Week(Calendar):
    def interval(self):
        now = datetime.now()
        start_of_week = now - timedelta(days=(now.weekday() + 1) % 7)  # Monday
        end_of_week = start_of_week + timedelta(days=6)  # Sunday
        return start_of_week, end_of_week
