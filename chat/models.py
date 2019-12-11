from django.db import models

class Room(models.Model):
    """
    A room for people to chat in.
    """

    # Room title
    title = models.CharField(max_length=255)
    # If only "staff" users are allowed (is_staff on django's User)
    staff_only = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    @property
    def group_name(self):
        """
        Returns the Channels Group name that sockets should subscribe to to get sent
        messages as they are generated.
        """
        return "room-%s" % self.id

class Messages(models.Model):
   text = models.CharField(max_length=255,default="")
   datetime = models.DateTimeField(auto_now_add=True)
   sender_id = models.IntegerField(default=0)
   room = models.ForeignKey(Room,on_delete=models.CASCADE)
   star = models.CharField(max_length=255,default="unstar")
