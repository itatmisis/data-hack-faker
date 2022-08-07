import ujson, os

path = os.path.dirname(os.path.realpath(__file__))


with open(path + "/company/config.json") as f:
    company_settings = ujson.load(f)
with open(path + "/employee/config.json") as f:
    employee_settings = ujson.load(f)
with open(path + "/order/config.json") as f:
    order_settings = ujson.load(f)
with open(path + "/product/config.json") as f:
    product_settings = ujson.load(f)
with open(path + "/customer/config.json") as f:
    customer_settings = ujson.load(f)
