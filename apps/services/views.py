from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Case, Tag


def cases_view(request):
    cases = get_list_or_404(Case)
    tags = get_list_or_404(Tag)
    return render(request, 'use_cases.html', {
        'cases': cases,
        'tags': tags,
    })


def use_case_view(request, pk):
    case = get_object_or_404(Case.objects.prefetch_related('solutions'), id=pk)
    selected_solution = case.solutions.filter(is_selected=True).first()
    tags = case.tags.all()
    return render(request, 'use_case_single.html', {
        'case': case,
        'selected_solution': selected_solution,
        'tags': tags,
    })

def use_case_by_tag_view(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    cases = Case.objects.filter(tags=tag)
    tags = get_list_or_404(Tag)
    return render(request, 'use_cases.html', {
        'cases': cases,
        'tags': tags,
    })
