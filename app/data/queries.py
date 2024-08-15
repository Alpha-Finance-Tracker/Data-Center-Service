from datetime import datetime

from app.data.database import update_query, read_query



async def register_receipt_in_db(foods,date):
    event_date =datetime.strptime(date, '%d.%m.%Y').date()
    for n,p in foods.items():
        update_query('INSERT INTO expenditures(name,price,date,user_id) VALUES(%s,%s,%s, %s)',(n,p,event_date, 8))

async def get_expenditures_from_db(start_date,end_date,category,type):

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

async def category_expenditures_from_db():
    data =  read_query('SELECT category,  ROUND(SUM(price), 2) as total_price FROM expenditures GROUP BY category ORDER BY total_price DESC')

    output = {}
    for row in data:
        if row[0] == "":
            output['Total'] = row[1]
        else:
            output[row[0]] = row[1]

    return output


async def food_expenditures_from_db():
    data = read_query(
        'SELECT type,  ROUND(SUM(price), 2) as total_price FROM expenditures WHERE category = %s GROUP BY type ORDER BY total_price DESC',("Food",))
    output = {}

    for row in data:
        if row[0] in output:
            output[row[0]] += row[1]
        output[row[0]] = row[1]


    return output