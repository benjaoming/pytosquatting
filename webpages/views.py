from django.db.models import Sum
from django.views.generic.base import TemplateView

from pingback import models


class Index(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        c = TemplateView.get_context_data(self, **kwargs)
        top_pingbacks = models.Pingback.objects.filter(
            unique_count__gt=1,
        ).values('package_name', 'unique_count', 'first_seen', 'last_seen')
        total_sum_per_hour = 0
        
        top_pingbacks = list(top_pingbacks)
        
        top_pingbacks_static_refs = []
        
        for pkg in top_pingbacks:
            
            duration = pkg['last_seen'] - pkg['first_seen']

            if not duration:
                continue
            
            avg_per_hour = pkg['unique_count'] / (duration.total_seconds()//3600)
            pkg['avg_per_hour'] = avg_per_hour
            pkg['avg_per_day'] = avg_per_hour * 24
            total_sum_per_hour += avg_per_hour
            top_pingbacks_static_refs.append({**pkg})
        
        top_pingbacks_static_refs = sorted(top_pingbacks_static_refs, key=lambda x: -x['avg_per_hour'])
        # Keep on showing the Top 20, because some PyPI admin is deleting the
        # packages in it.
        # ...just this top 20 seems to be the source... so we could sneak in
        # names like "six" and "django" and they'd just delete that too??
        c['top'] = top_pingbacks_static_refs[:20]
        c['total_unique_ips'] = models.Pingback.objects.all().aggregate(sum=Sum('unique_count'))['sum']
        return c