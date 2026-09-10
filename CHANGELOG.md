# Changelog

Todas as alteracoes relevantes deste projeto devem ser documentadas neste ficheiro.

## 0.1.0

- Criacao da estrutura documental inicial.
- Definicao preliminar da stack tecnologica.
- Definicao da estrategia multilingue.
- Definicao da independencia face a ferramentas de IA especificas.

## 0.2.0

- Atualização do planeamento mestre do portfólio Miguel Cardoso.
- Registo do conceito portfólio profissional + hub pessoal.
- Definição de público principal e secundário.
- Registo das áreas conceptuais Tecnologia, Fotografia e Fitness.
- Definição da estrutura conceptual da Home.
- Criação da arquitetura da informação.
- Criação dos princípios de design.
- Criação do guia de desenvolvimento assistido por IA.
- Criação do decision log.
- Clarificação de que Python está confirmado, PHP está excluído e Django/PostgreSQL permanecem decisões técnicas pendentes ou preliminares.

## 0.2.1

- Validação da Development Foundation V1 (manage.py check e suite de testes).
- Primeiro incremento visual da Home: tokens de design, layout base,
  header com navegação, hero (identidade, posicionamento, áreas, CTA),
  footer básico, responsividade mobile-first e acessibilidade base.
- Rota "/" passa a servir a Home; verificação da Foundation move-se para
  "/foundation-check/", sem perder funcionalidade.
- Correções de estabilização após revisão crítica do incremento:
  ajuste da hierarquia tipográfica fluida aos limites documentados,
  skip-link visível ao focar, alvos de toque da navegação/marca,
  clarificação da limitação técnica dos tokens de breakpoint,
  escolha explícita e documentada da label "Início" na navegação,
  reforço do teste de navegação pendente, e separação do CTA "Explore"
  de qualquer destino ainda não implementado.

## 0.2.2

- Secção Explora na Home: grid extensível (`repeat(auto-fit, minmax(...))`)
  com cartões para Tecnologia, Fotografia (maior peso visual — variante
  "primary") e Fitness (peso secundário — variante "secondary"),
  conforme FR-003 e ux-specification-v1.md §5.
- Novo token `--card-grid-min-width` em tokens.css para a largura mínima
  de coluna da grid, reutilizável por futuras grids de cartões.
- Cada área aparece como `<article>` com estado "Em preparação" — sem
  página própria nem ligação funcional ainda, seguindo o mesmo padrão
  de estados vazios já usado na navegação (ux-specification-v1.md §13).
- CTA "Explore" da Hero passa a ter destino real (`#explora`), deixando
  de ser um elemento inerte agora que a secção existe.
- Testes novos para a existência da secção, as três áreas, a hierarquia
  visual Tecnologia/Fotografia vs. Fitness, a ausência de ligações
  fictícias e o estado "Em preparação" de cada área.
- Ajuste visual: os três cartões da Explora ficam alinhados (mesmo topo
  e base) quando partilham a mesma linha da grid em desktop, via
  `align-items: stretch` (comportamento nativo do CSS Grid) — sem
  alturas fixas. Em mobile, cada cartão mantém a sua altura natural.

## 0.2.3

- Secção Sobre mim na Home: texto restrito ao já aprovado — a frase-base
  de posicionamento ("estudante de Engenharia Informática, interessado
  em desenvolvimento, tecnologia e criação de conteúdo") com o nome
  antecipado, e uma frase que descreve a própria estrutura do site
  (Tecnologia/Fotografia em destaque, Fitness secundária), já
  implementada na Explora. Sem experiência, empresas, projetos,
  competências, prémios ou formação adicional inventados.
- Ligação interna "Ver as áreas do portfólio ↓" para `#explora` —
  não é criada nenhuma página "/sobre/" nesta fase.
- Sem fotografia pessoal; `.about__layout` preparado com uma classe
  modificadora reservada (`--with-media`) para, no futuro, receber uma
  imagem em duas colunas no desktop sem reconstruir a secção.
- Item "Sobre" da navegação passa a link funcional (`/#sobre`, não
  apenas `#sobre`), para continuar a funcionar também a partir de
  páginas sem esta secção (ex.: `/foundation-check/`). Restantes itens
  (Tecnologia, Fotografia, Fitness, Projetos, Contacto) continuam
  pendentes, sem alteração.
- Testes novos para a existência da secção, o conteúdo aprovado, a
  ausência de conteúdo inventado, a ausência de URLs fictícias e a
  ausência de imagem nesta fase.

## 0.2.4

- Secção Tecnologia na Home: introdução parafraseada da descrição de
  FR-005, e os quatro temas exatamente como documentados em
  sitemap-v1.md ("Tecnologia" > Conteúdo previsto) — Desenvolvimento e
  programação, Desenvolvimento web, Hardware e computadores,
  Otimização e troubleshooting de PC. Apresentados como texto simples,
  não como badges/skills com percentagens.
- Espaço reservado para projetos tecnológicos reais, com o mesmo
  estado "Em preparação" já usado na Explora (reutiliza a classe
  `.area-card__status`, sem duplicar a regra). Nenhum projeto,
  tecnologia específica, empresa ou competência inventada.
- Novo token `--prose-max-width` (42rem) em tokens.css — já havia o
  mesmo valor isolado em `.hero__statement` e `.about__content`; os
  três sítios passam agora a usar o token em vez de repetir o número
  (substituição mecânica, sem alteração visual).
- Extensão da estrutura de Home aprovada em DEC-009 (que não previa
  secção própria de Tecnologia) — registada em DEC-016 do
  decision-log.md.
- Item "Tecnologia" da navegação NÃO foi alterado nesta fase — continua
  pendente, por não ter sido pedido explicitamente (ao contrário do que
  aconteceu com "Sobre" no incremento anterior).
- Testes novos para a existência da secção, os temas documentados, a
  ausência de conteúdo/tecnologias inventadas, a ausência de projetos
  fictícios e a confirmação de que não foi criada nenhuma página
  "/tecnologia/".

## 0.2.5

- Secção Projetos em destaque na Home, posicionada depois de Tecnologia
  e antes do Footer (DEC-009 previa esta secção depois de Sobre mim;
  a posição exata segue a extensão já registada em DEC-016).
- Sem nenhum cartão de projeto: ainda não existem projetos pessoais
  finais aprovados (FR-006, information-architecture.md, sitemap-v1.md
  "6. Projetos"). Apenas introdução curta e o estado "Em preparação"
  (reutiliza `.area-card__status`, já usado na Explora e Tecnologia).
- Estrutura de "Project Card" deliberadamente NÃO desenhada nesta fase
  — ficaria a adivinhar campos sem projetos reais para os validar.
  Quando existirem, um grid pode reutilizar o padrão já estabelecido
  em `.explora__grid`/`--card-grid-min-width` (tokens.css), sem
  reconstruir a secção.
- Item "Projetos" da navegação passa a link funcional (`/#projetos`),
  seguindo exatamente o mesmo padrão já aplicado a "Sobre" — não é
  registada como decisão nova (é a mesma decisão a ser reaplicada).
- Testes novos para a existência da secção, o estado "Em preparação",
  a ausência de projetos/tecnologias/imagens/links fictícios, a
  ausência de uma página "/projetos/" dedicada, e a posição correta
  na Home (depois de Tecnologia, antes do Footer).
