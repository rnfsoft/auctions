from django.db import models

from accounts.models import User

# Create your models here.
class AuctionManager(models.Manager):
    def active(self):
        return super().get_queryset().filter(active=True)

    def expired(self):
        return super().get_queryset().filter(active=False)


class Auction(models.Model):
    title = models.CharField(max_length=255)
    current_bid = models.FloatField()
    bid_count = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    live_date = models.DateTimeField()
    expiry_date = models.DateTimeField()
    active = models.BooleanField()
    owner = models.ForeignKey(User, on_delete=None)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

    objects = models.Manager()
    AuctionManager = AuctionManager()


class BidManager(models.Manager):
    def current(self, auction):
        return super().get_queryset().filter(auction=auction).order_by('-created_at')


class Bid(models.Model):
    auction = models.ForeignKey(Auction, on_delete=None)
    value = models.FloatField()
    owner = models.ForeignKey(User, on_delete=None)
    created_at = models.DateTimeField(auto_now_add=True)
    email_sent = models.BooleanField(default=False)
    email_sent_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "{0} - {1}".format(self.auction, self.value)

    objects = models.Manager()
    BidManager = BidManager()

class EmailManager(models.Manager):
    def emails(self):
        return super().get_queryset().order_by('-created_at')

class EmailQueue(models.Model):
    auction = models.ForeignKey(Auction, on_delete=None, blank=True, null=True)
    bid = models.ForeignKey(Bid, on_delete=None, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    EmailManager = EmailManager()