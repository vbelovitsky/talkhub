# """test.py"""
# from django.test import TestCase
# from django.test import SimpleTestCase
# from blogapp.forms import *
# from .models import *
# from django.urls import reverse
#
#
# class LogInTest(TestCase):
#     """login test"""
#     def setUp(self):
#         """test"""
#         self.credentials = {
#             'username': 'testuser',
#             'password': 'secret'}
#         User.objects.create_user(**self.credentials)
#
#     def test_login(self):
#         """test"""
#         # send login data
#         response = self.client.post('/login/', self.credentials, follow=True)
#         # should be logged in now
#         self.assertTrue(response.context['user'].is_active)
#
#
# class FormsTest(TestCase):
#     """forms test"""
#     def PostCreateFormTest(self):
#         """test"""
#         form = forms.PostCreateForm(title='qwerty',
#                                     private=True,
#                                     body='')
#         self.assertTrue(form.is_valid())
#
#     def PostEditFormTest(self):
#         """test"""
#         form = forms.PostCreateForm(title='qwerty',
#                                     private=True,
#                                     body='')
#         self.assertTrue(form.is_valid())
#
#     def UserLoginFormTest(self):
#         """test"""
#         form = forms.PostCreateForm(username='test',
#                                     password='test')
#         self.assertTrue(form.is_valid())
#
#     def UserRegistrationFormTest(self):
#         """test"""
#         form = forms.PostCreateForm(username='test',
#                                     password='test',
#                                     first_name='test',
#                                     last_name='test',
#                                     confirm_password='test',
#                                     email='test@test.com')
#         self.assertTrue(form.is_valid())
#
#     def UserEditFormTest(self):
#         """test"""
#         form = forms.PostCreateForm(username='test',
#                                     password='test',
#                                     first_name='test',
#                                     last_name='test',
#                                     email='test@test.com')
#         self.assertTrue(form.is_valid())
#
#     def CommentFormTest(self):
#         """test"""
#         form = forms.PostCreateForm(content='testtsetsetset')
#         self.assertTrue(form.is_valid())
#
#     def ProfileFormTest(self):
#         """test"""
#         form = forms.PostCreateForm()
#         self.assertTrue(form.is_valid())
#
#
# class TestSignup(TestCase):
#     """register test"""
#     def setUp(self):
#         """test"""
#         pass
#
#     def test_signup_fire(self):
#         """test"""
#         self.driver.get("https://talkhub.herokuapp.com/")
#         self.driver.find_element_by_id('id_title').send_keys("test title")
#         self.driver.find_element_by_id('id_body').send_keys("test body")
#         self.driver.find_element_by_id('submit').click()
#         self.assertIn("https://talkhub.herokuapp.com/", self.driver.current_url)
#
#     def tearDown(self):
#         """test"""
#         self.driver.quit
#
#
# class HomePageTests(SimpleTestCase):
#     """main page test"""
#     def test_home_page_status_code(self):
#         """test"""
#         response = self.client.get('/')
#         self.assertEquals(response.status_code, 200)
#
#     def test_view_url_by_name(self):
#         """test"""
#         response = self.client.get(reverse('home'))
#         self.assertEquals(response.status_code, 200)
#
#     def test_view_uses_correct_template(self):
#         """test"""
#         response = self.client.get(reverse('home'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'base.html')
#
#     def test_home_page_contains_correct_html(self):
#         """test"""
#         response = self.client.get('/')
#         self.assertContains(response, '<h1>Homepage</h1>')
#
#     def test_home_page_does_not_contain_incorrect_html(self):
#         """test"""
#         response = self.client.get('/')
#         self.assertNotContains(
#             response, 'Hi there! I should not be on the page.')
