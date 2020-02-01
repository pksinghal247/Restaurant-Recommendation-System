from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/aboutUs')
def aboutUs():
    return render_template("AboutUs.html")

@app.route('/analysis')
def analysis():
    return render_template("analysis.html")

@app.route('/recommend', methods=['POST'])
def predict():
    city = request.form['city']
    cuisines = request.form['cuisines']

    from pymongo import MongoClient

    # create connection with mongo server
    client = MongoClient('mongodb://localhost:27017')

    # get the database
    db = client['banglore']

    # get the collection
    data = db['data']

    # execute find() on collection & get cursor
    criteria = {'city': f'{city}', 'Sentiment': 'Positive', 'cuisines': f'{cuisines}'}
    cur = data.find(criteria).sort('Rating', -1)

    list = []
    for val in cur:
        dict = {}
        dict['Name'] = val['name']
        dict['Address'] = val['address']
        dict['online_order'] = val['online_order']
        dict['book_table'] = val['book_table']
        dict['rate'] = val['rate']
        dict['cost'] = val['cost']
        dict['phone'] = val['phone']
        dict['cuisines'] = val['cuisines']
        dict['dish_liked'] = val['dish_liked']
        list.append(dict)
    if len(list) == 0:
        criteria = {'city': f'{city}', 'Sentiment': 'Neutral', 'cuisines': f'{cuisines}'}
        cur = data.find(criteria).sort('Rating', -1)
        for val in cur:
            dict = {}
            dict['Name'] = val['name']
            dict['Address'] = val['address']
            dict['online_order'] = val['online_order']
            dict['book_table'] = val['book_table']
            dict['rate'] = val['rate']
            dict['cost'] = val['cost']
            dict['phone'] = val['phone']
            dict['cuisines'] = val['cuisines']
            dict['dish_liked'] = val['dish_liked']
            list.append(dict)
    if len(list) == 0:
        criteria = {'city': f'{city}', 'Sentiment': 'Negative', 'cuisines': f'{cuisines}'}
        cur = data.find(criteria).sort('Rating', -1)
        for val in cur:
            dict = {}
            dict['Name'] = val['name']
            dict['Address'] = val['address']
            dict['online_order'] = val['online_order']
            dict['book_table'] = val['book_table']
            dict['rate'] = val['rate']
            dict['cost'] = val['cost']
            dict['phone'] = val['phone']
            dict['cuisines'] = val['cuisines']
            dict['dish_liked'] = val['dish_liked']
            list.append(dict)
    return render_template('result.html',len=len(list) , dict=list)


app.run(port=5000, host='0.0.0.0')