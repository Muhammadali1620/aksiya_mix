# Generated by Django 5.0.7 on 2024-09-12 11:59

import apps.companies.validators
import apps.users.validators
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_id', models.CharField(editable=False, unique=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='company/logo/%Y/%m/%d/', validators=[apps.companies.validators.validate_company_logo_size])),
                ('video', models.FileField(blank=True, null=True, upload_to='company/videos/%Y/%m/%d/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4']), apps.companies.validators.validate_company_video_size])),
                ('banner', models.ImageField(blank=True, null=True, upload_to='company/banner/%Y/%m/%d/', validators=[apps.companies.validators.validate_company_banner_size, apps.companies.validators.validate_image_size])),
                ('name', models.CharField(max_length=150)),
                ('username', models.SlugField(max_length=20, unique=True)),
                ('phone_number', models.CharField(max_length=13, validators=[apps.users.validators.phone_validate])),
                ('description', models.TextField(max_length=1000)),
                ('description_uz', models.TextField(max_length=1000, null=True)),
                ('description_ru', models.TextField(max_length=1000, null=True)),
                ('followers', models.CharField(default='0', max_length=40)),
                ('likes', models.CharField(default='0', max_length=40)),
                ('comments', models.CharField(default='0', max_length=50)),
                ('views', models.CharField(default='0', max_length=50)),
                ('installment', models.BooleanField(default=False)),
                ('web_site', models.URLField(blank=True, null=True)),
                ('slogan', models.CharField(blank=True, max_length=30, null=True)),
                ('slogan_uz', models.CharField(blank=True, max_length=30, null=True)),
                ('slogan_ru', models.CharField(blank=True, max_length=30, null=True)),
                ('region', models.PositiveSmallIntegerField(choices=[(1, 'Sirdaryo'), (2, 'Navoiy'), (3, 'Jizzax'), (4, 'Xorazm'), (5, 'Buxoro'), (6, 'Surxondaryo'), (7, 'Namangan'), (8, 'Andijon'), (9, 'Qashqadaryo'), (10, 'Samarqand'), (11, 'Fargʻona'), (12, 'Toshkent'), (13, 'Qoraqalpog‘iston')])),
                ('district', models.PositiveSmallIntegerField(choices=[('1X1', 'BOYOVUT'), ('1X2', 'GULISTON_SHAXRI'), ('1X3', 'GULISTON'), ('1X4', 'OQOLTIN'), ('1X5', 'SARDOBA'), ('1X6', 'SAYXUNOBOD'), ('1X7', 'SHIRIN'), ('1X8', 'SIRDARYO'), ('1X9', 'XOVOS'), ('1X10', 'YANGIYER'), ('2X1', 'KARMANA'), ('2X2', 'KONIMEX'), ('2X3', 'NAVBAHOR'), ('2X4', 'NAVOIY'), ('2X5', 'NUROTA'), ('2X6', 'QIZILTEPA'), ('2X7', 'TOMDI'), ('2X8', 'UCHQUDUQ'), ('2X9', 'XATIRCHI'), ('2X10', 'ZARAFSHON'), ('3X1', 'ARNASOY'), ('3X2', 'BAXMAL'), ('3X3', 'DOSTLIK'), ('3X4', 'FORISH'), ('3X5', 'GALLAOROL'), ('3X6', 'JIZZAX'), ('3X7', 'JIZZAX_SHAXRI'), ('3X8', 'MIRZACHOL'), ('3X9', 'PAXTAKOR'), ('3X10', 'YANGIOBOD'), ('3X11', 'ZAFAROBOD'), ('3X12', 'ZARBAND'), ('3X13', 'ZOMIN'), ('4X1', 'BOGOT'), ('4X2', 'GURLAN'), ('4X3', 'QOSHKOPIR'), ('4X4', 'SHOVOT'), ('4X5', 'URGANCH_SHAHRI'), ('4X6', 'URGANCH'), ('4X7', 'XAZORASP'), ('4X8', 'XIVA'), ('4X9', 'XONQA'), ('4X10', 'YANGIARIQ'), ('4X11', 'YANGIBOZOR'), ('5X1', 'BUXORO_SHAHRI'), ('5X2', 'BUXORO'), ('5X3', 'GIJDUVON'), ('5X4', 'JONDOR'), ('5X5', 'KOGON_SHAHRI'), ('5X6', 'KOGON'), ('5X7', 'OLOT'), ('5X8', 'PESHKU'), ('5X9', 'QORAKOL'), ('5X10', 'QOROVULBOZOR'), ('5X11', 'ROMITAN'), ('5X12', 'SHOFIRKON'), ('5X13', 'VOBKENT'), ('6X1', 'ANGOR'), ('6X2', 'BANDIXON'), ('6X3', 'BOYSUN'), ('6X4', 'DENOV'), ('6X5', 'JARQORGON'), ('6X6', 'MUZROBOT'), ('6X7', 'OLTINSOY'), ('6X8', 'QIZIRIQ'), ('6X9', 'QUMQORGON'), ('6X10', 'SARIOSIYO'), ('6X11', 'SHEROBOD'), ('6X12', 'SHORCHI'), ('6X13', 'TERMIZ_SHAHRI'), ('6X14', 'TERMIZ'), ('6X15', 'UZUN'), ('7X1', 'CHORTOQ'), ('7X2', 'CHUST'), ('7X3', 'KOSONSOY'), ('7X4', 'MINGBULOQ'), ('7X5', 'NAMANGAN_SHAHRI'), ('7X6', 'NAMANGAN'), ('7X7', 'NORIN'), ('7X8', 'POP'), ('7X9', 'TORAQORGON'), ('7X10', 'UCHQORGON'), ('7X11', 'UYCHI'), ('7X12', 'YANGIQORGON'), ('8X1', 'ANDIJON_SHAHRI'), ('8X2', 'ANDIJON'), ('8X3', 'ASAKA'), ('8X4', 'BALIQCHI'), ('8X5', 'BOZ'), ('8X6', 'BULOQBOSHI'), ('8X7', 'IZBOSKAN'), ('8X8', 'JALOLQUDUQ'), ('8X9', 'MARHAMAT'), ('8X10', 'OLTINKOL'), ('8X11', 'PAXTAOBOD'), ('8X12', 'QORGONTEPA'), ('8X13', 'SHAHRIXON'), ('8X14', 'ULUGNOR'), ('8X15', 'XOJAOBOD'), ('8X16', 'XONOBOD_SHAHRI'), ('9X1', 'CHIROQCHI'), ('9X2', 'DEHQONOBOD'), ('9X3', 'GUZOR'), ('9X4', 'KASBI'), ('9X5', 'KITOB'), ('9X6', 'KOSON'), ('9X7', 'MIRISHKOR'), ('9X8', 'MUBORAK'), ('9X9', 'NISHON'), ('9X10', 'QAMASHI'), ('9X11', 'QARSHI_SHAHRI'), ('9X12', 'QARSHI'), ('9X13', 'SHAHRISABZ_SHAHRI'), ('9X14', 'YAKKABOG'), ('10X1', 'BULUNGUR'), ('10X2', 'ISHTIXON'), ('10X3', 'JOMBOY'), ('10X4', 'KATTAQORGON_SHAXRI'), ('10X5', 'KATTAQORGON'), ('10X6', 'NARPAY'), ('10X7', 'NUROBOD'), ('10X8', 'OQDARYO'), ('10X9', 'PAST_DARGOM'), ('10X10', 'PAXTACHI'), ('10X11', 'POYARIQ'), ('10X12', 'QOSHRABOT'), ('10X13', 'SAMARQAND'), ('10X14', 'SAMARQAND'), ('10X15', 'TOYLOQ'), ('10X16', 'URGUT'), ('11X1', 'BESHARIQ'), ('11X2', 'BOGDOD'), ('11X3', 'BUVAYDA'), ('11X4', 'DANGARA'), ('11X5', 'FARGONA_SHAHRI'), ('11X6', 'FARGONA'), ('11X7', 'FURQAT'), ('11X8', 'MARGILON_SHAHRI'), ('11X9', 'OZBEKISTON'), ('11X10', 'OLTIARIQ'), ('11X11', 'QOQON_SHAHRI'), ('11X12', 'QOSHTEPA'), ('11X13', 'QUVA'), ('11X14', 'QUVASOY_SHAHRI'), ('11X15', 'RISHTON'), ('11X16', 'SOX'), ('11X17', 'TOSHLOQ'), ('11X18', 'UCHKOPRIK'), ('11X19', 'YOZYOVON'), ('12X1', 'BEKTEMIR'), ('12X2', 'MIROBOD'), ('12X3', 'MIRZO_ULUG‘BEK'), ('12X4', 'SERGELI'), ('12X5', 'OLMAZOR'), ('12X6', 'UCHTEPA'), ('12X7', 'SHAYXONTOHUR'), ('12X8', 'YASHNOBOD'), ('12X9', 'CHILONZOR'), ('12X10', 'YUNUSOBOD'), ('12X11', 'YAKKASAROY'), ('13X1', 'AMUDARYO'), ('13X2', 'BERUNIY'), ('13X3', 'CHIMBOY'), ('13X4', 'ELLIKQALA'), ('13X5', 'KEGEYLI'), ('13X6', 'MOYNOQ'), ('13X7', 'NUKUS_SHAHRI'), ('13X8', 'NUKUS'), ('13X9', 'QONLIKOL'), ('13X10', 'QORAUZAQ'), ('13X11', 'QUNGIROT'), ('13X12', 'SHUMANAY'), ('13X13', 'TAXIATOSH_SHAHRI'), ('13X14', 'TAXTAKOPIR'), ('13X15', 'TORTKOL'), ('13X16', 'XOJAYLI')])),
                ('address', models.CharField(max_length=255)),
                ('address_uz', models.CharField(max_length=255, null=True)),
                ('address_ru', models.CharField(max_length=255, null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('balance', models.DecimalField(decimal_places=1, default=0, max_digits=30, validators=[django.core.validators.MinValueValidator(0)])),
                ('rating1', models.CharField(default='0', max_length=50)),
                ('rating2', models.CharField(default='0', max_length=50)),
                ('rating3', models.CharField(default='0', max_length=50)),
                ('rating4', models.CharField(default='0', max_length=50)),
                ('rating5', models.CharField(default='0', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('categories', models.ManyToManyField(blank=True, to='categories.category')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Filial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=13, validators=[apps.users.validators.phone_validate])),
                ('delivery', models.BooleanField(default=False)),
                ('region', models.PositiveSmallIntegerField(choices=[(1, 'Sirdaryo'), (2, 'Navoiy'), (3, 'Jizzax'), (4, 'Xorazm'), (5, 'Buxoro'), (6, 'Surxondaryo'), (7, 'Namangan'), (8, 'Andijon'), (9, 'Qashqadaryo'), (10, 'Samarqand'), (11, 'Fargʻona'), (12, 'Toshkent'), (13, 'Qoraqalpog‘iston')])),
                ('district', models.PositiveSmallIntegerField(choices=[('1X1', 'BOYOVUT'), ('1X2', 'GULISTON_SHAXRI'), ('1X3', 'GULISTON'), ('1X4', 'OQOLTIN'), ('1X5', 'SARDOBA'), ('1X6', 'SAYXUNOBOD'), ('1X7', 'SHIRIN'), ('1X8', 'SIRDARYO'), ('1X9', 'XOVOS'), ('1X10', 'YANGIYER'), ('2X1', 'KARMANA'), ('2X2', 'KONIMEX'), ('2X3', 'NAVBAHOR'), ('2X4', 'NAVOIY'), ('2X5', 'NUROTA'), ('2X6', 'QIZILTEPA'), ('2X7', 'TOMDI'), ('2X8', 'UCHQUDUQ'), ('2X9', 'XATIRCHI'), ('2X10', 'ZARAFSHON'), ('3X1', 'ARNASOY'), ('3X2', 'BAXMAL'), ('3X3', 'DOSTLIK'), ('3X4', 'FORISH'), ('3X5', 'GALLAOROL'), ('3X6', 'JIZZAX'), ('3X7', 'JIZZAX_SHAXRI'), ('3X8', 'MIRZACHOL'), ('3X9', 'PAXTAKOR'), ('3X10', 'YANGIOBOD'), ('3X11', 'ZAFAROBOD'), ('3X12', 'ZARBAND'), ('3X13', 'ZOMIN'), ('4X1', 'BOGOT'), ('4X2', 'GURLAN'), ('4X3', 'QOSHKOPIR'), ('4X4', 'SHOVOT'), ('4X5', 'URGANCH_SHAHRI'), ('4X6', 'URGANCH'), ('4X7', 'XAZORASP'), ('4X8', 'XIVA'), ('4X9', 'XONQA'), ('4X10', 'YANGIARIQ'), ('4X11', 'YANGIBOZOR'), ('5X1', 'BUXORO_SHAHRI'), ('5X2', 'BUXORO'), ('5X3', 'GIJDUVON'), ('5X4', 'JONDOR'), ('5X5', 'KOGON_SHAHRI'), ('5X6', 'KOGON'), ('5X7', 'OLOT'), ('5X8', 'PESHKU'), ('5X9', 'QORAKOL'), ('5X10', 'QOROVULBOZOR'), ('5X11', 'ROMITAN'), ('5X12', 'SHOFIRKON'), ('5X13', 'VOBKENT'), ('6X1', 'ANGOR'), ('6X2', 'BANDIXON'), ('6X3', 'BOYSUN'), ('6X4', 'DENOV'), ('6X5', 'JARQORGON'), ('6X6', 'MUZROBOT'), ('6X7', 'OLTINSOY'), ('6X8', 'QIZIRIQ'), ('6X9', 'QUMQORGON'), ('6X10', 'SARIOSIYO'), ('6X11', 'SHEROBOD'), ('6X12', 'SHORCHI'), ('6X13', 'TERMIZ_SHAHRI'), ('6X14', 'TERMIZ'), ('6X15', 'UZUN'), ('7X1', 'CHORTOQ'), ('7X2', 'CHUST'), ('7X3', 'KOSONSOY'), ('7X4', 'MINGBULOQ'), ('7X5', 'NAMANGAN_SHAHRI'), ('7X6', 'NAMANGAN'), ('7X7', 'NORIN'), ('7X8', 'POP'), ('7X9', 'TORAQORGON'), ('7X10', 'UCHQORGON'), ('7X11', 'UYCHI'), ('7X12', 'YANGIQORGON'), ('8X1', 'ANDIJON_SHAHRI'), ('8X2', 'ANDIJON'), ('8X3', 'ASAKA'), ('8X4', 'BALIQCHI'), ('8X5', 'BOZ'), ('8X6', 'BULOQBOSHI'), ('8X7', 'IZBOSKAN'), ('8X8', 'JALOLQUDUQ'), ('8X9', 'MARHAMAT'), ('8X10', 'OLTINKOL'), ('8X11', 'PAXTAOBOD'), ('8X12', 'QORGONTEPA'), ('8X13', 'SHAHRIXON'), ('8X14', 'ULUGNOR'), ('8X15', 'XOJAOBOD'), ('8X16', 'XONOBOD_SHAHRI'), ('9X1', 'CHIROQCHI'), ('9X2', 'DEHQONOBOD'), ('9X3', 'GUZOR'), ('9X4', 'KASBI'), ('9X5', 'KITOB'), ('9X6', 'KOSON'), ('9X7', 'MIRISHKOR'), ('9X8', 'MUBORAK'), ('9X9', 'NISHON'), ('9X10', 'QAMASHI'), ('9X11', 'QARSHI_SHAHRI'), ('9X12', 'QARSHI'), ('9X13', 'SHAHRISABZ_SHAHRI'), ('9X14', 'YAKKABOG'), ('10X1', 'BULUNGUR'), ('10X2', 'ISHTIXON'), ('10X3', 'JOMBOY'), ('10X4', 'KATTAQORGON_SHAXRI'), ('10X5', 'KATTAQORGON'), ('10X6', 'NARPAY'), ('10X7', 'NUROBOD'), ('10X8', 'OQDARYO'), ('10X9', 'PAST_DARGOM'), ('10X10', 'PAXTACHI'), ('10X11', 'POYARIQ'), ('10X12', 'QOSHRABOT'), ('10X13', 'SAMARQAND'), ('10X14', 'SAMARQAND'), ('10X15', 'TOYLOQ'), ('10X16', 'URGUT'), ('11X1', 'BESHARIQ'), ('11X2', 'BOGDOD'), ('11X3', 'BUVAYDA'), ('11X4', 'DANGARA'), ('11X5', 'FARGONA_SHAHRI'), ('11X6', 'FARGONA'), ('11X7', 'FURQAT'), ('11X8', 'MARGILON_SHAHRI'), ('11X9', 'OZBEKISTON'), ('11X10', 'OLTIARIQ'), ('11X11', 'QOQON_SHAHRI'), ('11X12', 'QOSHTEPA'), ('11X13', 'QUVA'), ('11X14', 'QUVASOY_SHAHRI'), ('11X15', 'RISHTON'), ('11X16', 'SOX'), ('11X17', 'TOSHLOQ'), ('11X18', 'UCHKOPRIK'), ('11X19', 'YOZYOVON'), ('12X1', 'BEKTEMIR'), ('12X2', 'MIROBOD'), ('12X3', 'MIRZO_ULUG‘BEK'), ('12X4', 'SERGELI'), ('12X5', 'OLMAZOR'), ('12X6', 'UCHTEPA'), ('12X7', 'SHAYXONTOHUR'), ('12X8', 'YASHNOBOD'), ('12X9', 'CHILONZOR'), ('12X10', 'YUNUSOBOD'), ('12X11', 'YAKKASAROY'), ('13X1', 'AMUDARYO'), ('13X2', 'BERUNIY'), ('13X3', 'CHIMBOY'), ('13X4', 'ELLIKQALA'), ('13X5', 'KEGEYLI'), ('13X6', 'MOYNOQ'), ('13X7', 'NUKUS_SHAHRI'), ('13X8', 'NUKUS'), ('13X9', 'QONLIKOL'), ('13X10', 'QORAUZAQ'), ('13X11', 'QUNGIROT'), ('13X12', 'SHUMANAY'), ('13X13', 'TAXIATOSH_SHAHRI'), ('13X14', 'TAXTAKOPIR'), ('13X15', 'TORTKOL'), ('13X16', 'XOJAYLI')])),
                ('address', models.CharField(max_length=255)),
                ('address_uz', models.CharField(max_length=255, null=True)),
                ('address_ru', models.CharField(max_length=255, null=True)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyTimeTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.PositiveSmallIntegerField(choices=[(0, 'SUNDAY'), (1, 'MONDAY'), (2, 'TUESDAY'), (3, 'WEDNESDAY'), (4, 'THURSDAY'), (5, 'FRIDAY'), (6, 'SATURDAY')])),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.company')),
                ('filial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companies.filial')),
            ],
            options={
                'unique_together': {('company', 'week_day'), ('filial', 'week_day')},
            },
        ),
    ]
