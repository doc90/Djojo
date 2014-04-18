from django.shortcuts import render
from django.views.generic.edit import DeleteView
from django.views import generic
from django.contrib.auth.decorators import permission_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.core.urlresolvers import reverse_lazy

from .models import Document


@permission_required('documents.view_documents', raise_exception=True)
def documents_list(request):
    document_list = Document.objects.order_by('title')
    paginator = Paginator(document_list, 25)

    page = request.GET.get('page')
    try:
        document_list = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        document_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        document_list = paginator.page(paginator.num_pages)

    return render_to_response('documents/document_list.html', {"document_list": document_list},
                              context_instance=RequestContext(request))


class Add_document(generic.CreateView):
    model = Document
    fields = ['title', 'uploadedfile']
    template_name = 'documents/document_add.html'
    success_url = reverse_lazy('documents:list')


class Edit_document(generic.UpdateView):
    model = Document
    fields = ['title', 'uploadedfile']
    template_name = 'documents/document_edit.html'
    success_url = reverse_lazy('documents:list')


class Delete_document(generic.DeleteView):
    model = Document
    success_url = reverse_lazy('documents:list')
    template_name = 'documents/document_delete.html'

    def dispatch(self, *args, **kwargs):
        return super(Delete_document, self).dispatch(*args, **kwargs)

