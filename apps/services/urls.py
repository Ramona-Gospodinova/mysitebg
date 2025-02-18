from django.urls import path
from .views import cases_view, use_case_view, use_case_by_tag_view, contacts_view

urlpatterns = [
    path('use-cases/', cases_view, name='cases'),
    path('use-cases/<pk>/', use_case_view, name='use-case-single'),
    path('use-cases/tag/<slug:tag_slug>/', use_case_by_tag_view, name='use-cases-by-tag'),
    path('contacts/', contacts_view, name='contacts'),
]
