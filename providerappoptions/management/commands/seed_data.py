from django.core.management.base import BaseCommand
from providerappoptions.models import MainApp, AppSubType, AppHosting, ListingStatus, ListingAppStatus, ListingStateStatus


class Command(BaseCommand):
    help = 'Seed database with initial data'

    def handle(self, *args, **kwargs):
        # Create MainApp instances
        main_app1 = MainApp.objects.create(name='Games', value='games')
        main_app2 = MainApp.objects.create(name='Vending Machines', value='vending_machines')

        # Create AppSubType instances
        AppSubType.objects.create(name='Online Casino', value='online_casino', main_app=main_app1)
        AppSubType.objects.create(name='Onsite Casino', value='onsite_casino', main_app=main_app1)

        # Create AppHosting instances
        AppHosting.objects.create(name='Self-hosted', value='self_hosted', subtype=AppSubType.objects.first())
        AppHosting.objects.create(name='Platform Hosted', value='platform_hosted', subtype=AppSubType.objects.first())

        # Create ListingStatus instances
        ListingStatus.objects.create(name='Active', value='is_active')
        ListingStatus.objects.create(name='Inactive', value='is_inactive')

        # Create ListingAppStatus instances
        ListingAppStatus.objects.create(name='Active', value='is_active')
        ListingAppStatus.objects.create(name='Inactive', value='is_inactive')

        # Create ListingStateStatus instances
        ListingStateStatus.objects.create(name='Pending', value='pending')
        ListingStateStatus.objects.create(name='In Progress', value='in_progress')

        self.stdout.write(self.style.SUCCESS('Successfully seeded the database'))