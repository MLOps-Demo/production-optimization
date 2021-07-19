"""
Run load tests:

locust -f load_test/locustfile.py --host http://127.0.0.1:3000
"""

from locust import HttpUser, task
import pandas as pd
import random


feature_columns = {
    '% Iron Feed':'iron_feed',
     'Starch Flow':'starch_flow',
     'Amina Flow':'amina_flow',
     'Ore Pulp Flow':'ore_pulp_flow',
     'Ore Pulp pH':'ore_pulp_ph',
     'Ore Pulp Density':'ore_pulp_density',
     'Flotation Column 01 Air Flow':'flotation_column_01_air_flow',
     'Flotation Column 02 Air Flow':'flotation_column_02_air_flow',
     'Flotation Column 04 Air Flow':'flotation_column_04_air_flow',
     'Flotation Column 05 Air Flow':'flotation_column_05_air_flow',
     'Flotation Column 06 Air Flow':'flotation_column_06_air_flow',
     'Flotation Column 07 Air Flow':'flotation_column_07_air_flow',
     'Flotation Column 01 Level':'flotation_column_01_level',
     'Flotation Column 02 Level':'flotation_column_02_level',
     'Flotation Column 03 Level':'flotation_column_03_level',
     'Flotation Column 04 Level':'flotation_column_04_level',
     'Flotation Column 05 Level':'flotation_column_05_level',
     'Flotation Column 06 Level':'flotation_column_06_level',
     'Flotation Column 07 Level':'flotation_column_07_level',
     '% Iron Concentrate':'iron_concentrate'
}

# /Users/shreyassk/Desktop/production-monitoring/load_test/

dataset = (pd.read_csv("mining_flotation_test.csv", decimal=",").rename(columns=feature_columns).to_dict(orient="records"))


class ProductionOptimizationUser(HttpUser):
    @task(1)
    def healthcheck(self):
        self.client.get("/healthcheck")

    @task(10)
    def prediction(self):
        record = random.choice(dataset).copy()
        self.client.post("/predict", json=record)

    @task(2)
    def prediction_bad_value(self):
        record = random.choice(dataset).copy()
        corrupt_key = random.choice(list(record.keys()))
        record[corrupt_key] = "bad data"
        self.client.post("/predict", json=record)
