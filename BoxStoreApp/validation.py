from django.conf import settings
from .models import BoxModel
from django.db.models import Sum, Q
# settings.configure()
# from ..MainProj import settings

def validate_box(user, area, volume):
    max_area= settings.A1
    max_volume= settings.V1
    max_individual_box= settings.L1
    max_total_box= settings.L2
    print(max_area, max_volume, max_individual_box, max_total_box)

    total_area= BoxModel.objects.aggregate(Sum('area'))['area__sum']
    total_volume= BoxModel.objects.aggregate(Sum('volume'))['volume__sum']
    total_box= BoxModel.objects.count()
    total_individual_box= BoxModel.objects.filter(created_by=user).count()

    print("tot: ", total_area, total_volume, total_box, total_individual_box)

    if total_area is None:
        total_area= 0
    
    if total_volume is None:
        total_volume= 0
    
    if total_box is None:
        total_box= 0

    if total_individual_box is None:
        total_individual_box= 0

    if total_area+area > max_area:
        return False, 'Total area exceeded'
    
    if total_volume+volume > max_volume:
        return False, 'Total volume exceeded'
    
    if total_individual_box+1 > max_individual_box:
        return False, 'Total individual box exceeded'
    
    if total_box+1 > max_total_box:
        return False, 'Total box exceeded'

    return True, 'Validated'
    


