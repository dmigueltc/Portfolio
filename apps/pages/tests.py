import re

from django.conf import settings
from django.test import TestCase
from django.urls import reverse


class HomePageTests(TestCase):
    def test_home_page_responds(self):
        response = self.client.get(reverse("pages:home"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/home.html")

    def test_home_page_shows_identity_and_positioning(self):
        response = self.client.get(reverse("pages:home"))

        self.assertContains(response, "Miguel Cardoso")
        self.assertContains(
            response,
            "Sou estudante de Engenharia Inform\xe1tica, interessado em "
            "desenvolvimento, tecnologia e cria\xe7\xe3o de conte\xfado.",
        )

    def test_home_page_lists_main_areas(self):
        response = self.client.get(reverse("pages:home"))

        for area in ("Tecnologia", "Fotografia", "Fitness"):
            self.assertContains(response, area)

    def test_home_page_has_explore_cta(self):
        response = self.client.get(reverse("pages:home"))

        # O CTA agora tem destino real: a secção Explora nesta mesma
        # página (deixou de ser um elemento inerte sem href).
        self.assertContains(response, "Explore")
        self.assertContains(response, '<a class="button button--primary" href="#explora">')

    def test_home_page_includes_header_and_footer(self):
        response = self.client.get(reverse("pages:home"))

        self.assertContains(response, "site-header")
        self.assertContains(response, "site-footer")

    def test_home_page_uses_design_tokens(self):
        response = self.client.get(reverse("pages:home"))

        self.assertContains(response, "/static/css/tokens.css")
        self.assertContains(response, "/static/css/layout.css")

    def test_navigation_home_link_is_functional(self):
        response = self.client.get(reverse("pages:home"))

        self.assertContains(response, 'href="/"')

    def test_navigation_pending_areas_are_not_links(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # Sobre/Tecnologia/Fotografia/Fitness/Projetos/Contacto ainda não
        # têm página de destino nesta fase — devem aparecer como
        # <span class="site-nav__item--pending">, nunca como <a href="...">.
        pending_areas = (
            "Sobre",
            "Tecnologia",
            "Fotografia",
            "Fitness",
            "Projetos",
            "Contacto",
        )
        for area in pending_areas:
            self.assertIn(
                f'<span class="site-nav__item--pending">{area}</span>',
                content,
                f"'{area}' devia estar marcado como pendente, não como link.",
            )

        # Confirma também que não existe nenhuma tag <a> a envolver
        # qualquer um destes nomes de área.
        for area in pending_areas:
            pattern = re.compile(rf"<a[^>]*>\s*{re.escape(area)}\s*</a>")
            self.assertNotRegex(content, pattern)


class ExploraSectionTests(TestCase):
    def test_explora_section_exists(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        self.assertContains(response, 'id="explora"')
        self.assertContains(response, "Explora")
        # Título da secção é um h2 — mantém a hierarquia correta a
        # seguir ao h1 da Hero (Miguel Cardoso).
        self.assertRegex(content, r"<h2[^>]*>\s*Explora\s*</h2>")

    def test_explora_lists_the_three_areas(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        for area in ("Tecnologia", "Fotografia", "Fitness"):
            self.assertRegex(content, rf"<h3[^>]*>\s*{area}\s*</h3>")

    def test_explora_gives_more_visual_weight_to_technology_and_photography(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # Tecnologia e Fotografia usam a variante "primary"; Fitness usa
        # "secondary" — a hierarquia visual pedida (FR-003 / sitemap-v1).
        self.assertEqual(content.count("area-card area-card--primary"), 2)
        self.assertEqual(content.count("area-card area-card--secondary"), 1)

    def test_explora_areas_do_not_link_to_fictitious_urls(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # Nenhuma das três áreas tem página própria ainda — os cartões
        # são <article>, não <a>, e não podem apontar para nenhuma URL.
        for area in ("Tecnologia", "Fotografia", "Fitness"):
            pattern = re.compile(rf"<a[^>]*>\s*{area}\s*</a>")
            self.assertNotRegex(content, pattern)

    def test_explora_areas_show_pending_status(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # Mesmo padrão de "estados vazios" já usado na navegação:
        # comunicar honestamente que a área ainda não é uma página.
        self.assertEqual(
            content.count('<span class="area-card__status">Em preparação</span>'),
            3,
        )

    def test_explore_cta_links_to_explora_section(self):
        response = self.client.get(reverse("pages:home"))

        self.assertContains(response, 'href="#explora"')


class FoundationCheckTests(TestCase):
    def test_foundation_page_responds(self):
        response = self.client.get(reverse("pages:foundation-check"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "pages/foundation-check.html")
        self.assertContains(response, "Development Foundation V1")

    def test_admin_is_available(self):
        response = self.client.get("/admin/login/")

        self.assertEqual(response.status_code, 200)

    def test_foundation_page_uses_static_asset(self):
        response = self.client.get(reverse("pages:foundation-check"))

        self.assertContains(response, "/static/css/base.css")

    def test_foundation_languages_are_configured(self):
        self.assertEqual(settings.LANGUAGE_CODE, "pt-pt")
        self.assertEqual(
            {code for code, _ in settings.LANGUAGES},
            {"pt-pt", "en", "fr"},
        )
