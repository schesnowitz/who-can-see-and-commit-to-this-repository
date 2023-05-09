from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Project, Text
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages




def contactView(request):
    text = Text.objects.get(pk=1)
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            # contact_em = form.cleaned_data["contact_em"]
            message = form.cleaned_data["message"]
            try:
                send_mail(message, email, from_email="steve@chesnowitz.com", recipient_list=["steve@chesnowitz.com"]) 
            except BadHeaderError:
                return HttpResponse("Invalid header found.")
            messages.add_message(request, messages.INFO, "Your message has been sent.")
            return redirect("/")
    return render(request, "projects/contact.html", {"form": form, "text" : text})




class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/projects_new.html"
    fields = (
        "title",
        "description",
        "github",
    )

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProjectListView(ListView):
    model = Project
    template_name = "projects/project_list.html"
    queryset = Project.objects.order_by("-date")[:6]


    def get_context_data(self, *args, **kwargs):
        context = super(ProjectListView, self).get_context_data(*args, **kwargs)
        context["text"] = Text.objects.get(pk=1)
        return context


class ProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    extra_context={'text': Text.objects.get(pk=1)}

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = (
        "title",
        "description",
    )
    template_name = "projects/project_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = "projects/project_delete.html"
    success_url = reverse_lazy("projects:project_list")

    def test_func(self):
        obj = self.get_object()
        return obj.user == self.request.user
