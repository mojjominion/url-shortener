import random
import string

def generate_key(size=9, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for i in range(size))

def create_key(instance, size=9):
    if not instance.random_key or instance.random_key=='':
        new_key = generate_key(size=size)
    else:
        new_key = instance.random_key
    Urlclass  = instance.__class__
    query_set_exists = Urlclass.objects.filter(random_key=new_key).exists()
    if query_set_exists and new_key!=instance.random_key:
        return create_key(instance, size=size)
    return new_key