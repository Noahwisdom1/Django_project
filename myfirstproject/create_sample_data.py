#!/usr/bin/env python
import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproject.settings')
django.setup()

from members.models import Member

# Create sample members
sample_members = [
    {'name': 'John Doe', 'email': 'john@example.com', 'city': 'New York', 'country': 'USA'},
    {'name': 'Jane Smith', 'email': 'jane@example.com', 'city': 'London', 'country': 'UK'},
    {'name': 'Bob Johnson', 'email': 'bob@example.com', 'city': 'Toronto', 'country': 'Canada'},
    {'name': 'Alice Brown', 'email': 'alice@example.com', 'city': 'Sydney', 'country': 'Australia'},
]

for member_data in sample_members:
    member, created = Member.objects.get_or_create(
        email=member_data['email'],
        defaults=member_data
    )
    if created:
        print(f"Created member: {member.name}")
    else:
        print(f"Member already exists: {member.name}")

print("Sample data creation completed!")