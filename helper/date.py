from datetime import timedelta, date, datetime
import time

def calculate_expiration_date():
    """
    Calculates the expiration date by adding 30 days to the current date.

    Returns:
        tuple: (epoch timestamp, formatted normal date)
    """
    today = date.today()
    expiration_date = today + timedelta(days=30)
    pattern = '%Y-%m-%d'
    epoch = int(time.mktime(time.strptime(str(expiration_date), pattern)))
    normal_date = datetime.fromtimestamp(epoch).strftime('%Y-%m-%d')
    return epoch, normal_date

def is_date_valid(saved_date):
    """
    Checks if a given saved date is still valid.

    Args:
        saved_date (int): The saved date as an epoch timestamp.

    Returns:
        bool: True if the date is still valid, False otherwise.
    """
    today = date.today()
    pattern = '%Y-%m-%d'
    current_epoch = int(time.mktime(time.strptime(str(today), pattern)))
    time_difference = saved_date - current_epoch

    if time_difference > 0:
        return True
    else:
        return False
