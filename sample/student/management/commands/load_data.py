from django.core.management.base import BaseCommand, CommandError
import pandas
import json
from student.models import Book, Student, School

class Command(BaseCommand):
    help = " load Students data"

    def add_arguments(self, parser):
        parser.add_argument('param', type=str)

    def handle(self, *args, **options):
        try:
            print("Running load data script")
            param = options.get('param')
            books_data = (pandas.read_excel(param, sheet_name='Books')).to_json(orient='records')
            schools_data = (pandas.read_excel(param, sheet_name='Schools')).to_json(orient='records')
            students_data = (pandas.read_excel(param, sheet_name='Students')).to_json(orient='records')

            for i in json.loads(books_data):
                Book(**i).save()
            
            for i in json.loads(schools_data):
                School(**i).save()
                
            for i in json.loads(students_data):
                try:
                    i['books'] = Book.objects.get(title=i['books'])
                except:
                    i['books'] = None

                try:
                    i['school'] = School.objects.get(school=i['school'])
                except:
                    i['school'] = None
                Student(**i).save()
        except:
            raise CommandError("Something went wrong with running load data")