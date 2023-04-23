from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView




class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "account/signup.html"

class EditView(UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("project_list")
    template_name = "account/edit.html"
    def get_object(self):
        return self.request.user

"""
We’re subclassing the generic class-based view CreateView in our SignUpView class. We specify
the use of the built-in UserCreationForm and the not-yet-created template at signup.html. And
we use reverse_lazy to redirect the user to the log in page upon successful registration.
Why use reverse_lazy here instead of reverse? The reason is that for all generic class-based
views the URLs are not loaded when the file is imported, so we have to use the lazy form of
reverse to load them later when they’re available.
Now in your text editor create the file signup.html within the templates/registration/
directory. Populate it with the code below.
"""