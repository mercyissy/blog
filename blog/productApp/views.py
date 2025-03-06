from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Blog
from .forms import BlogForm
from blog.userApp.models import Profile
from .decorators  import staff_required
from django.core.mail import send_mail
from django.contrib import messages
from django.views.generic import ListView

@staff_required      
@login_required
def add_blog(request):
    addedby = get_object_or_404(Profile, user_id=request.user.id)
    if request.method == 'POST':
        blog_form = BlogForm(request.POST, request.FILES)
        if blog_form.is_valid():
            form = blog_form.save(commit=False)
            form.addedby = addedby
            try: 
                
                send_mail(
                    subject= f'New Product Added by {addedby.user.first_name} {addedby.user.last_name}',
                    message= 'Hello Admin, A new blog has be added Kindly approve or decline.',
                    from_email='admin@example.com',
                    recipient_list=['admin@example.com'],
                    fail_silently=False
                )
                
                send_mail(
                    subject= f'New Blog Added by You',
                    message= 'Hello, You added a new blog. you will be notified once it is approved.',
                    from_email='admin@example.com',
                    recipient_list=[addedby.user.email],
                    fail_silently=False
                    
                )
                
                form.save()
                messages.success(request, 'Blog Added Successfully')
                
                
            except:
                messages.error(request, 'Error sending email, hence blog not added')
                
        else:
            print(blog_form.errors)
            messages.error(request, 'Error adding blog')
        
        return redirect('add-blog')
        
    else:
        blog_form = BlogForm()
        return render(request, template_name='add_blog.html', context={'blog_form':blog_form})
            
            
            
        


def home(request):
    blogs = Blog.objects.all().filter(approved=True)
    return render(request, template_name='index.html', context={'all_blog': blogs})

def viewblog(request, blog_id):
    blogs = Blog.objects.get(id=blog_id)
    return render(request, template_name='viewblog.html', context={'blog': blogs})

@staff_required
@login_required
def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    blog.delete()
    messages.success(request, 'Blog deleted successfully')
    return redirect('home')

   

@staff_required      
@login_required
def edit_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)


    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('view-blog', blog_id=blog.id)
        else:
            print(form.errors)

    else:
        form = BlogForm(instance=blog)

    return render(request, 'add_blog.html', {'form': form})


@staff_required      
@login_required
def viewAllBlogs(request):
    blogs = Blog.objects.all()  # Retrieve all blogs
    return render(request, 'viewAllBlogs.html', {'all_blog': blogs})

@staff_required
@login_required
def approve_reject_blog(request, blog_id, action):
    blog = get_object_or_404(Blog, id=blog_id)

    if action == 'approve':
        blog.approved = True
    elif action == 'reject':
        blog.approved = False

    blog.save()
    return redirect('view-all-blogs')
