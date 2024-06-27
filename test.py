from locust import HttpUser, task, between
import pandas as pd

# Load data from Excel
data = pd.read_excel('Libro6.xlsx', sheet_name='Hoja1')

class MyUser(HttpUser):
    wait_time = between(1, 2)
    
    @task
    def index(self):
        for index, row in data.iterrows():
            monto = row['RUT']
            url = f"/xxx?xxx={monto}"

            headers = {
                "Authorization": f"Bearer "
            }
            
            
            with self.client.get(url,headers=headers, catch_response=True) as response:
                if response.status_code == 401:
                    response.failure("401 Unauthorized")
                elif response.status_code == 400:
                    response.failure("400 Bad Request")
                elif response.status_code == 500:
                      response.failure("500 internal")
                else:
                    response.success()

# To run the script, use the command: locust -f script_name.py
