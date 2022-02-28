from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm,PasswordResetForm,MySetPasswordForm
urlpatterns = [
    path('', views.ProductView.as_view(), name='home'),
    path('product-detail/<int:pk>',
         views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword.html',
         form_class=MyPasswordChangeForm, success_url='/changepassword_done/'), name='changepassword'),
    path('changepassword_done/', auth_views.PasswordChangeView.as_view(template_name='app/changepassword_done.html',
         form_class=MyPasswordChangeForm), name='changepassword_done'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password-reset.html',
          form_class = PasswordResetForm),name='password-reset'),

    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password-reset-done.html'),name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password-confirm.html',form_class = MySetPasswordForm),name='password_reset_confirm'),

    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='app/password-reset-successfully.html'),name='password_reset_complete'),

    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html',
         authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('registration/', views.CustomerResistrationView.as_view(),
         name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
