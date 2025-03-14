from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from applications import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/banks/', views.BankListView.as_view(), name='bank-list'),
    path('api/branches/', views.BranchListView.as_view(), name='branch-list'),
    path('api/applications/submit/', views.ApplicationSubmitView.as_view(), name='application-submit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)