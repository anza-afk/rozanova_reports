
from django.core.validators import MaxValueValidator
from django.db import models

from subdivisions.models import (APPSubdivision,
                                 ChildSubdivision,
                                 HospitalSubdivision,
                                 OncologySubdivision,
                                 StomatologySubdivision,
                                 WomenConsSubdivision)


class APPReport(models.Model):
    subdivision = models.ForeignKey(
        to=APPSubdivision,
        verbose_name='reports',
        on_delete=models.CASCADE
    )

    time = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Отчёт {self.subdivision}, ({self.time})'


class ChildReport(models.Model):
    subdivision = models.ForeignKey(
        to=ChildSubdivision,
        verbose_name='reports',
        on_delete=models.CASCADE
    )

    time = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Отчёт {self.subdivision}, ({self.time})'


class WomenConsReport(models.Model):
    subdivision = models.ForeignKey(
        to=WomenConsSubdivision,
        verbose_name='reports',
        on_delete=models.CASCADE
    )
    timely_medication_provision = models.PositiveIntegerField(
        verbose_name=('Своевременное обеспечение беременных лекарственными '
                      'препаратами за счет средств родовых сертификатов '
                      '(витаминами)'),
        validators=[
            MaxValueValidator(5)
        ]
    )
    doctor_availability = models.PositiveIntegerField(
        verbose_name='Доступность врачей акушеров-гинекологов',
        validators=[
            MaxValueValidator(5)
        ]
    )
    complaints = models.PositiveIntegerField(
        verbose_name='Жалобы (своевременный ответ в днях)',
        validators=[
            MaxValueValidator(5)
        ]
    )
    timely_screening_referral = models.PositiveIntegerField(
        verbose_name=('Своевременное направление на пренатальный скрининг'
                      '(первый и второй)'),
        validators=[
            MaxValueValidator(5)
        ]
    )
    timely_childbirth_referral = models.PositiveIntegerField(
        verbose_name=('Своевременное направление на роды в зависимости'
                      'от установленной степени риска'),
        validators=[
            MaxValueValidator(5)
        ]
    )
    reducing_requests_number = models.PositiveIntegerField(
        verbose_name='Снижение количества обращений',
        validators=[
            MaxValueValidator(5)
        ]
    )
    schedule_for_weeks = models.PositiveIntegerField(
        verbose_name='Формирование расписания врачей на 3 недели вперед',
        validators=[
            MaxValueValidator(5)
        ]
    )
    doctor_digital_signatures = models.PositiveIntegerField(
        verbose_name='Электронные цифровые подписи врачей',
        validators=[
            MaxValueValidator(5)
        ]
    )
    telemed_consultations_protocol = models.PositiveIntegerField(
        verbose_name=('Протокол Телемедицинских консультаций Врач-Пациент) '
                      'в женской консультации'),
        validators=[
            MaxValueValidator(5)
        ]
    )
    templates_using = models.PositiveIntegerField(
        verbose_name='Использование шаблонов по акушерству и гинекологии',
        validators=[
            MaxValueValidator(5)
        ]
    )
    time = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'

    def __str__(self):
        return f'Отчёт {self.subdivision}, ({self.time})'


class OncologyReport(models.Model):
    subdivision = models.ForeignKey(
        to=OncologySubdivision,
        verbose_name='reports',
        on_delete=models.CASCADE
    )

    time = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Отчёт {self.subdivision}, ({self.time})'


class StomatologyReport(models.Model):
    subdivision = models.ForeignKey(
        to=StomatologySubdivision,
        verbose_name='reports',
        on_delete=models.CASCADE
    )
    patient_feedback = models.PositiveIntegerField(
        verbose_name='Обратная связь пациента',
        validators=[
            MaxValueValidator(5)
        ]
    )
    complaints = models.PositiveIntegerField(
        verbose_name='Жалобы (своевременный ответ в днях)',
        validators=[
            MaxValueValidator(5)
        ]
    )
    patient_non_attendance = models.PositiveIntegerField(
        verbose_name='Неявки на прием врача',
        validators=[
            MaxValueValidator(5)
        ]
    )
    doctor_availability = models.PositiveIntegerField(
        verbose_name=('Доступность врачей стоматологов (стоматологи'
                      ' терапевтические, стоматологи детские)'),
        validators=[
            MaxValueValidator(5)
        ]
    )
    cancer_screening_plan = models.PositiveIntegerField(
        verbose_name='Мониторинг исполнения плана по онкоскринингу',
        validators=[
            MaxValueValidator(5)
        ]
    )
    reducing_requests_number = models.PositiveIntegerField(
        verbose_name='Снижение количества обращений',
        validators=[
            MaxValueValidator(5)
        ]
    )
    schedule_for_weeks = models.PositiveIntegerField(
        verbose_name='Формирование расписания врачей на 3 недели вперед',
        validators=[
            MaxValueValidator(5)
        ]
    )
    insurance_plan = models.PositiveIntegerField(
        verbose_name=('Выполнение объемов обязательного медицинского '
                      'страхования'),
        validators=[
            MaxValueValidator(5)
        ]
    )
    templates_using = models.PositiveIntegerField(
        verbose_name='Мониторинг использования шаблонов по стоматологии',
        validators=[
            MaxValueValidator(5)
        ]
    )
    time = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Отчёт {self.subdivision}, ({self.time})'


class HosiltalReport(models.Model):
    subdivision = models.ForeignKey(
        to=HospitalSubdivision,
        verbose_name='reports',
        on_delete=models.CASCADE
    )

    time = models.DateTimeField(
        auto_now_add=True,
        null=True,
        blank=True
    )

    def __str__(self):
        return f'Отчёт {self.subdivision}, ({self.time})'
