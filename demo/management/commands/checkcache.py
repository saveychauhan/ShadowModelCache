from django.core.management.base import BaseCommand
from demo.models import Demo
import csv


class Command(BaseCommand):

    def handle(self, *args, **options):
        a = Demo.objects.cget(id='6')

        print(a)
