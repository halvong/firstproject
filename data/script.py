from datetime import datetime
from django.utils import timezone
from django.utils.six import BytesIO
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from toys.models import Toy
from toys.serializers import ToySerializer

toy_release_date = timezone.make_aware(datetime.now(), timezone.get_current_timezone())

toy3 = Toy(name='Lego Mincraft', description='Construction Toy for Kids', release_date=toy_release_date, toy_category='Education', was_included_in_home=True)
toy4 = Toy(name='RC Drone', description='Portable Pocket Quadcopter', release_date=toy_release_date, toy_category='Gadget', was_included_in_home=False)
