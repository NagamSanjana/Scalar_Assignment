import random

COMPANY_NAMES = [
    "CloudNova", "DataNest", "Flowstack", "MetricLabs",
    "Syncly", "OpsPilot", "ScaleForge", "InsightLoop"
]

def get_company_name():
    return random.choice(COMPANY_NAMES)
