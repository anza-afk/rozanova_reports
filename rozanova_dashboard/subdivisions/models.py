from django.db import models


class APPSubdivision(models.Model):
    title = models.CharField(
        verbose_name="Наименование подразделения",
        max_length=30
    )

    class Meta:
        verbose_name = 'Амбулаторно-поликлиническое подразделение'
        verbose_name_plural = 'Амбулаторно-поликлинические подразделения'

    def __str__(self):
        return self.title


class ChildSubdivision(models.Model):
    title = models.CharField(
        verbose_name="Наименование подразделения",
        max_length=30
    )

    class Meta:
        verbose_name = 'Детская поликлиника'
        verbose_name_plural = 'Детские поликлиники'

    def __str__(self):
        return self.title


class WomenConsSubdivision(models.Model):
    title = models.CharField(
        verbose_name="Наименование подразделения",
        max_length=30
    )

    class Meta:
        verbose_name = 'Женская консультация'
        verbose_name_plural = 'Женские консультации'

    def __str__(self):
        return self.title


class StomatologySubdivision(models.Model):
    title = models.CharField(
        verbose_name="Наименование подразделения",
        max_length=30
    )

    class Meta:
        verbose_name = 'Стоматологическое подразделение'
        verbose_name_plural = 'Стоматологические подразделения'

    def __str__(self):
        return self.title


class OncologySubdivision(models.Model):
    title = models.CharField(
        verbose_name="Наименование подразделения",
        max_length=30
    )

    class Meta:
        verbose_name = 'Онкологическое подразделение'
        verbose_name_plural = 'Онкологические подразделения'

    def __str__(self):
        return self.title


class HospitalSubdivision(models.Model):
    title = models.CharField(
        verbose_name="Наименование подразделения",
        max_length=30
    )

    class Meta:
        verbose_name = 'подразделение Стационара'
        verbose_name_plural = 'подразделения Стационара'

    def __str__(self):
        return self.title
