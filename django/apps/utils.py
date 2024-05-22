from django.shortcuts import redirect


def snake_case_to_title(snake_case_string, decorator='* '):
    # Split the snake case string into words
    words = snake_case_string.split('_')
    # Capitalize the first word and lowercase the rest, then join them with a space
    title_case_string = ' '.join(words[0].capitalize() if i == 0 else word for i, word in enumerate(words))
    return title_case_string + decorator

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('dashboard')
        return wrapper_func
    return decorator