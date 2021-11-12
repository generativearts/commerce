from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_item", views.new_item, name="new_item"),
    path("p/<str:item_UUID>", views.item_page, name="item_page"),
    path("add_to_favorites/<str:item_UUID>", views.add_to_favorites, name="add_to_favorites"),
    path("favorites", views.favorites, name="favorites"),
    path("favorites/", views.favorites, name="favorites"),
    path("category", views.index, name="category"),
    path("category/<str:category>", views.index, name="index"),
    #path('<slug:slug>/', views.post_detail, name='post_detail'),
]
