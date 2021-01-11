from flask import Flask
from pymongo import MongoClient
from random import randint
import time
from flask_caching import Cache

app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/main')
@cache.cached(timeout=20)
def main():
    client = MongoClient(host = "mongo", port=27017)
    db = client.test

    names = ['Kitchen', 'Animal', 'State', 'Tastey', 'Big', 'City', 'Fish', 'Pizza', 'Goat', 'Salty', 'Sandwich',
             'Lazy', 'Fun']
    company_type = ['LLC', 'Inc', 'Company', 'Corporation']
    company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']

    business = {
        'name': names[randint(0, (len(names) - 1))] + ' ' + names[randint(0, (len(names) - 1))] + ' ' + company_type[
            randint(0, (len(company_type) - 1))],
        'rating': randint(1, 5),
        'cuisine': company_cuisine[randint(0, (len(company_cuisine) - 1))],
        'insert_ts': time.time()
    }

    result = db.testschema.insert_one(business)

    msg = """1 row is inserted
    Data inserted: {business} 
    Count of documents: {cnt}
    """.format(cnt = db.testschema.count_documents({}), business = business)

    return msg

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


