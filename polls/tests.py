from django.test import TestCase
from polls.models import A


class ATest(TestCase):

    def setUp(self):
        A.objects.create(a='abc', b=1)
        A.objects.create(a='def', b=2)

    def test_a(self):
        abc = A.objects.get(b=1)
        self.assertEqual(
            abc.get_a(), "abc")
