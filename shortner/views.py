from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import UrlForm
from .models import UrlData
# Create your views here.

class Url(TemplateView):
    template_name = 'index.html'
# handles GET request
    def get(self, request):
        ctx = {
            'title':"Shorten your url here",
            'form' :UrlForm()
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = UrlForm(request.POST or None)
        # print(form.get["short_key"])
        if request.method == 'POST' and form.is_valid():
            # process data
            cleaned_url                 = form.cleaned_data["url"]
            cleaned_random_key          = form.cleaned_data["short_key"]
            cleaned_exp_in_minutes      = form.cleaned_data["expire"]

            if UrlData.objects.filter(random_key__iexact=cleaned_random_key):
                ctx = {
                    'title':"Cutom URL already exists",
                    'form' :UrlForm()
                }
                return render(request, self.template_name, ctx)

            url_object                  = UrlData.objects.create(url=cleaned_url, random_key=cleaned_random_key, exp_in_minutes=cleaned_exp_in_minutes)
            if not url_object:
                url_object.save()
        # return HttpResponseRedirect('/thanks/')
            return render(request, 'results.html', {'title':"Successfully shortened url!",'url':cleaned_url, 'shorturl':url_object.get_abs_url()})
        else:
            ctx = {
                    'title':"Invalid entry",
                    'form' :form
                }
            return render(request, self.template_name, ctx)


def results(request):
    context = {
        'data':"nede",
    }
    return render(request, 'results.html', context)
    # return HttpResponse()

def redirect(request, slug):
    obj = UrlData.objects.filter(random_key__iexact=slug)
    if not obj:
        form = UrlForm()
        ctx = {
            'title':'invalid url provided',
            'form':form,
        }
        return render(request, 'index.html', ctx)
    else:
        url = obj.first().url
        return HttpResponseRedirect(url)