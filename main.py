from flask import Flask
from models import recipes_db, Menu, Recipe, Ingredients, Mealkit, MealkitIngredient
from processing import get_forecast, get_ingredient
app = Flask(__name__)


@app.route('/get')
def main():
    for menu in Menu.select():
        print(menu)
    return 'Hello, World!'



@app.route('/test')
def get_test():
    # result = get_forecast('2018-W29') # {slot:number}
    # for x in result:
    #     print(x)
    result = get_ingredient('2018-W29')
    return 'Test'


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
