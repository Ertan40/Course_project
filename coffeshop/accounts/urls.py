from django.urls import path, include


from coffeshop.accounts.views import IndexView, SignUpView, SignInView, SignOutView, UserDetailsView, UserEditView, \
    UserDeleteView, CreateUpStaffView, AdminIndexView

urlpatterns = (
    path('', IndexView.as_view(), name='index'),
    path('adminstaff/', AdminIndexView.as_view(), name='admin index'), ####
    path('register/', SignUpView.as_view(), name='register user'),
    path('register/staff/', CreateUpStaffView.as_view(), name='register staff user'),
    path('login/', SignInView.as_view(), name='login user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('user/<int:pk>/', include([
        path('', UserDetailsView.as_view(), name='user details'),
        path('edit/', UserEditView.as_view(), name='edit user'),
        path('delete/', UserDeleteView.as_view(), name='delete user'),
    ]))
)