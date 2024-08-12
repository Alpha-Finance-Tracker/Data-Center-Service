from datetime import datetime

from app.data.database import update_query, read_query



async def register_receipt_in_db(foods,date):
    event_date =datetime.strptime(date, '%d.%m.%Y').date()
    for n,p in foods.items():
        update_query('INSERT INTO expenditures(name,price,date,user_id) VALUES(%s,%s,%s, %s)',(n,p,event_date, 8))

async def get_category_expenditures_from_db(start_date,end_date,category,type):

    if category and type :
        products =  read_query('SELECT name,price FROM expenditures WHERE  category = %s AND type = %s AND date BETWEEN %s AND %s', (category,type,start_date,end_date))
        total_spent = read_query('SELECT SUM(price) FROM expenditures WHERE category = %s AND type = %s AND date BETWEEN %s AND %s',(category,type,start_date,end_date) )
        return {f"Monthly Total Spent {total_spent[0][0]} BGN": products}

    if type :
        products = read_query('SELECT name,price FROM expenditures WHERE type = %s AND date BETWEEN %s AND %s',
                              (type, start_date, end_date))
        total_spent = read_query('SELECT SUM(price) FROM expenditures WHERE type = %s AND  date BETWEEN %s AND %s',
                                 (type, start_date, end_date))
        return {f"Monthly Total Spent {total_spent[0][0]} BGN": products}

    if category:
        products = read_query('SELECT name,price FROM expenditures WHERE  category = %s AND date BETWEEN %s AND %s',
                              ('food', start_date, end_date))
        total_spent = read_query('SELECT SUM(price) FROM expenditures WHERE category = %s AND  date BETWEEN %s AND %s',
                                 ('food', start_date, end_date))
        return {f"Monthly Total Spent {total_spent[0][0]} BGN": products}



async def add_expenditure_into_db(name,price,category,type,date,token):
    event_date = datetime.strptime(date, '%d.%m.%Y').date()
    update_query('INSERT INTO expenditures(name,price,category,type,date,user_id) VALUES(%s,%s,%s,%s,%s,%s)',(name,price,category,type,event_date, token.get("user_id")))
    return "Product added successfully "

