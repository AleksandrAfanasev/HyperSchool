alex_cars_number = Car.objects.filter(drivers__name='Alex').count()