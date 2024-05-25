
from .urls_authentification import urlpatterns as authentification_urlpatterns
from .urls_car import urlpatterns as car_urlpatterns
from .urls_car_body import urlpatterns as car_body_urlpatterns
from .urls_car_drive import urlpatterns as car_drive_urlpatterns
from .urls_car_engine import urlpatterns as car_engine_urlpatterns
from .urls_car_engine_type import urlpatterns as car_engine_type_urlpatterns
from .urls_car_title_model_generation import urlpatterns as car_title_model_generation_urlpatterns
from .urls_car_transmission import urlpatterns as car_transmission_urlpatterns
from .urls_car_year import urlpatterns as car_year_urlpatterns
from .urls_messagedata import urlpatterns as messagedata_urlpatterns
from .urls_registration import urlpatterns as registration_urlpatterns
from .urls_sentmessage import urlpatterns as sentmessage_urlpatterns


urlpatterns = (authentification_urlpatterns + car_urlpatterns + car_body_urlpatterns + car_drive_urlpatterns +
               car_engine_urlpatterns + car_engine_type_urlpatterns + car_title_model_generation_urlpatterns +
               car_transmission_urlpatterns + car_year_urlpatterns + messagedata_urlpatterns +
               registration_urlpatterns + sentmessage_urlpatterns)
