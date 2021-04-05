from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .models import DiscussSide, DiscussTheme, User, DiscussionComment
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import JsonResponse

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
        tmp_user = request.POST['name']
        user = User(name=tmp_user, create_date=timezone.now())
        user.save()
    except (KeyError):
        # Redisplay the discussion side_selection form.
        return render(request, 'discuss/detail.html', {
            'discuss_theme': discuss_theme,
            'error_message': "You didn't select a side.",
        })
    else:
        selected_side.side_count += 1
        selected_side.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('discuss:waiting', args=(discuss_theme.id, )))

def waiting(request, discuss_theme_id):
    discuss_theme = get_object_or_404(DiscussTheme, pk=discuss_theme_id)
    return render(request, 'discuss/waiting.html', {'discuss_theme': discuss_theme})

class DiscussionCommentList(generic.ListView):
    model = DiscussionComment

def discussion(request, discuss_theme_id):
    comment = request.POST.get('comment')
    post = DiscussionComment.objects.create(discuss_side=DiscussSide.objects.get(pk=2), user=User.objects.get(pk=3), comment=comment)
    d = {
        'comment': post.comment,
    }
    return JsonResponse(d)
