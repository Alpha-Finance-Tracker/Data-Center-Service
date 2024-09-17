from app.database.models.expenditures import Expenditures
from app.models.base_models.periods import Periods


class ExpendituresService:

    def __init__(self, data):
        self.data = data

    async def display(self):
        data = await self.retrieve_data()
        print(f"Received data {data}")
        output = {}
        try:
            for row in data:
                if row[0] == "":
                    output['Total'] = row[1]
                else:
                    output[row[0]] = row[1]
            print(f"sending data {output}")
            return output
        except:
            return {}

    async def retrieve_data(self):
        period_instance = Periods(self.data.interval)
        time_period_condition = await period_instance.get_period()
        return await Expenditures().retrieve_data(self.data.column_type,self.data.category,time_period_condition)


    async def register(self, user_id):
        new_expenditure = Expenditures(name=self.data.name,price=self.data.price,
                                       category=self.data.category,
                                       expenditure_type=self.data.expenditure_type,
                                       date=self.data.date,user_id=user_id)

        await Expenditures().register(new_expenditure)

        return {'message': 'Product added successfully'}
