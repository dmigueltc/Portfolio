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

    def test_navigation_sobre_link_is_functional(self):
        response = self.client.get(reverse("pages:home"))

        # "Sobre" passa a link real, apontando sempre para a Home +
        # âncora — funciona mesmo a partir de páginas sem a secção
        # (ex.: /foundation-check/), não apenas "#sobre" isolado.
        self.assertContains(response, 'href="/#sobre"')

    def test_navigation_projetos_link_is_functional(self):
        response = self.client.get(reverse("pages:home"))

        # "Projetos" segue o mesmo padrão já aplicado a "Sobre": link
        # real para a Home + âncora, não apenas "#projetos" isolado.
        self.assertContains(response, 'href="/#projetos"')

    def test_navigation_pending_areas_are_not_links(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # Tecnologia/Fotografia/Fitness/Contacto ainda não têm página
        # de destino nesta fase — devem aparecer como
        # <span class="site-nav__item--pending">, nunca como <a href="...">.
        # "Sobre" e "Projetos" já não estão nesta lista: passaram a
        # links funcionais.
        pending_areas = (
            "Tecnologia",
            "Fotografia",
            "Fitness",
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
        # Contagem restrita à própria secção Explora — a secção
        # Tecnologia também reutiliza a classe area-card__status para
        # o seu próprio estado "Em preparação" dos projetos.
        explora_section = re.search(
            r'<section id="explora".*?</section>', content, re.DOTALL
        )
        self.assertIsNotNone(explora_section)
        self.assertEqual(
            explora_section.group(0).count(
                '<span class="area-card__status">Em preparação</span>'
            ),
            3,
        )

    def test_explore_cta_links_to_explora_section(self):
        response = self.client.get(reverse("pages:home"))

        self.assertContains(response, 'href="#explora"')


class AboutSectionTests(TestCase):
    def test_about_section_exists(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        self.assertContains(response, 'id="sobre"')
        # Título é um h2 — mesma hierarquia da Explora, sem saltar níveis.
        self.assertRegex(content, r"<h2[^>]*>\s*Sobre mim\s*</h2>")

    def test_about_uses_only_approved_base_statement(self):
        response = self.client.get(reverse("pages:home"))

        # A frase-base aprovada tem de estar presente tal como aprovada
        # (aqui com o nome antecipado, sem alterar o resto do texto).
        self.assertContains(
            response,
            "estudante de Engenharia Inform\xe1tica, interessado em "
            "desenvolvimento, tecnologia e cria\xe7\xe3o de conte\xfado.",
        )

    def test_about_does_not_invent_unapproved_content(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # Nada de experiência profissional, empresas, prémios, anos ou
        # formação adicional inventados — nenhum destes termos deve
        # aparecer em lado nenhum da página.
        forbidden_terms = (
            "anos de experiência",
            "empresa",
            "prémio",
            "certificado",
            "certificação",
            "curso de",
            "cliente",
        )
        for term in forbidden_terms:
            self.assertNotIn(
                term,
                content.lower(),
                f"Conteúdo não aprovado encontrado: '{term}'.",
            )

    def test_about_links_to_explora_not_a_fictitious_page(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # A Home não cria uma página "/sobre/" nesta fase; a ligação
        # dentro da secção aponta para a Explora já existente na mesma
        # página, não para uma URL inventada.
        self.assertNotContains(response, 'href="/sobre/"')
        self.assertIn('<a href="#explora">', content)

    def test_about_layout_is_ready_for_future_media_without_rendering_one(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # Sem fotografia pessoal nesta fase: nenhum <img> na secção.
        about_section = re.search(
            r'<section id="sobre".*?</section>', content, re.DOTALL
        )
        self.assertIsNotNone(about_section)
        self.assertNotIn("<img", about_section.group(0))


class TechnologySectionTests(TestCase):
    def test_technology_section_exists(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        self.assertContains(response, 'id="tecnologia"')
        self.assertRegex(content, r"<h2[^>]*>\s*Tecnologia\s*</h2>")

    def test_technology_lists_documented_topics(self):
        response = self.client.get(reverse("pages:home"))

        # Temas exatamente como documentados em sitemap-v1.md
        # ("Tecnologia" > Conteúdo previsto) — nenhuma tecnologia
        # específica (linguagem, framework, ferramenta) inventada.
        for topic in (
            "Desenvolvimento e programação",
            "Desenvolvimento web",
            "Hardware e computadores",
            "Otimização e troubleshooting de PC",
        ):
            self.assertContains(response, topic)

    def test_technology_does_not_invent_unapproved_content(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # Mesma cautela da secção Sobre mim: nada de experiência,
        # empresas, prémios, clientes ou tecnologias específicas não
        # documentadas (linguagens/frameworks concretos não aprovados).
        forbidden_terms = (
            "anos de experiência",
            "empresa",
            "cliente",
            "prémio",
            "certificado",
            "certificação",
            "python",
            "javascript",
            "react",
        )
        for term in forbidden_terms:
            self.assertNotIn(
                term,
                content.lower(),
                f"Conteúdo não aprovado encontrado: '{term}'.",
            )

    def test_technology_projects_area_has_no_fictitious_projects(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        tech_section = re.search(
            r'<section id="tecnologia".*?</section>', content, re.DOTALL
        )
        self.assertIsNotNone(tech_section)
        # Nenhum link para projeto, e o estado "Em preparação" está
        # presente — nenhum projeto real ainda, nenhum fictício.
        self.assertNotIn("<a ", tech_section.group(0))
        self.assertIn(
            '<span class="area-card__status">Em preparação</span>',
            tech_section.group(0),
        )

    def test_technology_does_not_create_dedicated_page(self):
        # Nesta fase não existe uma página "/tecnologia/" própria — é
        # apenas uma secção da Home, não uma rota nova.
        response = self.client.get(reverse("pages:home"))

        self.assertNotContains(response, 'href="/tecnologia/"')


class FeaturedProjectsSectionTests(TestCase):
    def test_projects_section_exists(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        self.assertContains(response, 'id="projetos"')
        self.assertRegex(content, r"<h2[^>]*>\s*Projetos em destaque\s*</h2>")

    def test_projects_section_shows_pending_status(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        projects_section = re.search(
            r'<section id="projetos".*?</section>', content, re.DOTALL
        )
        self.assertIsNotNone(projects_section)
        self.assertIn(
            '<span class="area-card__status">Em preparação</span>',
            projects_section.group(0),
        )

    def test_projects_section_has_no_fictitious_projects(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        projects_section = re.search(
            r'<section id="projetos".*?</section>', content, re.DOTALL
        )
        self.assertIsNotNone(projects_section)
        section_html = projects_section.group(0)

        # Nenhum cartão de projeto, nenhuma ligação (GitHub, demo, ou
        # qualquer outra), nenhuma imagem — só o estado "Em preparação".
        self.assertNotIn("<article", section_html)
        self.assertNotIn("<a ", section_html)
        self.assertNotIn("<img", section_html)

    def test_projects_section_does_not_invent_content(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # Nada de nomes de projeto, tecnologias específicas, clientes,
        # empresas, métricas ou datas inventadas.
        forbidden_terms = (
            "github.com",
            "cliente",
            "empresa",
            "%",
            "utilizadores",
            "downloads",
        )
        for term in forbidden_terms:
            self.assertNotIn(
                term,
                content.lower(),
                f"Conteúdo não aprovado encontrado: '{term}'.",
            )

    def test_projects_section_does_not_create_dedicated_page(self):
        # Nesta fase não existe nenhuma página "/projetos/" própria.
        response = self.client.get(reverse("pages:home"))

        self.assertNotContains(response, 'href="/projetos/"')

    def test_projects_section_integrates_after_technology(self):
        response = self.client.get(reverse("pages:home"))
        content = response.content.decode()

        # Confirma a posição na Home: depois de Tecnologia, antes do
        # footer (DEC-009: Sobre mim > Projetos em destaque > Footer;
        # Tecnologia foi inserida entre Sobre mim e Projetos por
        # DEC-016).
        tech_index = content.find('id="tecnologia"')
        projects_index = content.find('id="projetos"')
        footer_index = content.find('class="site-footer"')

        self.assertGreater(tech_index, -1)
        self.assertGreater(projects_index, tech_index)
        self.assertGreater(footer_index, projects_index)


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
