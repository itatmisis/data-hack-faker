from pathlib import Path

import ujson as json

path = Path("../../../configs")

with open(path / Path("/company/configs.json")) as f:
    company_settings = json.load(f)
with open(path / Path("/employee/configs.json")) as f:
    employee_settings = json.load(f)
with open(path / Path("/order/configs.json")) as f:
    order_settings = json.load(f)
with open(path / Path("/product/configs.json")) as f:
    product_settings = json.load(f)
with open(path / Path("/customer/configs.json")) as f:
    customer_settings = json.load(f)
