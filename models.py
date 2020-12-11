from peewee import *
import datetime

# Connect to a Postgres database.
DATABASE = PostgresqlDatabase('flask_expense_tracker', host='localhost', port=5432)

class Expense(Model):
    exp_date = DateField()
    exp_descr = CharField()
    exp_amt = IntegerField()
    exp_comment = CharField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Expense], safe=True)
    print("TABLES Created")
    DATABASE.close()