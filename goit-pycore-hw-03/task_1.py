from datetime import datetime

def get_days_from_today(date):
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = (input_date - today).days
        return delta
    except ValueError:
        return "Invalid date format. Please use 'YYYY-MM-DD'."


print(get_days_from_today("2021-10-09"))
