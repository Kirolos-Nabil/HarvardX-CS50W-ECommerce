from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create_listing", views.create_listing, name="create listing"),
    path("listing-page/<int:listing_id>", views.listing_page, name="listing page"),
    path("create-bid/<int:listing_id>", views.create_bid, name="create bid"),
    path("close-listing/<int:listing_id>", views.close_listing, name="close listing"),
    path("watchlist-page", views.watchlist_page, name="watchlist page"),
    path("watchlist-action/<int:listing_id>", views.watchlist_action, name="watchlist action"),
    path("make-comment/<int:listing_id>", views.make_comment, name="leave comment"),
    path("categories", views.category, name="category listing"),
    path("categories/<str:category>", views.filtered_category, name='category index'),
    path("closed-listing", views.closed_listing, name="closed listing")
]
