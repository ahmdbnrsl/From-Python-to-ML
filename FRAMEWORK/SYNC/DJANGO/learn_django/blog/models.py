from django.db import models

class Artikel(models.Model):
    judul = models.CharField(max_length=100)
    isi = models.TextField()
    tanggal_publikasi = models.DateTimeField(auto_now_add=True)