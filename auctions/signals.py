from django.dispatch import receiver
from django.db.models.signals import post_save


from .models import *
#from .auctions_classes.bidding_actions import BiddingActions


@receiver(post_save, sender=Bid)
def update_auction_totals_for_bid(sender, instance, created, **kwargs):
    if created:
        auction = instance.auction
        auction.bid_count = Bid.BidManager.current(auction).count()
        auction.current_bid = instance.value
        auction.save()
        
        EmailQueue(auction=auction, bid=instance).save()

        print (instance)
      
        #EmailQueue(bid=sender.bid).save()
        # bid = BiddingActions(instance.auction)
        # print(instance.auction)
        # bid.update_auction(instance.value)
        # bid.send_email()


