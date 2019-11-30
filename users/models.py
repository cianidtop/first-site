from django.db import models
from django.contrib.auth.models import User


TYPE_CHOICES = (
    ('Актер', 'Актер'),
    ('Режиссер', 'Режиссер'),
    ('Оператор', 'Оператор'),
    ('Монтажер', 'Монтажер'),
)


EXP = (
    ('До года', 'До года'),
    ('От года до трёх лет','От года до трёх лет'),
    ('Больше трех лет', 'Больше трех лет'),

)

WATCH = (
    ('not_allowed', 'not_allowed'),
    ('allowed', 'allowed'),

)


# Апдейт профиля после регистрации
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='default.jpg', upload_to='user_images')
    name = models.CharField('Ваше имя:', default='', max_length=20)
    portfoils_site = models.URLField('Ссылка на портфолио/личную страницу', blank=True)
    about = models.CharField('Номер телефона', max_length=15)
    ready = models.BooleanField('Вы готовы работать за идею в некомерческом проекте?', default=True)
    job = models.CharField('Специализация', choices=TYPE_CHOICES, default='Актер', max_length=30)
    exp = models.CharField('Опыт', choices=EXP, default='До года', max_length=30)
    price = models.CharField('Цена', default='.../час работы', max_length=15)
    acess = models.CharField('Доступ', choices=WATCH, default='Не разрешать', max_length=30)


    def __str__(self):
        return f'Профиль пользователя{self.user.username}'