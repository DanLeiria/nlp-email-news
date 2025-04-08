from datetime import datetime
from dateutil.relativedelta import relativedelta


def life_tracker(birthday_date: str, expect_years: int):
    """
    This function tracks the number of weeks
    I expect to have left of the users life

    Parameters:
        - birthday_date: birthday_date: As a string, e.g., "17/10/1997"
        - expect_years: Number of expected years to live
    """

    # Convert birthday date to datetime
    origin_date = datetime.strptime(birthday_date, "%d/%m/%Y").date()

    # Get todays date
    today_date = datetime.today().date()

    # Calculate the current number of weeks since birthday
    days_diff = (today_date - origin_date).days
    current_weeks = days_diff // 7

    # Calculate total number of weeks (entire life)
    final_date = origin_date + relativedelta(years=expect_years)
    final_weeks = (final_date - origin_date).days // 7

    # Calculate diff of weeks
    diff_weeks = final_weeks - current_weeks

    return f"You have {diff_weeks} weeks left"


if __name__ == "__main__":
    print(life_tracker(birthday_date="16/10/1996", expect_years=76))
