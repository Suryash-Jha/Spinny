from django.conf import settings
settings.configure()
# from ..MainProj import settings

def validate_box(user, area, volume):
    max_area= settings.A1
    max_volume= settings.V1
    max_individual_box= settings.L1
    max_total_box= settings.L2
    print(max_area, max_volume, max_individual_box, max_total_box)

default_value_if_not_exists=10
A1_value = getattr(settings, 'A1', default_value_if_not_exists)
V1_value = getattr(settings, 'V1', default_value_if_not_exists)
# Add other settings as needed

# Use the setting values
print(f'A1 value: {A1_value}')
print(f'V1 value: {V1_value}')
# validate_box('user', 100, 1000)
from django.conf import settings

# Access constraint settings
A1_constraint = getattr(settings, 'A1', 0)
# Use the constraint values
print(f'A1 constraint: {A1_constraint}')
