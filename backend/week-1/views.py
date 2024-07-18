from flask import request, Blueprint, jsonify
from models import add_product, get_product, alter_product, remove_product

product_bp = Blueprint('Products', __name__,url_prefix='/products')

@product_bp.route('/')
def product():
    return "<h1>Products</h1>"

@product_bp.route('/create',methods = ['GET','POST'])
def create_product():
    if(request.method=="POST"):
        item_sku = request.form['item_sku']
        item_name = request.form['item_name']
        item_description = request.form['item_description']
        item_price = request.form['item_price']
        item_qty = request.form['item_qty']

        res = add_product(item_sku,item_name,item_description,item_price,item_qty)
        if(res):
            return jsonify({'error':'already exists',"message":res})
        return jsonify({"message":'created succesfully'})

    return "<h1>Products create</h1>"


@product_bp.route('/read')
def read_product():
    item_sku = request.args.get('item_sku', default=None, type=int)
    items = get_product(item_sku)
    return jsonify(items)

@product_bp.route('/update', methods = ['GET','PUT'])
def update_product():
    if(request.method=="PUT"):
        item_sku = request.args.get('item_sku',type=int)
        item_col = request.form['column']
        item_value = request.form['value']
        res = alter_product(item_sku,item_col,item_value)
        return jsonify(res)
    return "<h1>Products update</h1>"

@product_bp.route('/delete', methods = ['GET','DELETE'])
def delete_product():
    if(request.method=="DELETE"):
        item_sku = request.form['item_sku']
        res = remove_product(item_sku)
        return jsonify(res)
    return "<h1>Products delete</h1>"
