from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from .forms import CreateForm

# Create your views here.
def home(request):
    post = Post.objects.all()
    return render(request, 'crudpra/home.html',{'post':post})

def create(request, post = None):
    if request.method == 'POST':
        form = CreateForm(request.POST, instance=post)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('home')
    else:
        form = CreateForm(instance=post)
        return render(request, 'crudpra/new.html', {'form':form})

def update(request, pk):
    post = get_object_or_404(Post,pk=pk)
    return create(request,post)

def delete(request, pk):
    post = get_object_or_404(Post,pk=pk)
    post.delete()
    return redirect('home')
    
    
