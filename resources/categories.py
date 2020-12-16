import models

from flask import Blueprint, jsonify, request

from playhouse.shortcuts import model_to_dict


# first argument is blueprints name
# second argument is it's import_name
category = Blueprint('categories', 'category')


# This will get categories for categorizing expenses
@category.route('/', methods=["GET"])
def get_all_categories():
    try:
        categories = [model_to_dict(category) for category in models.Category.select()]
        print(categories)
        return jsonify(data=categories, status={"code": 200, "message": "Success"})
    except models.DoesNotExist:
        return jsonify(data={}, status={"code": 401, "message": "Error getting the resources"})


