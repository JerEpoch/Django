from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, ListView, CreateView, DeleteView, UpdateView, DetailView
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from amiibo.models import Amiibo
from django.core.exceptions import PermissionDenied
from .forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
# Create your views here.


class LoggedInMixin(object):

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)

class ListAmiiboView(LoggedInMixin,ListView):

    model = Amiibo
    template_name = 'amiibo_list.html'

    def get_queryset(self):

        return Amiibo.objects.filter(owner=self.request.user)

class AmiiboRegister(CreateView):

    model = Amiibo
    template_name = 'amiibo_register.html'
    form_class = UserCreationForm

    def get_success_url(self,request,user):
        return ('amiibo-list')

    def form_valid(self, form):
        form.save()
        #return self.render_to_response(self.get_context_data(form=form))
        return render_to_response('registration/registersuccess.html',)
        #return HttpResponseRedirect(reverse('amiibo-list'))
        #form.owner = request.user
        #return super(AmiiboRegister, self).form_valid(form)



class AmiiboOwnerMixin(object):

    def get_object(self,queryset=None):

        if queryset is None:
            queryset = self.get_queryset()

        pk = self.kwargs.get(self.pk_url_kwarg, None)
        queryset = queryset.filter(
            pk=pk,
            owner=self.request.user,
        )

        try:
            obj = queryset.get()
        except ObjectDoesNotExist:
            raise PermissionDenied

        return obj

class CreateAmiiboView(LoggedInMixin,CreateView):


    model = Amiibo
    template_name = 'edit_amiibo.html'
    fields = ('name','series')
    #fields = "__all__"


    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
        return reverse('amiibo-list')

    def get_context_data(self, **kwargs):

        context = super(CreateAmiiboView,self).get_context_data(**kwargs)
        #form.instance.owner = AmiiboRegister.objects.get(user=self.request.user)
        context['action'] = reverse('amiibo-new')
        return context

class DeleteAmiiboView(DeleteView):

    model = Amiibo
    template_name = 'amiibo_delete.html'

    def get_success_url(self):
        return reverse('amiibo-list')

class UpdateAmiiboView(UpdateView):

    model = Amiibo
    template_name = 'edit_amiibo.html'
    fields = '__all__'
    #fields = ('name','series')

    def get_success_url(self):
        return reverse('amiibo-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateAmiiboView,self).get_context_data(**kwargs)
        context['action'] = reverse('amiibo-edit',
                        kwargs={'pk': self.get_object().id})
        return context

class AmiiboView(LoggedInMixin, AmiiboOwnerMixin, DetailView):

    model = Amiibo
    template_name = "amiibo.html"
