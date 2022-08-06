import ujson

with open('company/config.json') as f:
    company_settings = ujson.load(f)
with open('employee/config.json') as f:
    employee_settings = ujson.load(f)
with open('order/config.json') as f:
    order_settings = ujson.load(f)
with open('product/config.json') as f:
    product_settings = ujson.load(f)
with open('customer/config.json') as f:
    customer_settings = ujson.load(f)