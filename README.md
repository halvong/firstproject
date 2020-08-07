July 30, 2020, Thurs

docker-compose exec web python manage.py makemigrations toys
docker-compose exec web python manage.py migrate 
docker-compose logs -f web 
docker-compose exec web python manage.py createsuperuser
