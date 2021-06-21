from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from django.db.models import Max


class User(AbstractUser):
    pass

class Category(models.Model):
    category = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.category}"

class Listing(models.Model):
    item = models.CharField(max_length=64, help_text="The title displayed for the listing")
    description = models.CharField(max_length=1024, help_text="A longer description displayed for the listing")
    activeFlag = models.BooleanField(default=True)
    dateCreated = models.DateTimeField(default=timezone.now)
    startBid = models.IntegerField(default=0, help_text="What is the starting price displayed for the listing")
    imageURL = models.CharField(max_length=2048, blank=True, help_text="What is the image displayed for the listing")
    owner = models.ForeignKey(User, on_delete=models.PROTECT , related_name ="owner_list")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="similar_items", help_text="This is not required, but this could help your product gain the spotlight it deserves! Examples of categories include Fashion, Toys, Electronics, Home, etc.")
    watchlist = models.ManyToManyField(User, blank=True, related_name="watched_list")

    def current_price(self):
        list = Bids.objects.filter(acution=self).aggregate(Max('offer'))
        return list
        
    def num_of_bids(self):
        return len(self.bids.all())

    def buyer(self):
        list = Bids.objects.filter(acution=self).aggregate(Max('offer'))
        print (self.bids.get(offer=list['offer__max']).buyer)
        return self.bids.get(offer=list['offer__max']).buyer
    
    def __str__(self):
        return f" {self.item} {self.description} {self.activeFlag} {self.dateCreated} {self.startBid} {self.imageURL} {self.owner} {self.category} {self.watchlist}"

class Bids(models.Model):
    acution = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="bids")
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids_makers")
    offer = models.IntegerField()
    
    def __str__(self):
        return f"{self.acution} {self.buyer} {self.offer}"

class Comment(models.Model):
    comment = models.CharField(max_length=2048)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="all_comments")

    def __str__(self):
        return f"{self.comment} {self.user} {self.listing}"

