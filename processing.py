from models import forecast_db
from models import recipes_db, Menu, Recipe, Ingredients, Mealkit, MealkitIngredient
from peewee import Value, fn


def get_forecast(week):
    query = "select * from forecast where week='{w}';".format(w=week)
    cursor = forecast_db.execute_sql(query)
    result = []
    for row in cursor.fetchall():
        result.append({row[2]: row[4]})
    return result


def get_ingredient(week):
    menu = Menu.select(
        MealkitIngredient.sku,
        Ingredients.name,
        Ingredients.price,
        Value(0).alias('Volume'),
        fn.SUM(MealkitIngredient.qty_needed),
        Mealkit.slot
    )\
        .join(Mealkit)\
        .join(MealkitIngredient)\
        .join(Ingredients)\
        .where(
        (Menu.version == 2) & (Menu.week == '2018-W29')).group_by(Mealkit.slot).tuples()
    for m in menu:
        print(m)
    print(menu.__len__())
    print('done')
