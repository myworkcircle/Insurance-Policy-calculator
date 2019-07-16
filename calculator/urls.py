from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from dummy_premium.views import index,police,fir,view,Pdf


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',index,name="home"),
    path('policy/',police,name="policy"),
    path('fire/',fir,name="fire"),
    path('view/<id>/',view,name="view"),
    path('pdf/',Pdf.as_view(),name='pdf')
    
] 
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
