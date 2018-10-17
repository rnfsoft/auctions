from auctions_ops.models import *
from django.utils import timezone

class Management:
    log = None

    def __init__(self, title):
        self.log = ManagementLog(task=title, count=0, started=timezone.now(), state=1)
        self.log.save()

    def in_progress(self):
        self.log.state = 2
        self.log.save()

    def update_count(self, x):
        self.log.count = x
        self.log.save()

    def completed(self):
        self.log.state = 3
        self.log.finished = timezone.now()
        self.log.save()
        