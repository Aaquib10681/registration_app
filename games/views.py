from django.shortcuts import render, redirect, reverse
from django.views.generic import View

from games.models import Category, PlayerInformation


# register

class ListCategory(View):
    """ This endpoint lists all the categories in our system """

    def get(self, request, *args, **kwargs):
        template_name = "category_page.html"

        category_objects = Category.objects.all()
        obj = {'categories': category_objects}
        return render(request, template_name, context=obj)


class CreatePlayerView(View):
    """ This view will create Player object """

    def post(self, request, *args, **kwargs):
        req_obj = request.POST
        category_id = self.kwargs.get('id')
        print('post field id === ', category_id)
        category_obj = Category.objects.filter(id=category_id).first()
        name = req_obj.get('name')
        parentage = req_obj.get('parentage')
        address = req_obj.get('address')
        mobile_num = req_obj.get('mobile_num')
        email_address = req_obj.get('email_address')
        dob = req_obj.get('dob')
        age = req_obj.get('age')
        qualification = req_obj.get('qualification')

        print("name", name, "parentage", parentage, "address", address, "mobile_num", mobile_num, "email_address", email_address, "dob", dob, "age", age, "qualification", qualification) 
        try:
            PlayerInformation.objects.create(category=category_obj, name=name,
                parentage=parentage, address=address, mobile_num=mobile_num,
                email_address=email_address, dob=dob, age=age, qualification=qualification)

            return redirect(reverse('success_response'))
        except Exception as e:
            print('error == ', e)
            return redirect(reverse('fail_response'))

    def get(self, request, *args, **kwargs):
            category_id = self.kwargs.get('id')
            template_name = 'registration_page.html'
            context = {'category_id': category_id}
            return render(request, template_name, context=context)


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


# show

class ListRegisteredCategory(View):
    """ This endpoint lists all the registered details in our system """

    def get(self, request, *args, **kwargs):
        template_name = "registered_category.html"

        category_objects = Category.objects.all()
        obj = {'categories': category_objects}
        return render(request, template_name, context=obj)

class ShowCategoryPlayers(View):
    """ This endpoint will return player objects  linked to Category """

    def get(self, request, *args, **kwargs):
        template_name = "show_category_players.html"
        category_id = self.kwargs.get('id')

        category_obj = Category.objects.filter(id=category_id).first()
        if category_obj:
            player_obj = PlayerInformation.objects.filter(category=category_obj)
            obj = {'player': player_obj}
            return render(request, template_name, context=obj)


class ShowPlayerDetails(View):
    """ This endpoint will return player objects  linked to Category """

    def get(self, request, *args, **kwargs):
        template_name = "player_detail_page.html"
        player_id = self.kwargs.get('id')
        player_obj = PlayerInformation.objects.filter(id=player_id).first()   
        obj = {'player': player_obj}
        return render(request, template_name, context=obj)


