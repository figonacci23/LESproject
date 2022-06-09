from django.db import models
from django.utils import timezone
from djmoney.models.fields import MoneyField
from main.models import Administrator


# Create your models here.

class Park(models.Model):
    STRUCTURE = 'ST'
    SURFACE = 'SF'
    TYPOLOGYS = [
        (STRUCTURE, 'Structure'),
        (SURFACE, 'Surface'),
    ]

    LISBON1 = '11'
    LISBON2 = '12'
    LISBON3 = '13'
    LISBON4 = '14'
    LISBON5 = '15'
    LISBON6 = '16'
    LISBON7 = '17'
    LISBON8 = '18'
    LISBON9 = '19'
    FARO = '80'
    ALBUFEIRA = '82'
    CITY = [
        (LISBON1, 'Lisbon'),
        (LISBON2, 'Lisbon'),
        (LISBON3, 'Lisbon'),
        (LISBON4, 'Lisbon'),
        (LISBON5, 'Lisbon'),
        (LISBON6, 'Lisbon'),
        (LISBON8, 'Lisbon'),
        (LISBON9, 'Lisbon'),
        (FARO, 'Faro'),
        (ALBUFEIRA, 'Albufeira'),
    ]

    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', verbose_name='Name', max_length=50, unique=True)
    address = models.CharField(db_column='Address', verbose_name='Address', max_length=50, unique=True)
    postal_code = models.CharField(db_column='PostalCode', verbose_name='Postal Code', max_length=8, unique=True)
    typology = models.CharField(verbose_name='Typology', db_column='Typology', choices=TYPOLOGYS, max_length=2)
    map_html = models.TextField(db_column='MapLocationHTML', verbose_name='Map Location HTML')
    monday_start = models.TimeField(db_column='MondayStart', verbose_name='Monday Start', null=True)
    monday_end = models.TimeField(db_column='MondayEnd', verbose_name='Monday End', null=True)
    tuesday_start = models.TimeField(db_column='TuesdayStart', verbose_name='Tuesday Start', null=True)
    tuesday_end = models.TimeField(db_column='TuesdayEnd', verbose_name='Tuesday End', null=True)
    wednesday_start = models.TimeField(db_column='WednesdayStart', verbose_name='Wednesday Start', null=True)
    wednesday_end = models.TimeField(db_column='WednesdayEnd', verbose_name='Wednesday End', null=True)
    thursday_start = models.TimeField(db_column='ThursdayStart', verbose_name='Thursday Start', null=True)
    thursday_end = models.TimeField(db_column='ThursdayEnd', verbose_name='Thursday End', null=True)
    friday_start = models.TimeField(db_column='FridayStart', verbose_name='Friday Start', null=True)
    friday_end = models.TimeField(db_column='FridayEnd', verbose_name='Friday End', null=True)
    saturday_start = models.TimeField(db_column='SaturdayStart', verbose_name='Saturday Start', null=True)
    saturday_end = models.TimeField(db_column='SaturdayEnd', verbose_name='Saturday End', null=True)
    sunday_start = models.TimeField(db_column='SundayStart', verbose_name='Sunday Start', null=True)
    sunday_end = models.TimeField(db_column='SundayEnd', verbose_name='Sunday End', null=True)
    is_open = models.BooleanField(verbose_name='IsOpen', db_column='IsOpen', default=False)
    created = models.DateTimeField(db_column='Created', verbose_name='Created', default=timezone.now)
    updated = models.DateTimeField(db_column='Updated', verbose_name='Updated', default=timezone.now)
    admin = models.ForeignKey(Administrator, models.CASCADE, verbose_name='Admin', db_column='Admin',
                              null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/parks/%i/" % self.id

    def map_src(self):
        return self.map_html.split('"')[1]

    def city(self):
        for x in Park.CITY:
            if x[0] == self.postal_code[:2]:
                return x[1]
        return ''

    def posta_city(self):
        return self.postal_code + " " + self.city()

    def spots(self):
        i = 0
        for zone in self.zones():
            i += zone.spots().count()
        return i

    def zones(self):
        return Zone.objects.filter(park=self.id)

    def price_types(self):
        return PriceType.objects.filter(park=self.id)

    def contract_types(self):
        return ContractType.objects.filter(park=self.id)


class PriceType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    minutes = models.IntegerField(db_column='MinutesTime', verbose_name='Minutes Time', default=0)
    hours = models.IntegerField(db_column='HoursTime', verbose_name='Hours Time', default=0)
    total = models.DecimalField(db_column='TotalValue', verbose_name='Total Value', max_digits=6, decimal_places=2,
                                default=0)
    park = models.ForeignKey(Park, models.CASCADE, db_column='Parque', verbose_name='Park')

    class Meta:
        unique_together = ('minutes', 'hours', 'park')

    def total_time(self):
        if self.minutes and self.hours:
            return str(self.hours) + "h:" + str(self.minutes) + "m"
        elif self.hours:
            return str(self.hours) + "h"
        else:
            return str(self.minutes) + "m"


class ContractType(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', verbose_name='Name', max_length=50, unique=True)
    years = models.IntegerField(db_column='YearsTime', verbose_name='Years Time', default=0)
    months = models.IntegerField(db_column='MonthsTime', verbose_name='Months Time', default=0)
    total = models.DecimalField(db_column='TotalValue', verbose_name='Total Value', max_digits=6, decimal_places=2,
                                default=0)
    park = models.ForeignKey(Park, models.CASCADE, db_column='Parque', verbose_name='Park')

    class Meta:
        unique_together = ('name', 'park')


class LayoutLine(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    x = models.IntegerField(db_column="Abscissa", verbose_name="Abscissa")
    y = models.IntegerField(db_column="Ordiante", verbose_name="Ordiante")
    w = models.IntegerField(db_column="Width", verbose_name="Width")
    h = models.IntegerField(db_column="Height", verbose_name="Height")


class Zone(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)
    name = models.CharField(db_column='Name', verbose_name='Name', max_length=50, unique=True)
    park = models.ForeignKey(Park, models.CASCADE, db_column='Parque', verbose_name='Park')

    def spots(self):
        return ParkingSpot.objects.filter(zone=self.id)

    def n_spots(self):
        return self.spots().count()

    def available_spots(self):
        return ParkingSpot.objects.filter(zone=self.id, state='AV')

    def n_available_spots(self):
        return self.spots().count()

    def get_absolute_url(self):
        return "/parks/%i/zones/%i/" % (self.park.id, self.id)


class ParkingSpot(models.Model):
    AVAILABLE = 'AV'
    OCCUPIED = 'OC'
    RESERVED = 'RE'
    STATES = [
        (AVAILABLE, 'Available'),
        (OCCUPIED, 'Occupied'),
        (RESERVED, 'Reserved'),
    ]
    VERTICAL = 'VE'
    HORIZONTAL = 'HO'
    DIRECTIONS = [
        (VERTICAL, 'Vertical'),
        (HORIZONTAL, 'Horizontal'),
    ]
    id = models.AutoField(db_column='ID', primary_key=True)
    number = models.IntegerField(db_column='Number', verbose_name='Number')
    zone = models.ForeignKey(Zone, models.CASCADE, db_column='Zone', verbose_name='Zone')
    state = models.CharField(verbose_name='State', db_column='State', choices=STATES, max_length=2, default=AVAILABLE)
    x = models.IntegerField(db_column="Abscissa", verbose_name="Abscissa")
    y = models.IntegerField(db_column="Ordiante", verbose_name="Ordiante")
    direction = models.CharField(verbose_name='Direction', db_column='Direction', choices=DIRECTIONS, max_length=2)
