from datetime import datetime

def validate_datetime(value):
    try:
        # Try to parse the datetime string to the specific format
        datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        # If parsing fails, raise an exception
        raise ValueError("This is not a valid date-time format. It should be 'YYYY-MM-DD HH:MM:SS'")
