
from .models.models_car import Car
from .models.models_car_title_model_generation import Car_Title, Car_Model, Car_Generation
from .models.models_car_year import Car_Year
from .models.models_car_engine import Car_Engine
from .models.models_car_transmission import Car_Transmission
from .models.models_car_body import Car_Body
from .models.models_car_engine_type import Car_EngineType
from .models.models_car_drive import Car_Drive
from .models.models_messagedata import MessageData
from .models.models_sentmessage import SentMessage
from .models.models_post import Post
from .models.models_formmessage import FormMessage
from .models.models_registration import Registration
from django.contrib import admin
from django.conf import settings
import requests
from django.http import HttpResponseRedirect
from .views.telegram_utils import send_telegram_message, send_select_user_telegram_message, send_form_telegram_message
from admin_extra_buttons.api import ExtraButtonsMixin, button
from admin_extra_buttons.utils import HttpResponseRedirectToReferrer
from django.urls import reverse
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'car_title', 'car_model', 'car_generation', 'car_vin', 'main_car_image', 'car_images',
                    'year', 'transmission', 'engine', 'fuel', 'car_body', 'car_drive', 'car_color', 'horse_power',
                    'consumption', 'mileage', 'price_byn', 'price_usd', 'city', 'description', 'car_options',
                    'http_link')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'car_title', 'car_model', 'car_generation', 'car_vin', 'main_car_image', 'car_images',
                    'year', 'transmission', 'engine', 'fuel', 'car_body', 'car_drive', 'car_color', 'horse_power',
                    'consumption', 'mileage', 'price_byn', 'price_usd', 'city', 'description', 'car_options',
                    'http_link')
    # поиск по полям
    search_fields = ['id', 'car_title', 'car_model', 'car_generation', 'car_vin', 'main_car_image', 'car_images',
                    'year', 'transmission', 'engine', 'fuel', 'car_body', 'car_drive', 'car_color', 'horse_power',
                    'consumption', 'mileage', 'price_byn', 'price_usd', 'city', 'description', 'car_options',
                    'http_link']
    # ссылки по полям
    list_display_links = ['main_car_image', 'car_images', 'http_link']

    # редактирование
    #list_editable = ['price_byn', 'price_usd']

    #actions = ['send_message']


admin.site.register(Car, CarAdmin)
######################
class Car_TitleAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'car_title')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'car_title')
    # поиск по полям
    search_fields = ['id', 'car_title']

    # редактирование
    #list_editable = ['car_title']

admin.site.register(Car_Title, Car_TitleAdmin)

##########################
class Car_ModelAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'car_model', 'car_title_id')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'car_model', 'car_title_id')
    # поиск по полям
    search_fields = ['id', 'car_model', 'car_title_id']

    # редактирование
    #list_editable = ['car_model']

admin.site.register(Car_Model, Car_ModelAdmin)

##########################
class Car_GenerationAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'car_generation', 'car_model_id')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'car_generation', 'car_model_id')
    # поиск по полям
    search_fields = ['id', 'car_generation', 'car_model_id']

    # редактирование
    #list_editable = ['car_model']

admin.site.register(Car_Generation, Car_GenerationAdmin)
##########################
class Car_YearAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'car_year')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'car_year')
    # поиск по полям
    search_fields = ['id', 'car_year']

    # редактирование
    #list_editable = ['car_model']

admin.site.register(Car_Year, Car_YearAdmin)
##########################
class Car_EngineAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'car_engine')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'car_engine')
    # поиск по полям
    search_fields = ['id', 'car_engine']

    # редактирование
    list_editable = ['car_engine']

admin.site.register(Car_Engine, Car_EngineAdmin)
##########################
class Car_TransmissionAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'car_transmission')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'car_transmission')
    # поиск по полям
    search_fields = ['id', 'car_transmission']

    # редактирование
    #list_editable = ['car_model']

admin.site.register(Car_Transmission, Car_TransmissionAdmin)


##########################
class Car_BodyAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'car_body')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'car_body')
    # поиск по полям
    search_fields = ['id', 'car_body']

    # редактирование
    #list_editable = ['car_model']

admin.site.register(Car_Body, Car_BodyAdmin)

##########################
class Car_EngineTypeAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'car_engine_type')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'car_engine_type')
    # поиск по полям
    search_fields = ['id', 'car_engine_type']

    # редактирование
    #list_editable = ['car_model']

admin.site.register(Car_EngineType, Car_EngineTypeAdmin)

##########################
class Car_DriveAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'car_drive')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'car_drive')
    # поиск по полям
    search_fields = ['id', 'car_drive']

    # редактирование
    #list_editable = ['car_model']

admin.site.register(Car_Drive, Car_DriveAdmin)

##########################
class RegistrationAdmin(admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'username', 'email', 'password')
    # пагинация
    list_per_page = 10
    # для фильтрации по полям
    list_filter = ('id', 'username', 'email', 'password')
    # поиск по полям
    search_fields = ['id', 'username', 'email', 'password']

    # редактирование
    #list_editable = ['car_model']

admin.site.register(Registration, RegistrationAdmin)

########################################################

class MessageDataAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    # для отображения полей в django administration
    list_display = ('id', 'telegram_id', 'first_name', 'last_name', 'phone_number', 'message', 'full_date_time',
                    'click_on_button')
    # для фильтрации по полям
    list_filter = ('id', 'telegram_id', 'first_name', 'last_name', 'phone_number', 'message', 'full_date_time')
    # поиск по полям
    search_fields = ['id', 'telegram_id', 'first_name', 'last_name', 'phone_number', 'message', 'full_date_time']
    # ссылки по полям
    list_display_links = ['message']

    actions = ['send_message']

    def send_message(self, request, queryset):
        form_message_url = "http://127.0.0.1:8000/admin/tele_bot_app/formmessage/add/" #?????
        return HttpResponseRedirect(form_message_url)
        # token = settings.TOKEN
        # form_message = FormMessage.objects.first()
        #
        # if form_message:
        #     message = form_message.form_message
        #
        #     queryset_list = list(queryset.values('telegram_id'))
        #     queryset_repeated = [record['telegram_id'] for record in queryset_list]
        #     querysets = list(set(queryset_repeated))
        #
        #     for query in querysets:
        #         first_name = MessageData.objects.filter(telegram_id=query)
        #         name = first_name.first().first_name
        #         url = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={query}&text={name}, {message}"
        #         requests.get(url).json()

    send_message.short_description = "Перейти к написанию сообщения"


    def click_on_button(self, message_object):
        url = reverse('create-sent-message', args=(message_object.telegram_id, message_object.message))  #?????
        return format_html('<a class="button" href="{}">Ответить</a>', url)

    click_on_button.short_description = 'Ответ на сообщение'

####
    @button(permission='demo.add_demomodel1',
            change_form=False, label='Обновить',
            html_attrs={'style': 'background-color:#808080;color:white'})
    def refresh(self, request):
        self.message_user(request, 'Обновление выполнено')
        # Optional: returns HttpResponse
        return HttpResponseRedirectToReferrer(request)
####
admin.site.register(MessageData, MessageDataAdmin)

#######################################################

class SentMessageAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    change_form_template = "message_answer.html"
    # для отображения полей в django administration
    list_display = ('id', 'telegram_id', 'message', 'sentmessage_time', 'is_sent')
    # для фильтрации по полям
    list_filter = ('id', 'telegram_id', 'message', 'sentmessage_time')
    # поиск по полям
    search_fields = ['id', 'telegram_id', 'message', 'sentmessage_time']
    # ссылки по полям
    list_display_links = ['message']

    #actions = ['send_message']

    def response_change(self, request, sentmessage):
        if "message-answer" in request.POST:
            send_select_user_telegram_message(sentmessage=sentmessage)
            sentmessage.is_sent = True
            sentmessage.save()
            self.message_user(request, "Ответ на сообщение пользователя отправлено в телеграм")
            return HttpResponseRedirect(request.path_info)

        return super().response_change(request, sentmessage)


####
    @button(permission='demo.add_demomodel1',
            change_form=False, label='Обновить',
            html_attrs={'style': 'background-color:#808080;color:white'})
    def refresh(self, request):
        self.message_user(request, 'Обновление выполнено')
        # Optional: returns HttpResponse
        return HttpResponseRedirectToReferrer(request)
####
admin.site.register(SentMessage, SentMessageAdmin)
#######################################################
@admin.register(Post)
class PostAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    change_form_template = "post_change_form.html"
    list_display = ('title', 'created_at', 'is_published')
    list_filter = ('title', 'created_at', 'is_published')
    # поиск по полям
    search_fields = ['title', 'created_at', 'is_published']
    # ссылки по полям
    #list_display_links = ['message']

    def response_change(self, request, post_obj):
        if "publish-telegram" in request.POST:
            send_telegram_message(post=post_obj)
            post_obj.is_published = True
            post_obj.save()
            self.message_user(request, "Опубликовано сообщение об этом посте в телеграм канале")
            return HttpResponseRedirect(request.path_info)

        return super().response_change(request, post_obj)

####
    @button(permission='demo.add_demomodel1',
            change_form=False, label='Обновить',
            html_attrs={'style': 'background-color:#808080;color:white'})
    def refresh(self, request):
        self.message_user(request, 'Обновление выполнено')
        # Optional: returns HttpResponse
        return HttpResponseRedirectToReferrer(request)
####

###########
class FormMessageAdmin(admin.ModelAdmin):
    change_form_template = "message_answer_for_everyone.html"
    list_display = ('form_message', 'created_time', 'is_done')
    list_filter = ('form_message', 'created_time')
    # поиск по полям
    search_fields = ['form_message', 'created_time']
    # ссылки по полям
    #list_display_links = ['message']

    def response_change(self, request, formmessage):
        if "message-answer-all" in request.POST:
            send_form_telegram_message(formmessage=formmessage)
            formmessage.is_done = True
            formmessage.save()
            self.message_user(request, "Опубликовано сообщение всем подписчикам телеграм бота")
            return HttpResponseRedirect(request.path_info)

        return super().response_change(request, formmessage)

admin.site.register(FormMessage, FormMessageAdmin)