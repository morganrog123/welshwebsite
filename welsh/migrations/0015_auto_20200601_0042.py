# Generated by Django 2.0 on 2020-05-31 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welsh', '0014_lessonstart_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessonphrase',
            name='topic',
            field=models.CharField(choices=[['Fi fy Hunan', 'Fi fy Hunan'], ['Gwyliau', 'Gwyliau'], ['Ysgol', 'Ysgol'], ['Tywydd', 'Tywydd'], ['Amser', 'Amser'], ['Bwyd', 'Bwyd'], ['Ffasiwn', 'Ffasiwn'], ['Teulu a Ffrindiau', 'Teulu a Ffrindiau'], ['Trefn Ddyddiol', 'Trefn Ddyddiol'], ['Anifeiliad Anwes', 'Anifeiliad Anwes'], ['Cartref', 'Cartref'], ['Ardal', 'Ardal'], ['Hamdden a Hobiau', 'Hamdden a Hobiau'], ['Chwaraeon', 'Chwaraeon'], ['Digwyddiadau Arbennig', 'Digwyddiadau Arbennig'], ['Amser Gorffenol', 'Amser Gorffenol'], ['Cerddioraeth', 'Cerddioraeth'], ['Cymru, Digwylliant ac Enwogion', 'Cymru, Digwylliant ac Enwogion'], ["Cadw'n Iach", "Cadw'n Iach"], ['Y Penwythnos', 'Y Penwythnos'], ['Amser Dyfodol', 'Amser Dyfodol'], ['Gwaith', 'Gwaith'], ['Problemau Pobl Ifanc', 'Problemau Pobl Ifanc'], ['Y Amgylchedd', 'Y Amgylchedd'], ['Cyfryngau', 'Cyfryngau'], ['Technoleg', 'Technoleg']], max_length=50),
        ),
        migrations.AlterField(
            model_name='test',
            name='test_name',
            field=models.CharField(choices=[['Fi fy Hunan', 'Fi fy Hunan'], ['Gwyliau', 'Gwyliau'], ['Ysgol', 'Ysgol'], ['Tywydd', 'Tywydd'], ['Amser', 'Amser'], ['Bwyd', 'Bwyd'], ['Ffasiwn', 'Ffasiwn'], ['Teulu a Ffrindiau', 'Teulu a Ffrindiau'], ['Trefn Ddyddiol', 'Trefn Ddyddiol'], ['Anifeiliad Anwes', 'Anifeiliad Anwes'], ['Cartref', 'Cartref'], ['Ardal', 'Ardal'], ['Hamdden a Hobiau', 'Hamdden a Hobiau'], ['Chwaraeon', 'Chwaraeon'], ['Digwyddiadau Arbennig', 'Digwyddiadau Arbennig'], ['Amser Gorffenol', 'Amser Gorffenol'], ['Cerddioraeth', 'Cerddioraeth'], ['Cymru, Digwylliant ac Enwogion', 'Cymru, Digwylliant ac Enwogion'], ["Cadw'n Iach", "Cadw'n Iach"], ['Y Penwythnos', 'Y Penwythnos'], ['Amser Dyfodol', 'Amser Dyfodol'], ['Gwaith', 'Gwaith'], ['Problemau Pobl Ifanc', 'Problemau Pobl Ifanc'], ['Y Amgylchedd', 'Y Amgylchedd'], ['Cyfryngau', 'Cyfryngau'], ['Technoleg', 'Technoleg']], max_length=50),
        ),
    ]
