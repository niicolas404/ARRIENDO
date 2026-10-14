from django.contrib import admin
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Arriendo, Equipo


class AdminCreateTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.equipo = Equipo.objects.create(
            nombre="Taladro",
            descripcion="Taladro inalámbrico",
            stock=3,
            url_imagen="https://example.com/taladro.jpg",
        )

    def setUp(self):
        user = get_user_model().objects.create_superuser(
            username="admin",
            email="admin@example.com",
            password="test-password",
        )
        self.client.force_login(user)

    def test_models_use_custom_admin_configuration(self):
        self.assertEqual(
            admin.site._registry[Equipo].list_display,
            ["nombre", "descripcion", "stock", "url_imagen"],
        )
        self.assertEqual(
            admin.site._registry[Arriendo].list_display,
            ["equipo", "fecha_inicio", "fecha_fin", "cliente", "precio_formateado"],
        )

    def test_add_equipo_from_admin(self):
        response = self.client.post(
            reverse("admin:shop_equipo_add"),
            {
                "nombre": "Sierra",
                "descripcion": "Sierra circular",
                "stock": 2,
                "url_imagen": "https://example.com/sierra.jpg",
                "_save": "Guardar",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Equipo.objects.filter(nombre="Sierra").exists())

    def test_add_arriendo_from_admin(self):
        response = self.client.post(
            reverse("admin:shop_arriendo_add"),
            {
                "equipo": self.equipo.pk,
                "fecha_inicio": "2026-10-15",
                "fecha_fin": "2026-10-17",
                "cliente": "Ana Pérez",
                "precio": 25000,
                "_save": "Guardar",
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertTrue(Arriendo.objects.filter(cliente="Ana Pérez").exists())
