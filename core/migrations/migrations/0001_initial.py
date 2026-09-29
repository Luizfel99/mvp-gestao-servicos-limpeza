from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Cliente",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=150)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("telefone", models.CharField(blank=True, max_length=30)),
                ("ativo", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Profissional",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=150)),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("telefone", models.CharField(blank=True, max_length=30)),
                ("ativo", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Propriedade",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=150)),
                ("endereco", models.CharField(max_length=255)),
                ("cidade", models.CharField(max_length=100)),
                ("observacoes", models.TextField(blank=True)),
                (
                    "cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="propriedades",
                        to="core.cliente",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Servico",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("data", models.DateField()),
                ("horario", models.TimeField()),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("agendado", "Agendado"),
                            ("em_andamento", "Em andamento"),
                            ("concluido", "Concluído"),
                            ("cancelado", "Cancelado"),
                        ],
                        default="agendado",
                        max_length=20,
                    ),
                ),
                ("observacoes", models.TextField(blank=True)),
                (
                    "profissional",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="servicos",
                        to="core.profissional",
                    ),
                ),
                (
                    "propriedade",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="servicos",
                        to="core.propriedade",
                    ),
                ),
            ],
        ),
    ]
