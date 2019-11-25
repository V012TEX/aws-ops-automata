from aws_billing_checker import AwsBillingChecker
from tocaro_handler import TocaroHandler
from fx_market_store import FxMarketStore


def lambda_handler(event, context):
    ce = AwsBillingChecker()
    fx = FxMarketStore()
    fx.fetch_currency_api()

    tocaro = TocaroHandler(

    )
    tocaro.set_text("VORTEX-AWS " + ce.get_today()[:7] + "月の利用料金明細（" + ce.get_today() + "現在）")
    tocaro.set_color("info")

    costs = ce.get_costs()
    message = construct_message(costs)
    total_cost = round(ce.get_total_cost(), 2)
    jpy_total_cost = int(fx.get_jpy(total_cost))
    message.append({"title": "-----\n★合計金額", "value": str(total_cost) + "USD (約" + str(jpy_total_cost) + "円)"})

    tocaro.set_attachments(message)
    res = tocaro.send2tocaro()
    return res


def construct_message(costs):
    message = []
    for service, cost in costs.items():
        d = {"title": service, "value": str(round(cost, 1)) + "USD"}
        message.append(d)
    return message


if __name__ == "__main__":
    r = lambda_handler(None, None)
    print(r)
