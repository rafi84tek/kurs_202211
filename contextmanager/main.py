"""
menader do obsługi plików

"""

class ContextManager:
    #obowiązkowe funkcje init, enter, exit
    def __init__(self):
        print("Inicjacja funkcji init()")

    def __enter__(self):
        print("Inicjacja funkcji enter()")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Inicjacja funkcji exit()")

with ContextManager() as manager:
    print("Blok wykonawczy w instrukcji with")