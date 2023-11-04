from django.conf import settings


def tougshire_auth(request):
    return {"tougshire_auth": settings.TOUGSHIRE_AUTH}
