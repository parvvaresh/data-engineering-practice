import pandas as pd
import io
import os

def save_info(path):
    df = pd.read_csv(path)
    name = path.split("data/")[1].split(".csv")[0]
    print(name)

    buffer = io.StringIO()
    df.info(buf=buffer)  # Capture the info output into a buffer
    info_str = buffer.getvalue()

    info = f"""
                name is {name}
                data types and more details are:
                {info_str}

                ---------------------------------

                """
    return info 


accounts = save_info("./data/accounts.csv")
products = save_info("./data/products.csv")
transactions = save_info("./data/transactions.csv")


output_path = os.path.join("info.txt")
with open(output_path, "a") as f:
    f.write(accounts)


with open(output_path, "a") as f:
    f.write(products)

with open(output_path, "a") as f:
    f.write(transactions)
