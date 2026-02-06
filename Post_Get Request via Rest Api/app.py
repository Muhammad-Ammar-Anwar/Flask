from flask import Flask,jsonify,request

app = Flask(__name__)


product = [
        {"id":1,"name":"keyboard","price" : 49.95},
        {"id":2,"name":"mouse","price" : 29.95},
        {"id":3,"name":"speaker","price" : 99.95}
    ]


@app.route("/")
def home():
    return jsonify({"message":"Hello from our first flask Server"})




@app.route("/products", methods=['GET'])
def get_products():
    return jsonify(product)

@app.route("/products",methods=["POST"])
def add_product():
    data = request.get_json()
    new_product = {
        "id":len(product) + 1,
        "name": data.get("name"),
        "price" : data.get("price")
    }
    product.append(new_product)

    return jsonify({"message": "Product added", "product" : new_product}), 201



if __name__ == "__main__":
    app.run(debug=True)