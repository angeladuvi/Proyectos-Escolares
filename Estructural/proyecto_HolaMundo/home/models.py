from django.db import models

# Create your models here.
class Paciente(models.Model):

    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Paciente")
        verbose_name_plural = ("Pacientes")

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
     #   return reverse("Paciente_detail", kwargs={"pk": self.pk})

class tessiu(models.Model):

    temperature = models.FloatField(verbose_name="temperatura")
    color = models.FloatField()
    inflamation = models.FloatField(verbose_name="inflamacion")
    name = models.ForeignKey(Paciente, on_delete=models.CASCADE,blank=True, null=True)
    
    

    class Meta:
        verbose_name = "tejido"
        verbose_name_plural = "tejidos"

    def __str__(self):
        return 'temperatura: '+ str(self.temperature) + ' color: ' + str(self.color) + ' inflamacion: ' + str(self.temperature) 

   # def get_absolute_url(self):
        return reverse ("tessiu_detail", kwargs={"pk": self.pk})



