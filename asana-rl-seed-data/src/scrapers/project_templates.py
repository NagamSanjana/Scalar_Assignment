import random

PROJECT_TEMPLATES = [
    "Q2 Product Roadmap",
    "Website Redesign",
    "Enterprise Onboarding",
    "Marketing Campaign Launch",
    "Infrastructure Migration"
]

def get_project_name():
    return random.choice(PROJECT_TEMPLATES)
