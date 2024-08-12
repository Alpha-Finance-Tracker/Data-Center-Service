from datetime import datetime

from app.data.database import update_query, read_query



async def add_entertainment_into_db(name,price,category,type,date,token):
    event_date = datetime.strptime(date, '%d.%m.%Y').date()
    update_query('INSERT INTO expenditures(name,price,category,date,user_id) VALUES(%s,%s,%s,%s,%s)',(name,price,category,event_date, token.get("user_id")))
    return "Product added successfully "

async def get_entertainment_expenditures_from_db(start_date,end_date):
    products =  read_query('SELECT name,price FROM expenditures WHERE  category = %s AND date BETWEEN %s AND %s', ('food',start_date,end_date))
    total_spent = read_query('SELECT SUM(price) FROM expenditures WHERE category = %s AND  date BETWEEN %s AND %s',('food',start_date,end_date) )
    return {f"Monthly Total Spent {total_spent[0][0]} BGN": products}





