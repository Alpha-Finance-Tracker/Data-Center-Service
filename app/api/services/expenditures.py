from app.database.models.expenditures import Expenditures
from app.models.base_models.periods import Periods


class ExpendituresService:

    def __init__(self, data):
        self.data = data

    async def display(self):
        data = await self.retrieve_data()
        output = {}
        try:
            for row in data:
                if row[0] == "":
                    output['Total'] = row[1]
                else:
                    output[row[0]] = row[1]
            return output
        except:
            return {}

    async def retrieve_data(self):
        period_instance = Periods(self.data.interval)
        time_period_condition = await period_instance.get_period()
        return await Expenditures().retrieve_data(self.data.column_type,self.data.category,time_period_condition)


    async def register(self, user_id):
        await update_query(
            'INSERT INTO expenditures(name,price,category,type,date,user_id) VALUES(%s,%s,%s,%s,%s,%s)',
            (self.data.name, self.data.price, self.data.category, self.data.expenditure_type, self.data.date, user_id))
        return {'message': 'Product added successfully'}
