from datetime import datetime

from app.data.database import update_query, read_query


async def register_foods_in_db(foods,date):
    event_date =datetime.strptime(date, '%d.%m.%Y').date()
    for n,p in foods.items():
        update_query('INSERT INTO products(name,price,date,user_id) VALUES(%s,%s,%s, %s)',(n,p,event_date, 8))



async def add_product_into_db(name,price,type,date):
    event_date = datetime.strptime(date, '%d.%m.%Y').date()
    update_query('INSERT INTO products(name,price,date,user_id) VALUES(%s,%s,%s,%s,%s)',(name,price,type,event_date, 8))


async def get_expenditures_from_db(month):
    products =  read_query('SELECT name,price FROM products WHERE MONTH(date) = %s', (month,))
    total_spent = read_query('SELECT SUM(price) FROM products WHERE MONTH(date) = %s',(month,) )
    return {f"Monthly Total Spent {total_spent[0][0]} BGN": products}









































