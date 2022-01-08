from datetime import datetime 

def get_date(date_string, format):
    try:
        return datetime.strptime(date_string, format)
    except Exception as ex :
        return None