import psycopg2
from datetime import date
from dotenv import dotenv_values
config = dotenv_values(".env")
def get_users() :
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname=config["DBNAME"], user=config["DBUSER"], password=config["DBPASSWORD"], host=config["DBHOST"])
        cur = conn.cursor()
        cur.execute("select email, password from users")
        users = cur.fetchall()
        cur.close()
        conn.close()
        return users
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')

def get_products():
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname=config["DBNAME"], user=config["DBUSER"], password=config["DBPASSWORD"], host=config["DBHOST"])
        cur = conn.cursor()
        cur.execute("select id, name, cost from products")
        products = cur.fetchall()
        cur.close()
        conn.close()
        return products
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')
def insert_request(product_id, phone_number, name):
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname=config["DBNAME"], user=config["DBUSER"], password=config["DBPASSWORD"], host=config["DBHOST"])
        cur = conn.cursor()
        query = f"insert into requests (product_id, phone_number, name) values ({product_id}, '{phone_number}', '{name}')"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        return "success"
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')
def insert_product(name, cost):
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname=config["DBNAME"], user=config["DBUSER"], password=config["DBPASSWORD"], host=config["DBHOST"])
        cur = conn.cursor()
        query = f"insert into products (name, cost) values ('{name}', {cost})"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        return "success"
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')
def del_product(id):
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname=config["DBNAME"], user=config["DBUSER"], password=config["DBPASSWORD"], host=config["DBHOST"])
        cur = conn.cursor()
        query = f"delete from products where id = {id}"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        return "success"
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')
def insert_log(event):
    try:
        # пытаемся подключиться к базе данных
        conn = psycopg2.connect(dbname=config["DBNAME"], user=config["DBUSER"], password=config["DBPASSWORD"], host=config["DBHOST"])
        cur = conn.cursor()
        today= date.today()
        query = f"insert into logs (event,dt) values ('{event}', '{today}')"
        cur.execute(query)
        conn.commit()
        cur.close()
        conn.close()
        return "success"
    except:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print('Can`t establish connection to database')
