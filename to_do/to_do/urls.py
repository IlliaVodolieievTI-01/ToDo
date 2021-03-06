# from django.conf import settings
from django.urls import include, path
# from django.conf.urls.static import static
from django.contrib import admin

# from .yasg import urlpatterns as dock_urls
# from rest_framework_jwt.views import obtain_jwt_token
# from rest_framework.routers import DefaultRouter
# from store_api.views import CategoryViewSet, AuthorViewSet
# from rest_framework.schemas import get_schema_view
# from rest_framework.documentation import include_docs_urls
# from rest_framework_swagger.views import get_swagger_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api", include("to_do_api.urls")),
    # path("api/accounts/", include("accounts.urls")),
    # path("api/comments/", include("comments.urls")),
    path("", include("to_do_app.urls")),

    # path("api/auth/token/", obtain_jwt_token),
    # path("api/category/", include(router.urls)),
    # path("api/author/", include(router2.urls)),
    # path("api/schema/", schema_view),
    # path("api/docs/", include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    # path('swagger/', schema_view),
]
