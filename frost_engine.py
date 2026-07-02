
def calculate_f(revenue_growth):
    if revenue_growth > 25:
        return 3
    elif revenue_growth > 15:
        return 2
    elif revenue_growth > 5:
        return 1
    return 0


def calculate_r(rs_rank):
    if rs_rank > 90:
        return 3
    elif rs_rank > 80:
        return 2
    elif rs_rank > 70:
        return 1
    return 0


