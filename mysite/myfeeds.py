from django.contrib.syndication.feeds import Feed
#from mysite.blog.models import Entry#no code yet

class LatestEntries(Feed):
    title = "My Blog"
    link = "/archive/"
    description = "The latest news about stuff."

    def items(self):
        return ['one feed item','another feed item','the third feed item','one feed item']#Entry.objects.order_by('-pub_date')[:5]
    def item_link(self,item):
        return 'www.fakelink.com.zz'
