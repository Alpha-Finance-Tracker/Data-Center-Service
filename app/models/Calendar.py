from abc import ABC,abstractmethod
from datetime import datetime


class Calendar(ABC):
    @abstractmethod
    def interval(self):
        pass

class Week(Calendar):
    def interval(self):
        return f"WEEK(date) = {datetime.now().isocalendar().week -1}"

class Month(Calendar):
    def interval(self):
        return f'MONTH(date) = {datetime.now().month}'


class Quarter(Calendar):
    def interval(self):
        return f"QUARTER(date) = {(datetime.now().month -1 ) // 3 + 1}"


class Year(Calendar):
    def interval(self):
        return f"YEAR(date) = {datetime.now().year}"

class Total(Calendar):
    def interval(self):
        return f"date BETWEEN (SELECT MIN(date) FROM expenditures) AND (SELECT MAX(date) FROM expenditures)"




def interval_selector(interval):
    if interval == 'Week':
        return Week()
    if interval == 'Month':
        return Month()
    if interval == 'Quarter':
        return Quarter()
    if interval == 'Year':
        return Year()
    if interval == 'Total':
        return Total()

