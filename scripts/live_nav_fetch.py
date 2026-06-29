import requests
import pandas as pd
url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)
data = response.json()
print(data)
nav_data = data["data"]
df = pd.DataFrame(nav_data)
print(df.head())
df.to_csv(
    "data/raw/HDFC_Top100_NAV.csv",
    index=False
)
funds = {

    "SBI_Bluechip":119551,

    "ICICI_Bluechip":120503,

    "Nippon_LargeCap":118632,

    "Axis_Bluechip":119092,

    "Kotak_Bluechip":120841
}
for name, code in funds.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/{name}.csv",
        index=False
    )

    print(name, "Downloaded")
df = pd.read_csv("data/raw/01_fund_master.csv")
print(df["fund_house"].unique())
print(df["category"].unique())
print(df["sub_category"].unique())
print(df["risk_category"].unique())
master = pd.read_csv("data/raw/01_fund_master.csv")
history = pd.read_csv("data/raw/02_nav_history.csv")
master_codes = set(master["amfi_code"])
history_codes = set(history["amfi_code"])
master_codes = set(master["amfi_code"])
history_codes = set(history["amfi_code"])
missing = master_codes - history_codes
print(missing)
set()
