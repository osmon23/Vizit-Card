from django.db import models
from django.utils.translation import gettext_lazy as _


class Title(models.Model):
    name = models.CharField(
        _('Заголовок'),
        max_length=255,
    )
    description = models.TextField(
        _('Описания условии'),
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Заголовок')
        verbose_name_plural = _('Заголовки')


class Contact(models.Model):
    icon = models.ImageField(
        _('Иконка'),
        upload_to='contacts_icon/',
    )
    url = models.URLField(
        _('Ссылка'),
    )
    text = models.CharField(
        _('Текст'),
        max_length=255,
    )

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = _('Контакт')
        verbose_name_plural = _('Контакты')


class BankRequisites(models.Model):
    image = models.ImageField(
        _('Изображение'),
        upload_to='images/',
    )
    requisites = models.CharField(
        _('Реквизиты'),
        max_length=255,
    )

    def __str__(self):
        return self.requisites

    class Meta:
        verbose_name = _('Банковский реквизит')
        verbose_name_plural = _('Банковские реквизиты')
