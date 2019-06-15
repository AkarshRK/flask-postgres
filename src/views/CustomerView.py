#/src/views/CustomerView.py
from flask import request, g, Blueprint, json, Response
from ..shared.Authentication import Auth
from ..models.CustomerModel import CustomerModel, CustomerSchema

customer_api = Blueprint('customer_api', __name__)
customer_schema = CustomerSchema()


@customer_api.route('/', methods=['POST'])
@Auth.auth_required
def create():
  """
  Create Customer Function
  """
  req_data = request.get_json()
  # req_data['owner_id'] = g.user.get('id')
  data, error = customer_schema.load(req_data)
  if error:
    return custom_response(error, 400)
  post = CustomerModel(data)
  post.save()
  data = customer_schema.dump(post).data
  return custom_response(data, 201)

@customer_api.route('/', methods=['GET'])
@Auth.auth_required
def get_all():
  """
  Get All Customers
  """
  
  n = request.args.get("n",type=int)

  if n :
    posts = CustomerModel.get_n_customers(n)
  else:
    posts = CustomerModel.get_all_customers()

  data = customer_schema.dump(posts, many=True).data

  return custom_response(data, 200)

@customer_api.route('/<int:customer_id>', methods=['GET'])
@Auth.auth_required
def get_one(customer_id):
  """
  Get A Customer
  """
  post = CustomerModel.get_one_customer(customer_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = customer_schema.dump(post).data
  return custom_response(data, 200)

@customer_api.route('/<int:customer_id>', methods=['PUT'])
@Auth.auth_required
def update(customer_id):
  """
  Update A Customer
  """
  req_data = request.get_json()
  post = CustomerModel.get_one_customer(customer_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = customer_schema.dump(post).data
  if data.get('id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)
  
  data, error = customer_schema.load(req_data, partial=True)
  if error:
    return custom_response(error, 400)
  post.update(data)
  
  data = customer_schema.dump(post).data
  return custom_response(data, 200)

@customer_api.route('/<int:customer_id>', methods=['DELETE'])
@Auth.auth_required
def delete(customer_id):
  """
  Delete A Customer
  """
  post = CustomerModel.get_one_customer(customer_id)
  if not post:
    return custom_response({'error': 'post not found'}, 404)
  data = customer_schema.dump(post).data
  if data.get('id') != g.user.get('id'):
    return custom_response({'error': 'permission denied'}, 400)

  post.delete()
  return custom_response({'message': 'deleted'}, 204)
  

def custom_response(res, status_code):
  """
  Custom Response Function
  """
  return Response(
    mimetype="application/json",
    response=json.dumps(res),
    status=status_code
  )