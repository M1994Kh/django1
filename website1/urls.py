
from django.urls import path
from website1.views import *



urlpatterns = [
    path('',index_view),
    # path('', Home.as_view(), name='home')
]

# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)