from functools import wraps
from django.shortcuts import redirect

def staff_required(view_func):
    @wraps(view_func)
    def wrapped(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return wrapped




# from django.http import HttpResponseForbidden
# from functools import wraps

# def staff_required(view_func):
#     @wraps(view_func)
#     def _wrapped_view(request, *args, **kwargs):
#         if not request.user.is_authenticated or not request.user.is_staff:
#             return HttpResponseForbidden("You do not have permission to access this page.")
#         return view_func(request, *args, **kwargs)
    
#     return _wrapped_view