from django.core.exceptions import ValidationError
from django.test import TestCase

from django.contrib.auth import get_user_model

UserModel = get_user_model()


class ProfileModelTests(TestCase):
    def test_profile_save__with_first_name_only_letters__expect_correct_result(self):
        profile = UserModel(
            username="test01",
            password="Testpass@123!",
            age=38,
            email="test@mail.com",
            first_name="firstname",
            last_name="lastname",
        )
        profile.full_clean()
        profile.save()
        self.assertIsNotNone(profile.pk)

    def test_profile_save__with_first_name_with_numbers__expect_validation_error(self):
        profile = UserModel(
            username="test01",
            password="Testpass@123!",
            age=38,
            email="test@mail.com",
            first_name="firstname01",
            last_name="lastname",
        )

        with self.assertRaises(ValidationError) as ve:
            profile.full_clean()
            profile.save()
        self.assertIsNotNone(ve.exception)