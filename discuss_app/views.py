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
        selected_side = request.POST['side-choice']
    except (KeyError):
        # Redisplay the question voting form.
        return render(request, 'discuss/detail.html', {
            'discuss_theme': discuss_theme,
            'error_message': "You didn't select a side.",
        })
    else:
        if selected_side == discuss_theme.one_side:
            discuss_theme.one_side_count += 1
        if selected_side == discuss_theme.another_side:
            discuss_theme.another_side_count += 1
        
        discuss_theme.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('discuss:results', args=(discuss_theme.id,)))

def results(request, discuss_theme_id):
    discuss_theme = get_object_or_404(DiscussTheme, pk=discuss_theme_id)
    return render(request, 'discuss/results.html', {'discuss_theme': discuss_theme})