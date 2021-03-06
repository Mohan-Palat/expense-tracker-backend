from peewee import *
import datetime

# Connect to a Postgres database.
DATABASE = PostgresqlDatabase('flask_expense_tracker', host='localhost', port=5432)

class Expense(Model):
    exp_date = DateField()
    exp_descr = CharField()
    exp_amt = IntegerField()
    # exp_amt = DecimalField(13,2)
    exp_category = CharField()
    # exp_comment = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

class Category(Model):
    category = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Expense, Category], safe=True)
    print("TABLES Created")
    DATABASE.close()