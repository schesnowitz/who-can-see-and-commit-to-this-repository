from django.db.models import Q
from django.views.generic import ListView, DetailView
from projects.views import Text
from .models import Post
from django.shortcuts import redirect
from django.contrib import messages


class SearchResultsView(ListView):
    model = Post
    template_name = "aipost/search.html"
    extra_context={'text': Text.objects.get(pk=1)}
    # def get_context_data(self, *args, **kwargs):
    #     context = super(SearchResultsView, self).get_context_data(*args, **kwargs)
    #     context["text"] = Text.objects.get(pk=1)

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query == "":
            messages.add_message(
                self.request,
                messages.INFO,
                "Your search was blank, please enter a valid search request.",
            )
            redirect("/")
        else:
            object_list = Post.objects.filter(
                Q(content__icontains=query) | Q(title__icontains=query)
            )

            if not object_list.exists():
                messages.add_message(
                    self.request,
                    messages.INFO,
                    "Your search did not return any results.",
                )
            else:
                # print(object_list)
                return object_list


# def search_posts(request):
#     if request.method == Post:
#         search_ai = request.POST('search_ai')
#         context = {'search_ai' : search_ai}
#         print(context)
#         return render(request, 'aipost/search.html', context=context)
#     else:
#         context = {}
#         return render(request, 'aipost/search.html', context=context)


class PostListView(ListView):
    model = Post
    template_name = "aipost/list.html"
    paginate_by = 10
    extra_context={'text': Text.objects.get(pk=1)}
    ordering = ['-created_on']
    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["side_page"] = Post.objects.all().order_by("?")[:6]
        context["page_texts"] = Text.objects.get(pk=1)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "aipost/detail.html"
    extra_context={'text': Text.objects.get(pk=1)}
    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["side_page"] = Post.objects.all().order_by("?")[:6]
        context["page_texts"] = Text.objects.get(pk=1)
        return context
