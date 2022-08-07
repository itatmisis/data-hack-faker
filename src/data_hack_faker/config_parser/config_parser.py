from pathlib import Path

import ujson as json

path = Path("./configs/")

with open(path / Path("company/config.json")) as f:
    company_settings = json.load(f)
with open(path / Path("employee/config.json")) as f:
    employee_settings = json.load(f)
with open(path / Path("order/config.json")) as f:
    order_settings = json.load(f)
with open(path / Path("product/config.json")) as f:
    product_settings = json.load(f)
with open(path / Path("customer/config.json")) as f:
    customer_settings = json.load(f)
