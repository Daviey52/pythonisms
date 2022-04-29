from functools import wraps

def yes_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'Alright, "{orig_val}" Yes!! that\'s perfect'

    return wrapper


@yes_decorator
def playoff_games(game):
  return game
