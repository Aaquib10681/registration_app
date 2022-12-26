from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from games.models import Category, PlayerInformation


class ListCategory(View):
    """ This endpoint lists all the categories in our system """

    def get(self, request, *args, **kwargs):
        template_name = "category_page.html"

        category_objects = Category.objects.all()
        obj = {'categories': category_objects}
        return render(request, template_name, context=obj)


class ListPlayerInfo(View):
    """ This endpoint will return player objects of our PlayerInformation class """

    def get(self, request, *args, **kwargs):
        template_name = "player_info_page.html"

        player_obj = PlayerInformation.objects.all()
        obj = {'player': player_obj}
        return render(request, template_name, context=obj)


class CreatePlayerView(View):
    """ This view will create Player object """

    def post(self, request, *args, **kwargs):
        req_obj = request.POST
        category_id = self.kwargs.get('id')
        category_obj = Category.objects.filter(id=category_id).first()
        name = req_obj.get('name')
        parentage = req_obj.get('parentage')
        address = req_obj.get('address')
        mobile_num = req_obj.get('mobile_num')
        email_address = req_obj.get('email_address')
        dob = req_obj.get('dob')
        age = req_obj.get('age')
        qualification = req_obj.get('qualification')
        try:
            PlayerInformation.objects.create(category=category_obj, name=name,
                parentage=parentage, address=address, mobile_num=mobile_num,
                email_address=email_address, dob=dob, age=age, qualification=qualification)

            return redirect(reverse('success_response'))
        except:
            return redirect(reverse('fail_response'))


class SuccessResponseView(View):
    """ This is Success page view """
    def get(self, request, *args, **kwargs):
        template_name = 'success_page.html'
        return render(request, template_name)


class FailResponseView(View):
    """ This is Fail page view """
    def get(self, request, *args, **kwargs):
        template_name = 'fail_page.html'
        return render(request, template_name)
