from django.urls import path


from post.views import ContactView, BlockView

app_name = 'post'

urlpatterns = [
    path('blog/', BlockView.as_view(), name='block'),
    # path('', BlockDetailsView.as_view(), name='block-detail'),

]