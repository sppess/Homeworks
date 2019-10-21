# Write a decorator arg_rules that validates arguments passed to the function
# A decorator should take 3 arguments:
#   max_length: 15
#   type_: str
#   contains: []  - list of symbols that an argument should contain
#
# If some of the rules' checks returns False, the function should return False
# and print the reason it failed
#
# Otherwise return result


def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wripper(*args, **kwargs):

            for arg in args:
                if type(arg) != type_:
                    mistake = f"Type is {type(args)}"
                    print(mistake)
                    return False

                else:
                    if len(arg) > max_length:
                        mistake = f"Length is {len(arg)}"
                        print(mistake)
                        return False

                    for symb in contains:
                        if symb not in arg:
                            mistake = f"Name isn't contain {symb}"
                            print(mistake)
                            return False

            return func(*args)
        return wripper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'
