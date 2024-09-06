from app.database import read_query, update_query
from app.models.base_models.periods import Periods


class Expenditures:

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
        except Exception as e:
            print('No data found')
            return {}


    async def register(self, user_id):
        await update_query(
            'INSERT INTO expenditures(name,price,category,type,date,user_id) VALUES(%s,%s,%s,%s,%s,%s)',
            (self.data.name, self.data.price, self.data.category, self.data.expenditure_type, self.data.date, user_id))
        return {'message':'Product added successfully'}

    async def retrieve_data(self):
        time_period = await Periods(self.data.interval).get_period()

        if self.data.category:
            return await read_query(f"""
                           SELECT {self.data.column_type}, ROUND(SUM(price), 2) as total_price
                           FROM expenditures
                           WHERE category = %s AND {time_period}
                           GROUP BY {self.data.column_type}
                           ORDER BY total_price DESC """,(self.data.category,))
        else:
            return await read_query(f"""
                           SELECT category, ROUND(SUM(price), 2) as total_price
                           FROM expenditures
                           WHERE {time_period}
                           GROUP BY category
                           ORDER BY total_price DESC""")
