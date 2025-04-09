from datetime import datetime
from dateutil.relativedelta import relativedelta


def life_tracker(birthday_date: str, expect_years: int):
    """
    This function tracks in percentage the remaining
    life the user has left given his/hers birthday date
    and expect (estimated) years to live.

    Parameters:
        - birthday_date: As a string, e.g., "17/10/1997"
        - expect_years: Number of expected years to live
    """

    # Convert birthday date to datetime
    origin_date = datetime.strptime(birthday_date, "%d/%m/%Y").date()

    # Get todays date
    today_date = datetime.today().date()

    # Calculate the current number of days since birthday
    current_diff = (today_date - origin_date).days

    # Calculate total number of days (entire expected life)
    final_date = origin_date + relativedelta(years=expect_years)
    total_diff = (final_date - origin_date).days

    # Calculate percentage of remaining life
    pct_life = (total_diff - current_diff) / total_diff * 100

    return f"{pct_life:.0f}% remaining"


if __name__ == "__main__":
    print(life_tracker(birthday_date="16/02/2005", expect_years=76))
