from django.db.models import Q
from django.views.generic import ListView, DetailView
from projects.views import Text
from .models import Post
from django.shortcuts import redirect, render
from django.contrib import messages
from django.http import HttpResponseRedirect

# langchain
import os
from langchain.llms import OpenAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders import WebBaseLoader
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from datetime import datetime

dt = datetime.now()


def create_post_view(request):


    

    if request.method == "POST":
        if request.POST.get("form_type") == "formOne":
            url = request.POST["url"]
            # print(url)
            context = {"url": url}
            os.environ[
                "OPENAI_API_KEY"
            ] = ""
            llm = OpenAI(temperature=0.9, verbose=True)

            loader = WebBaseLoader(web_path=url)
            data = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000, chunk_overlap=250, length_function=len
            )

            docs = text_splitter.split_documents(data)

            embeddings = OpenAIEmbeddings()
            db = FAISS.from_documents(docs, embeddings)
            db.add_documents(docs)

            """
            -------------------------------------------------------------
            Reporter Name
            -------------------------------------------------------------
            """

            prompt_template = """Use the context below to create a ficticious name for a news reporter.
            the name should be less than 25 characters, only generate a full name:
                name: {name}
                context: {query}
                Reporter Name:"""

            story_reporter = PromptTemplate(
                template=prompt_template, input_variables=["name", "query"]
            )

            chain = LLMChain(llm=llm, prompt=story_reporter, verbose=True)

            query = "write a title for the story"
            docs = db.similarity_search(query, k=3)
            story_reporter_name = chain.run({"name": docs, "query": query})
            print(story_reporter_name)

            """
            -------------------------------------------------------------
            Story Title
            -------------------------------------------------------------
            """

            prompt_template = """Use the context below to write  a title.:
                Context: {title}
                Topic: {query}
                Blog title:"""

            title_content = PromptTemplate(
                template=prompt_template, input_variables=["title", "query"]
            )

            chain = LLMChain(llm=llm, prompt=title_content, verbose=False)

            query = "write a title for the story"
            docs = db.similarity_search(query, k=3)
            story_title = chain.run({"title": docs, "query": query})
            print(story_title)

            """
            -------------------------------------------------------------
            Story Content
            -------------------------------------------------------------
            """

            prompt_template = """Use the context below to write a 700 word blog post about the context below:
                Context: {context}
                Topic: {query}
                Blog post:"""

            prompt_content = PromptTemplate(
                template=prompt_template, input_variables=["context", "query"]
            )

            chain = LLMChain(llm=llm, prompt=prompt_content, verbose=False)

            query = "write a detailed synopsis of this story"
            docs = db.similarity_search(query, k=3)
            story_content = chain.run({"context": docs, "query": query})
            print(story_content)
            text = Text.objects.get(pk=1)
            context = {
                "url": url,
                "story_content": story_content,
                "story_reporter_name": story_reporter_name,
                "story_title": story_title,
                "text":text
            }
            
            return render(request, "aipost/create_post.html", context)

        if (
            request.POST.get("form_type") == "formTwo"
            and request.POST.get("story_title")
            and request.POST.get("story_content")
            and request.POST.get("url")
            and request.POST.get("story_reporter_name")
        ):

            post = Post()
            post.title = request.POST.get("story_title")
            post.content = request.POST.get("story_content")
            post.url = request.POST.get("url")
            post.reporter = request.POST.get("story_reporter_name")
            post.save()
            print(post.id)
            messages.success(request, "AI news was successfully created")
                
            return redirect('aiposts:post_detail', post.id)
        else:
            return render(request, "aipost/create_post.html")
           
    text = Text.objects.get(pk=1)
    return render(request, "aipost/create_post.html", {'text':text})


class SearchResultsView(ListView):
    model = Post
    template_name = "aipost/search.html"
    extra_context = {"text": Text.objects.get(pk=1)}
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
    extra_context = {"text": Text.objects.get(pk=1)}
    ordering = ["-created_on"]

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context["side_page"] = Post.objects.all().order_by("?")[:6]
        context["page_texts"] = Text.objects.get(pk=1)
        return context


class PostDetailView(DetailView):
    model = Post
    template_name = "aipost/detail.html"
    extra_context = {"text": Text.objects.get(pk=1)}

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["side_page"] = Post.objects.all().order_by("?")[:6]
        context["page_texts"] = Text.objects.get(pk=1)
        return context
