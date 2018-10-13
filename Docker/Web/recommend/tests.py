from django.test import TestCase

from .models import Alcohol
import random

ans = '1331'


def recommend():
    r = Alcohol.objects.filter(type_name__contains=ans)
    for a in r:
        if r.count() > 1:
            res = r[random.randrange(r.count()-1)]
        else:
            res = a

    print(res.alco_name)


if __name__ == '__main__':
    recommend()
