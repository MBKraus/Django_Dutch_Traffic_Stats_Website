from django.shortcuts import render
from django.views import generic
from . import models
import datetime
from django.db.models import Q
from django.db.models import Count, Sum
from django.db.models import F
from django.db.models import FloatField
from django.db.models.functions import Cast
from dateutil.relativedelta import relativedelta

class MorningAll(generic.TemplateView):

    model = models.Trafficnow
    template_name = 'overview.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['highway'] = models.Trafficnow.objects.filter(
            Q(date__month=7) & (Q(time__icontains="5:00")| Q(time__icontains="5:01")| Q(time__icontains="6:00") | Q(time__icontains="6:01") | Q(time__icontains="7:00")| Q(time__icontains="7:01")) &
            Q(type__icontains="Traffic_Jam") &
            Q(road__icontains="A")).values('location_1', 'road').annotate(
            num=Count('location_1'),
            sum=Sum('km'),
            ).order_by('-sum')[:15]
        context['regional'] = models.Trafficnow.objects.filter(
            Q(date__month=7) & (Q(time__icontains="5:00")| Q(time__icontains="5:01")| Q(time__icontains="6:00") | Q(time__icontains="6:01") | Q(time__icontains="7:00")| Q(time__icontains="7:01")) & Q(type__icontains="Traffic_Jam") & Q(
                road__icontains="N")).values('location_1', 'road').annotate(num=Count('location_1'), sum=Sum('km')
                                                                            ).order_by(
            '-num')[:15]
        context['title'] = "Ochtendspits"
        context['time'] = "7.30, 8.30, en 9.30 uur"

        return context

class EveningAll(generic.TemplateView):

    model = models.Trafficnow
    template_name = 'overview.html'


    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['highway'] = models.Trafficnow.objects.filter(
            Q(date__month=7) & (Q(time__icontains="14:30")| Q(time__icontains="14:31")| Q(time__icontains="15:30") | Q(time__icontains="15:31") | Q(time__icontains="16:30")| Q(time__icontains="16:31")) &
            Q(type__icontains="Traffic_Jam") &
            Q(road__icontains="A")).values('location_1', 'road').annotate(
            num=Count('location_1'),
            sum=Sum('km'),
            ).order_by('-sum')[:15]
        context['regional'] = models.Trafficnow.objects.filter(
            Q(date__month=7) & (Q(time__icontains="14:30")| Q(time__icontains="14:31")| Q(time__icontains="15:30") | Q(time__icontains="15:31") | Q(time__icontains="16:30")| Q(time__icontains="16:31")) & Q(type__icontains="Traffic_Jam") & Q(
                road__icontains="N")).values('location_1', 'road').annotate(num=Count('location_1'), sum=Sum('km')
                                                                            ).order_by(
            '-num')[:15]
        context['title'] = "Avondspits"
        context['time'] = "16.00, 17.00 en 18.00 uur"

        return context

class TotalAll(generic.TemplateView):

    model = models.Trafficnow
    template_name = 'overview.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['highway'] = models.Trafficnow.objects.filter(
            Q(date__month=7) &
            Q(type__icontains="Traffic_Jam") &
            Q(road__icontains="A")).values('location_1', 'road').annotate(
            num=Count('location_1'),
            sum=Sum('km'),
            ).order_by('-sum')[:15]
        context['regional'] = models.Trafficnow.objects.filter(
            Q(date__month=7) &
            Q(type__icontains="Traffic_Jam") &
            Q(road__icontains="N")).values('location_1', 'road').annotate(
            num=Count('location_1'),
            sum=Sum('km')
            ).order_by('-num')[:15]
        context['title'] = "Totaal"
        context['time'] = "7.30, 8.30, 9.30, 16.00, 17.00 en 18.00 uur"

        return context