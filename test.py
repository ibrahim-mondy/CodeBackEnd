from rest_framework.test import APIRequestFactory

factory = APIRequestFactory()

request = factory.post('/notes/', {'title': 'new note'})


from django.test import TestCase
from myapp.models import Animal

class AnimalTestCase(TestCase):
    def setUp(self):
        # إنشاء بيانات اختبار
        Animal.objects.create(name="lion", sound="Roar")
        Animal.objects.create(name="cat", sound="Meow")

    def test_animals_can_speak(self):
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")

        self.assertEqual(lion.speak(), 'The lion says "Roar"')
        self.assertEqual(cat.speak(), 'The cat says "Meow"')
