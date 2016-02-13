from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from socialnetwork import views as private_views

urlpatterns = [
    #Default route
    url(r'^$', private_views.user_home, name='home'),
    #Route for home page of user
    url(r'^home$', private_views.user_home, name='home'),
    #Route for profile page of other users
    url(r'^profile/(?P<user_id>\d+)$', private_views.user_profile, name='profile'),
    #Route for global stream
    url(r'^global$', private_views.global_home, name='global'),
    #Route for posting user's post
    url(r'^post-item', private_views.post_item, name='post-item'),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', auth_views.login, {'template_name':'login.html'}, name='login'),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', auth_views.logout_then_login, name='logout'),
    # Route to register new user
    url(r'^register$', private_views.register, name='register'),
]
