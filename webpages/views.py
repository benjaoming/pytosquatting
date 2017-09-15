from datetime import timedelta
from django.db.models import F, ExpressionWrapper, fields, Sum
from django.views.generic.base import TemplateView

from pingback import models


class Index(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        c = TemplateView.get_context_data(self, **kwargs)
        duration = ExpressionWrapper(F('last_seen')-F('first_seen'), output_field=fields.DurationField())
        duration_float = ExpressionWrapper(duration, output_field=fields.FloatField())
        count_per_duration = ExpressionWrapper(F('unique_count')/duration_float, output_field=fields.FloatField())
        top_pingbacks = models.Pingback.objects.filter(
            unique_count__gt=1,
        ).annotate(
            duration=duration,
            timed_count=count_per_duration,
        ).filter(duration__gt=timedelta(hours=2)).order_by('-timed_count')
        total_sum_per_hour = 0
        
        top_20 = list(top_pingbacks[:20])
        
        for pkg in top_20:
            if not pkg.duration:
                continue
            avg_per_hour = pkg.unique_count / (pkg.duration.total_seconds()//3600)
            pkg.avg_per_hour = avg_per_hour
            pkg.avg_per_day = avg_per_hour * 24
            total_sum_per_hour += avg_per_hour
        c['top'] = top_20
        c['total_unique_ips'] = models.Pingback.objects.all().aggregate(sum=Sum('unique_count'))['sum']
        return c