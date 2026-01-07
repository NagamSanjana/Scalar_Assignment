from datetime import datetime, timedelta
import random

def random_past_date(days=90):
    return datetime.now() - timedelta(days=random.randint(0, days))
