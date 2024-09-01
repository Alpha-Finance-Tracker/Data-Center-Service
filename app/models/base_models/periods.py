from app.models.calendar_intervals.month import Month
from app.models.calendar_intervals.quarter import Quarter
from app.models.calendar_intervals.total import Total
from app.models.calendar_intervals.week import Week
from app.models.calendar_intervals.year import Year


class Periods:
    WEEK = 'Week'
    MONTH = 'Month'
    QUARTER = 'Quarter'
    YEAR = 'Year'
    TOTAL = 'Total'

    def __init__(self, interval):
        self.interval = interval
        self.calendar_map = {
            self.WEEK: self.week,
            self.MONTH: self.month,
            self.QUARTER: self.quarter,
            self.YEAR: self.year,
            self.TOTAL: self.total
        }

    @property
    def week(self):
        return Week().interval()

    @property
    def month(self):
        return Month().interval()

    @property
    def quarter(self):
        return Quarter().interval()

    @property
    def year(self):
        return Year().interval()

    @property
    def total(self):
        return Total().interval()

    def get_period(self):
        return self.calendar_map.get(self.interval)
