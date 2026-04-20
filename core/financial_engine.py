""" This function is used to calculate the expected loss and expected profit...."""

def calculate_finances(pd, loan_amount,interest_rate):
    # for calculating expected loss, we would be using pd, LGD and  interest rate....
    # for calculating expected profit, we would be using the other logic of probabaility of default and income and interest rate.....
    # What is LGD = Loss given default  ( tells about the probability of loss by the lender from the borrower getting defaulted...)

    LGD = 0.6 # which is just assuming for our project....
    cost_of_captial = 0.05
    expected_loss = pd*loan_amount*LGD
    expected_profit = loan_amount*interest_rate* (1-pd)
    expected_cost = cost_of_captial*loan_amount

    net_profit = expected_profit - expected_loss - expected_cost

    return {"expected profit":expected_profit,
            "expected loss": expected_loss,
            "expected cost":expected_cost,
            "net profit":net_profit}