from django.contrib.auth.models import User
from django.test import TestCase
from . import forms
from django.test import SimpleTestCase
from django.urls import reverse


class LogInTest(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testuser',
            'password': 'secret'}
        User.objects.create_user(**self.credentials)
    def test_login(self):
        # send login data
        response = self.client.post('/login/', self.credentials, follow=True)
        # should be logged in now
        self.assertTrue(response.context['user'].is_active)

class FormsTest(TestCase):

    def PostCreateFormTest(self):
        form = forms.PostCreateForm(title='qwerty',
                                 private=True,
                                 body='')
        self.assertTrue(form.is_valid())

    def PostEditFormTest(self):
        form = forms.PostCreateForm(title='qwerty',
                                 private=True,
                                 body='')
        self.assertTrue(form.is_valid())

    def UserLoginFormTest(self):
        form = forms.PostCreateForm(username='test',
                                    password='test')
        self.assertTrue(form.is_valid())

    def UserRegistrationFormTest(self):
        form = forms.PostCreateForm(username='test',
                                    password='test',
                                    first_name='test',
                                    last_name='test',
                                    confirm_password='test',
                                    email='test@test.com')
        self.assertTrue(form.is_valid())

    def UserEditFormTest(self):
        form = forms.PostCreateForm(username='test',
                                    password='test',
                                    first_name='test',
                                    last_name='test',
                                    email='test@test.com')
        self.assertTrue(form.is_valid())

    def CommentFormTest(self):
        form = forms.PostCreateForm(content='testtsetsetset')
        self.assertTrue(form.is_valid())

    def ProfileFormTest(self):
        form = forms.PostCreateForm()
        self.assertTrue(form.is_valid())

class TestSignup(TestCase):

    def setUp(self):
        pass

    def test_signup_fire(self):
        self.driver.get("https://talkhub.herokuapp.com/")
        self.driver.find_element_by_id('id_title').send_keys("test title")
        self.driver.find_element_by_id('id_body').send_keys("test body")
        self.driver.find_element_by_id('submit').click()
        self.assertIn("https://talkhub.herokuapp.com/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit

class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_home_page_contains_correct_html(self):
        response = self.client.get('/')
        self.assertContains(response, '<h1>Homepage</h1>')

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get('/')
        self.assertNotContains(
            response, 'Hi there! I should not be on the page.')
