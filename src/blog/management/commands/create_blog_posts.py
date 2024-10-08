from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from blog.models import Article
from faker import Faker
import random

class Command(BaseCommand):
    help = 'Creates a specified number of realistic blog posts'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of blog posts to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        fake = Faker()

        # Get all users
        users = User.objects.all()

        if not users:
            self.stdout.write(self.style.WARNING('No users found. Creating a default user.'))
            User.objects.create_user(username='default_user', password='password123')
            users = User.objects.all()

        for _ in range(total):
            title = fake.sentence(nb_words=6, variable_nb_words=True)
            content = '\n\n'.join(fake.paragraphs(nb=random.randint(3, 7)))
            is_published = random.choice([True, False])
            author = random.choice(users)

            article = Article.objects.create(
                title=title,
                content=content,
                is_published=is_published,
                author=author
            )

            status = "Published" if is_published else "Draft"
            self.stdout.write(self.style.SUCCESS(f'Successfully created article "{title}" ({status})'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} blog posts'))