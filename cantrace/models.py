from django.db import models


class Trace(models.Model):
    name = models.CharField(max_length=30, unique=True)
    comments = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Channel(models.Model):
    trace = models.ForeignKey(Trace, related_name='channels', on_delete=models.CASCADE)
    canChannel = models.IntegerField()

    def __str__(self):
        return str(self.canChannel)


class Message(models.Model):
    channel = models.ForeignKey(Channel, related_name='messages', on_delete=models.CASCADE)
    can_id_decimal = models.IntegerField()
    name = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return str(self.channel.trace) + '-CH' + str(self.channel) + '-' + str(self.can_id_decimal)


class Frame(models.Model):
    message = models.ForeignKey(Message, related_name='frames', on_delete=models.CASCADE)
    time = models.DecimalField(max_digits=10, decimal_places=6)
    data_length = models.IntegerField()

    def __str__(self):
        return str(self.message) + '-' + str(self.time)


class Data(models.Model):
    frame = models.ForeignKey(Frame, on_delete=models.CASCADE)
    byte_id = models.IntegerField()
    hex_data = models.CharField(max_length=2)
    dec_data = models.IntegerField()





