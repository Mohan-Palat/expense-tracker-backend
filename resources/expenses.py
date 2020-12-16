import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict


# first argument is blueprints name
# second argument is it's import_name
expense = Blueprint('expenses', 'expense')

@expense.route('/', methods=["GET"])
def get_all_expenses():
    try:
        expenses = [model_to_dict(expense) for expense in models.Expense.select().order_by(models.Expense.exp_date.desc())]
        # how to put a where clause in SQL
        # expenses = [model_to_dict(expense) for expense in models.Expense.select().where(models.Expense.exp_date > '2020-12-10' and models.Expense.exp_date < '2020-12-14)]
        # expenses = [model_to_dict(expense) for expense in models.Expense.select(fn.SUM(models.Expense.exp_amt))]
        print(expenses)
        return jsonify(data=expenses, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})

@expense.route('/', methods=["POST"])
def create_expenses():
    payload = request.get_json()
    print(type(payload), 'payload')
    expense = models.Expense.create(**payload)
    print(expense.__dict__)
    print(dir(expense))
    print(model_to_dict(expense), 'model to dict')
    expense_dict = model_to_dict(expense)
    return jsonify(data=expense_dict, status={"code": 201, "message": "Success"})

# UPDATE route
@expense.route('/<id>', methods=["PUT"])
def update_song(id):
    payload = request.get_json()
    query = models.Expense.update(**payload).where(models.Expense.id==id)
    query.execute()
    return jsonify(data=model_to_dict(models.Expense.get_by_id(id)), status={"code": 200, "message": "resource updated successfully"})

# DELETE route
@expense.route('/<id>', methods=["Delete"])
def delete_expense(id):
    query = models.Expense.delete().where(models.Expense.id==id)
    query.execute()
    return jsonify(data='resource successfully deleted', status={"code": 200, "message": "resource deleted successfully"})