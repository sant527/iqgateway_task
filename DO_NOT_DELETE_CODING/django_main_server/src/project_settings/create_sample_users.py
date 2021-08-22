from django.contrib.auth import get_user_model
User = get_user_model()
user = User.objects.create_user('u000', password='123')
user.is_allowed_to_fetch = True
user.save()
user = User.objects.create_user('u001', password='123')
user.is_allowed_to_fetch = False
user.save()
user = User.objects.create_user('u002', password='123')
user.is_allowed_to_fetch = True
user.save()
user = User.objects.create_user('u003', password='123')
user.is_allowed_to_fetch = False
user.save()
user = User.objects.create_user('u004', password='123')
user.is_allowed_to_fetch = True
user.save()
user = User.objects.create_user('u005', password='123')
user.is_allowed_to_fetch = False
user.save()
user = User.objects.create_user('u006', password='123')
user.is_allowed_to_fetch = True
user.save()
user = User.objects.create_user('u007', password='123')
user.is_allowed_to_fetch = False
user.save()
user = User.objects.create_user('u008', password='123')
user.is_allowed_to_fetch = True
user.save()