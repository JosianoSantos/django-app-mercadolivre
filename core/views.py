from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.base import TemplateView, RedirectView

from api.mercado_libre.items import get_best_sellers_by_item_category, get_most_expensives_by_category
from api.mercado_libre.user import get_logged_user_data, get_user_detail_by_id


class AuthView(TemplateView):
    template_name = 'core/auth.html'

    def get(self, request, *args, **kwargs):
        try:
            if request.GET.get('code'):
                request.session['code'] = request.GET['code']
            elif 'code' or 'user' not in request.session:
                return render(request, self.template_name)

            request.session['user'] = get_logged_user_data(request)
            return HttpResponseRedirect(reverse('core:home'))
        except Exception as e:
            messages.error(request, str(e))
            return render(request, self.template_name)


class LogoutView(RedirectView):
    def get(self, request, *args, **kwargs):
        for key in list(request.session.keys()):
            del request.session[key]
        request.session.set_expiry(-2)
        return HttpResponseRedirect(reverse('core:auth'))


class HomeView(TemplateView):
    template_name = 'core/home.html'


class BestSellersView(TemplateView):
    template_name = 'core/best_sellers.html'

    def get(self, request, *args, **kwargs):
        try:
            items = get_best_sellers_by_item_category('MLA352679')
            sorted_list = sorted(items, key=lambda x: x['sold_quantity'], reverse=True)

            # getting more seller details
            for item in sorted_list:
                seller_detail = get_user_detail_by_id(item['seller']['id'])
                item['seller'] = seller_detail

            return render(request, self.template_name, {'items': sorted_list[:5]})

        except Exception as e:
            messages.error(request, str(e))
            return render(request, self.template_name)


class MostExpensivesItemsView(TemplateView):
    template_name = 'core/most_expensives.html'

    def get(self, request, *args, **kwargs):
        try:
            items = get_most_expensives_by_category('MLA352679')
            return render(request, self.template_name, {'items': items['results'][:20]})

        except Exception as e:
            messages.error(request, str(e))
            return render(request, self.template_name)
