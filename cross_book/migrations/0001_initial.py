# Generated by Django 3.1.3 on 2021-06-28 16:43

import cross_book.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('image', models.ImageField(default='/profile_pics/default.png', upload_to='profile_pics')),
                ('profile_text', models.TextField(blank=True, max_length=250, verbose_name='プロフィール文')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last_name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designate whether this user should be treated as active.Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', cross_book.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='商品名')),
                ('explanation', models.TextField(blank=True, max_length=3000, verbose_name='出品者からの一言')),
                ('state', models.IntegerField(choices=[(0, '選択してください'), (1, '未使用'), (2, '未使用に近い状態'), (3, '目立った傷や汚れなし'), (4, 'やや傷や汚れあり'), (5, '傷や汚れあり'), (6, '全体的に状態が悪い')], default=0, validators=[cross_book.models.Item.validate_choice], verbose_name='商品の状態')),
                ('category', models.CharField(default='選択してください', max_length=255, validators=[cross_book.models.Item.validate_category], verbose_name='カテゴリ')),
                ('shipping_area', models.IntegerField(choices=[(0, '選択してください'), (1, '北海道'), (2, '青森県'), (3, '岩手県'), (4, '宮城県'), (5, '秋田県'), (6, '山形県'), (7, '福島県'), (8, '茨城県'), (9, '栃木県'), (10, '群馬県'), (11, '埼玉県'), (12, '千葉県'), (13, '東京都'), (14, '神奈川県'), (15, '新潟県'), (16, '富山県'), (17, '石川県'), (18, '福井県'), (19, '山梨県'), (20, '長野県'), (21, '岐阜県'), (22, '静岡県'), (23, '愛知県'), (24, '三重県'), (25, '滋賀県'), (26, '京都府'), (27, '大阪府'), (28, '兵庫県'), (29, '奈良県'), (30, '和歌山県'), (31, '鳥取県'), (32, '島根県'), (33, '岡山県'), (34, '広島県'), (35, '山口県'), (36, '徳島県'), (37, '香川県'), (38, '愛媛県'), (39, '高知県'), (40, '福岡県'), (41, '佐賀県'), (42, '長崎県'), (43, '熊本県'), (44, '大分県'), (45, '宮崎県'), (46, '鹿児島県'), (47, '沖縄県'), (48, '未定')], default=0, validators=[cross_book.models.Item.validate_choice], verbose_name='発送元の地域')),
                ('shipping_day', models.IntegerField(choices=[(0, '選択してください'), (1, '1~2日で発送'), (2, '2~3日で発送'), (3, '4~7日で発送')], default=0, validators=[cross_book.models.Item.validate_choice], verbose_name='発送までの日数')),
                ('at_created', models.DateTimeField(auto_now_add=True, verbose_name='出品日')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Trade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trading_start_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TradeRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cross_book.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TradeMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cross_book.trade')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TradeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cross_book.trade')),
                ('traded_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cross_book.item')),
                ('trader', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoomMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cross_book.room')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('comment', 'comment'), ('like', 'like'), ('transaction_request', 'transaction_request')], max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('target_object_id', models.PositiveIntegerField()),
                ('new_message', models.BooleanField(default=True)),
                ('unread', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('actor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_actor', to=settings.AUTH_USER_MODEL)),
                ('recipient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_recipient', to=settings.AUTH_USER_MODEL)),
                ('target_content_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notify_target', to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room_messages', to='cross_book.room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cross_book.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=cross_book.models.get_image_filename, verbose_name='')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cross_book.item')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length='1000', verbose_name='コメント')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cross_book.item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zip_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='郵便番号')),
                ('address1', models.IntegerField(blank=True, choices=[(0, '選択してください'), (1, '北海道'), (2, '青森県'), (3, '岩手県'), (4, '宮城県'), (5, '秋田県'), (6, '山形県'), (7, '福島県'), (8, '茨城県'), (9, '栃木県'), (10, '群馬県'), (11, '埼玉県'), (12, '千葉県'), (13, '東京都'), (14, '神奈川県'), (15, '新潟県'), (16, '富山県'), (17, '石川県'), (18, '福井県'), (19, '山梨県'), (20, '長野県'), (21, '岐阜県'), (22, '静岡県'), (23, '愛知県'), (24, '三重県'), (25, '滋賀県'), (26, '京都府'), (27, '大阪府'), (28, '兵庫県'), (29, '奈良県'), (30, '和歌山県'), (31, '鳥取県'), (32, '島根県'), (33, '岡山県'), (34, '広島県'), (35, '山口県'), (36, '徳島県'), (37, '香川県'), (38, '愛媛県'), (39, '高知県'), (40, '福岡県'), (41, '佐賀県'), (42, '長崎県'), (43, '熊本県'), (44, '大分県'), (45, '宮崎県'), (46, '鹿児島県'), (47, '沖縄県'), (48, '未定')], null=True, verbose_name='都道府県')),
                ('address2', models.CharField(blank=True, max_length=40, null=True, verbose_name='市区町村番地')),
                ('address3', models.CharField(blank=True, max_length=40, null=True, verbose_name='建物名')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
