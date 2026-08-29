from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from apps.accounts.models import CustomUser, PasswordReset


class CustomUserTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='testpass123',
            first_name='Test',
            last_name='User',
        )

    def test_user_creation(self):
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpass123'))

    def test_superuser_creation(self):
        owner = CustomUser.objects.create_superuser(
            email='owner@example.com',
            password='ownerpass123',
        )
        self.assertTrue(owner.is_superuser)


class PasswordResetTestCase(TestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            email='test@example.com',
            password='oldpass123',
        )

    def test_password_reset_generation(self):
        reset = PasswordReset.objects.create(
            user=self.user,
            token=PasswordReset.generate_token(),
            expires_at=timezone.now() + timedelta(hours=24),
        )
        self.assertFalse(reset.used)
        self.assertTrue(reset.is_valid())


class SignupViewTestCase(TestCase):
    def test_signup_page_renders(self):
        from django.urls import reverse
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/signup.html')

    def test_signup_successful(self):
        from django.urls import reverse
        response = self.client.post(reverse('signup'), {
            'email': 'newguy@example.com',
            'first_name': 'New',
            'last_name': 'Guy',
            'password1': 'securepass123',
            'password2': 'securepass123',
        })
        self.assertRedirects(response, reverse('dashboard_home'))
        self.assertTrue(CustomUser.objects.filter(email='newguy@example.com').exists())
