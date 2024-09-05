from calendar import Calendar


class Total(Calendar):
    async def interval(self):
        return f"date BETWEEN (SELECT MIN(date) FROM expenditures) AND (SELECT MAX(date) FROM expenditures)"
