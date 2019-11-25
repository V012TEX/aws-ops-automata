import boto3
from datetime import datetime


class AwsBillingChecker:
    def __init__(self):
        self.client = boto3.client("ce")
        self.costs = {}

    def get_cost_raw_data(self):
        cost = self.client.get_cost_and_usage(
            TimePeriod={'Start': self.get_first_day_of_month(), "End": self.get_today()},
            Granularity="MONTHLY", Metrics=['UnblendedCost'],
            GroupBy=[{"Type": "DIMENSION", "Key": "SERVICE"}])
        return cost

    def get_costs(self):
        billing = self.get_cost_raw_data()
        for service in billing["ResultsByTime"][0]["Groups"]:
            self.costs.update({service["Keys"][0]: float(service["Metrics"]["UnblendedCost"]["Amount"])})
        return self.costs

    def get_total_cost(self):
        total_cost = 0.0
        for cost in self.costs.values():
            total_cost += cost
        return total_cost

    def get_today(self):
        return str(datetime.today())[:10]

    def get_first_day_of_month(self):
        today = self.get_today()
        return today[:8] + "01"


if __name__ == '__main__':
    b = AwsBillingChecker()
    print(b.get_cost_raw_data())
    for i in b.get_cost_raw_data()["ResultsByTime"][0]["Groups"]:
        print(i)
    print(b.get_costs())
    print(b.get_total_cost())
