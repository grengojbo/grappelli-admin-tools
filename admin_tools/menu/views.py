from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.simple import direct_to_template

try:
    from django.views.decorators import csrf_exempt
except ImportError:
    from django.contrib.csrf.middleware import csrf_exempt

from forms import BookmarkForm
from models import Bookmark


@login_required
@csrf_exempt
def add_bookmark(request):
    if request.method == "POST":
        form = BookmarkForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            if not request.is_ajax():
                request.user.message_set.create(message='Bookmark added')
            if request.POST.get('next'):
                return HttpResponseRedirect(request.POST.get('next'))
            return HttpResponse('Added')
    else:
        form = BookmarkForm(user=request.user)
    return direct_to_template(request, 'menu/form.html', {
        'form': form,   
        'title': 'Add Bookmark',
    })


@login_required
@csrf_exempt
def edit_bookmark(request, id):
    bookmark = get_object_or_404(Bookmark, id=id)
    if request.method == "POST":
        form = BookmarkForm(user=request.user, data=request.POST, instance=bookmark)
        if form.is_valid():
            form.save()
            if not request.is_ajax():
                request.user.message_set.create(message='Bookmark updated')
            if request.POST.get('next'):
                return HttpResponseRedirect(request.POST.get('next'))
            return HttpResponse('Saved')
    else:
        form = BookmarkForm(user=request.user, instance=bookmark)
    return direct_to_template(request, 'menu/form.html', {
        'form': form,   
        'title': 'Edit Bookmark',
    })


@login_required
@csrf_exempt
def remove_bookmark(request, id):
    bookmark = get_object_or_404(Bookmark, id=id)
    if request.method == "POST":
        bookmark.delete()
        if not request.is_ajax():
            request.user.message_set.create(message='Bookmark removed')
        if request.POST.get('next'):
            return HttpResponseRedirect(request.POST.get('next'))
        return HttpResponse('Deleted')
    return direct_to_template(request, 'menu/delete_confirm.html', {
        'bookmark': bookmark,
        'title': 'Delete Bookmark',
    })
