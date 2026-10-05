from functools import wraps

is_logged_in = True

def require_login(func):
    @wraps(func)
    def wrapper():
        if is_logged_in:
            func()
        else:
            print("Access denied. Please login.")

    return wrapper


@require_login
def dashboard():
    print("Welcome to the dashboard!")


dashboard()

# Output:
# Welcome to the dashboard!
