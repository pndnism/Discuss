from django.http import HttpResponse, HttpResponseRedirect
from .models import DiscussTheme
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'discuss/index.html'
    context_object_name = 'latest_discuss_theme_list'

    def get_queryset(self):
        """Return the last ten published discussions."""
        return DiscussTheme.objects.order_by('-create_date')[:10]

def detail(request, discuss_theme_id):
    discuss_theme = get_object_or_404(DiscussTheme, pk=discuss_theme_id)
    return render(request, 'discuss/detail.html', {'discuss_theme': discuss_theme})

def entry(request, discuss_theme_id):
    discuss_theme = get_object_or_404(DiscussTheme, pk=discuss_theme_id)
    try:
        selected_side = discuss_theme.discussside_set.get(pk=request.POST['side-choice'])
        user_name = request.POST['user_name']
        request.session['user_name'] = user_name    
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'discuss/detail.html', {
            'discuss_theme': discuss_theme,
            'error_message': "You didn't select a side or enter your name.",
        })
    else:
        selected_side.side_count += 1
        selected_side.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('discuss:waiting', args=(discuss_theme.id,)))

def waiting(request, discuss_theme_id):
    discuss_theme = get_object_or_404(DiscussTheme, pk=discuss_theme_id)
    return render(request, 'discuss/waiting.html', {'discuss_theme': discuss_theme})