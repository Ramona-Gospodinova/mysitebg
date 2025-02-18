from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import ContactForm
from .models import Case, Tag
from django.contrib import messages
from django.core.mail import send_mail
from a_core.settings import DEFAULT_FROM_EMAIL, DEFAULT_TO_EMAIL

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

def contacts_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            try:
                send_mail(
                    f"Ново съобщение от {name}",
                    message + f"\n\nИмейл: {email}",
                    DEFAULT_FROM_EMAIL,
                    DEFAULT_TO_EMAIL,
                    fail_silently=False,
                )
                messages.success(request, 'Съобщението ви беше изпратено успешно.')
                form = ContactForm()
            except Exception as e:
                pass

            return redirect('contacts')
    else:
        form = ContactForm()
    return render(request, 'contacts.html', {'form': form})