# Write a decorator that takes a list of stop words and replaces in them
# with * inside decorated function


def stop_words(words: list):
    def decorator(func):
        def wripper(*args, **kwargs):
            slogan = func(*args, **kwargs)
            for word in words:
                if word in slogan:
                    slogan = slogan.replace(word, '*')
            return slogan
        return wripper
    return decorator


@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
