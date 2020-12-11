import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict


# first argument is blueprints name
# second argument is it's import_name
expense = Blueprint('expenses', 'expense')

@expense.route('/', methods=["GET"])
def get_all_expenses():
    try:
        expenses = [model_to_dict(expense) for expense in models.Expense.select()]
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