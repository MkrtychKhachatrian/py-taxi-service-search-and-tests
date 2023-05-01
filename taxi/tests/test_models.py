from django.contrib.auth import get_user_model
from django.test import TestCase

from taxi.models import Manufacturer, Car


class ModelsTests(TestCase):
    def setUp(self):
        self.manufacturer = Manufacturer.objects.create(
            name="Porsche", country="Germany"
        )

        self.driver = get_user_model().objects.create_user(
            username="test username",
            password="test123",
            first_name="test first",
            last_name="test last",
            license_number="TST12345"
        )

        self.car = Car.objects.create(
            model="Porsche 911", manufacturer=self.manufacturer
        )

    def test_manufacturer_str(self):
        self.assertEqual(
            str(self.manufacturer),
            f"{self.manufacturer.name} {self.manufacturer.country}"
        )

    def test_driver_str(self):
        self.assertEqual(
            str(self.driver),
            f"{self.driver.username} "
            f"({self.driver.first_name} {self.driver.last_name})"
        )

    def test_car_str(self):
        self.assertEqual(str(self.car), self.car.model)

    def test_create_driver_with_license_number(self):
        username = "test username"
        password = "test123"
        license_number = "TST12345"

        self.assertEqual(self.driver.username, username)
        self.assertTrue(self.driver.check_password(password))
        self.assertEqual(self.driver.license_number, license_number)

    def test_driver_get_absolute_url(self):
        self.assertEqual(self.driver.get_absolute_url(), "/drivers/1/")
