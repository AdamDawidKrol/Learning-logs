from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry, MainTopic
from .forms import TopicForm, EntryForm, MainTopicForm

def index(request):
    """The home page for Learning Log"""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show all topics"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def main_topics(request):
    """Show all main topics"""
    main_topics = MainTopic.objects.filter(owner=request.user).order_by('date_added')
    context = {'main_topics' : main_topics}
    return render(request, 'learning_logs/main_topics.html', context)

@login_required
def topic(request, topic_id):
    """Show one topic"""
    topic = Topic.objects.get(id = topic_id)
    main_topic = topic.main_topic
    #if topic.owner != request.user:
        #raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic' : topic, 'entries' : entries, 'main_topic' : main_topic}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def main_topic(request, maintopic_id):
    """Show one topic"""
    zupa = maintopic_id
    maintopic = MainTopic.objects.get(id = maintopic_id)
    if maintopic.owner != request.user:
        raise Http404
    topics = maintopic.topic_set.order_by('text')
    context = {'maintopic' : maintopic, 'topics' : topics, 'zupa' : zupa}
    return render(request, 'learning_logs/main_topic.html', context)

@login_required
def new_topic(request, maintopic_id):
    """Create new topic"""
    maintopic = MainTopic.objects.get(id=maintopic_id)
    maintopicid = maintopic.id
    if request.method != "POST":
        form = TopicForm()
    else:
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.main_topic = maintopic
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:main_topic', args=[maintopic_id]))
    context = {'form' : form, 'maintopic' : maintopic, 'maintopicid' : maintopicid}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_main_topic(request):
    """Create new main topic"""
    if request.method != "POST":
        form = MainTopicForm()
    else:
        form = MainTopicForm(request.POST)
        if form.is_valid():
            new_main_topic = form.save(commit=False)
            new_main_topic.owner = request.user
            new_main_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:main_topics'))
    context = {'form' : form}
    return render(request, 'learning_logs/new_main_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Create new entry"""
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    
    if request.method != "POST":
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))
    context = {'form' : form, 'topic' : topic}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit existing entry"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id]))
    context = { 'entry' : entry, 'form' : form, 'topic' : topic}
    return render(request,  'learning_logs/edit_entry.html', context)

@login_required
def delete_entry(request, entry_id):
    """Delete entry"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404
    
    entry.delete()
    
    context = {'topic' : topic}
    
    return render(request, 'learning_logs/base.html')
    
