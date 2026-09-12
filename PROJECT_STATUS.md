# Estado do Projeto

## Versão

0.2.9

## Fase

FASE 5 — Development Foundation V1

## Estado

Development Foundation V1 validada. Home com Hero, Explora, Sobre mim,
Tecnologia, Projetos em destaque e Fotografia/criação implementadas,
ainda sem páginas próprias por área, sem projetos ou fotografias reais
e sem a secção Contacto.

## Concluído

- Visão inicial do projeto.
- Estrutura documental base.
- Estratégia AI-agnostic.
- Identidade pública: Miguel Cardoso.
- Conceito: portfólio profissional + hub pessoal.
- Público principal e público secundário definidos.
- Áreas conceptuais iniciais definidas: Tecnologia, Fotografia e Fitness.
- Estrutura conceptual da Home definida.
- Direção visual definida como minimalista pessoal/criativa.
- Development Foundation V1 documentada.
- Development Foundation V1 validada (manage.py check e suite de testes a
  passar).
- Primeiro incremento visual da Home: tokens de design (cores, tipografia,
  espaçamento, radius, breakpoints), layout base, header com navegação,
  hero com identidade/posicionamento/CTA, footer básico, estrutura
  responsiva e acessibilidade base (skip-link, foco visível, alvos de
  toque, redução de movimento). Estabilizado e aprovado visualmente.
- Verificação da Foundation preservada em `/foundation-check/` (antes em
  `/`), agora que `/` serve a Home.
- Secção Explora da Home: grid extensível com cartões para Tecnologia,
  Fotografia (maior peso visual) e Fitness (peso secundário); cada área
  sem página própria ainda, apresentada com estado "Em preparação" em
  vez de simular uma ligação funcional. CTA "Explore" da Hero passa a
  apontar para esta secção (destino real, deixou de ser inerte).
  Aprovada visualmente, incluindo ajuste de alinhamento dos cartões.
- Secção Sobre mim da Home: texto restrito ao já aprovado (frase-base
  de posicionamento + referência às três áreas já presentes na
  Explora), sem fotografia pessoal, com layout preparado para receber
  uma imagem futuramente sem reconstrução (`.about__layout--with-media`
  em layout.css). Item "Sobre" da navegação passa a link funcional
  (`/#sobre`), incluindo a partir de páginas sem essa secção. Aprovada
  visualmente.
- Secção Tecnologia da Home (extensão de DEC-009 — ver DEC-016 em
  decision-log.md): introdução parafraseada de FR-005, temas exatos do
  sitemap-v1.md ("Tecnologia" > Conteúdo previsto), e espaço reservado
  para projetos reais com estado "Em preparação". Sem tecnologias,
  projetos ou competências específicas inventadas. Item "Tecnologia" da
  navegação continua pendente (não foi ligado à secção nesta fase).
  Aprovada visualmente.
- Secção Projetos em destaque da Home (posição prevista em DEC-009,
  aplicada após a Tecnologia — ver DEC-016): apenas introdução e
  estado "Em preparação", sem nenhum cartão de projeto — ainda não
  existem projetos pessoais finais aprovados (FR-006). Item "Projetos"
  da navegação passa a link funcional (`/#projetos`), seguindo o mesmo
  padrão já aplicado a "Sobre" (não é uma decisão nova). Aprovada
  visualmente.
- Secção Fotografia/criação da Home, revista para uma galeria
  masonry/waterfall via CSS columns (DEC-018, referência conceptual
  Pinterest, sem JavaScript e sem cópia da plataforma): imagens de
  proporções variadas (portrait, landscape, square) e um item que
  representa vídeo, com indicador de play discreto. A lista de temas e
  o "Em preparação" repetido da primeira versão foram removidos da
  apresentação visual. Assets DEMO temporários adicionados
  (`static/images/photography/demo/`, ver README nessa pasta), sem
  qualquer conteúdo real. DEC-017 (Instagram como plataforma de
  publicação; portfólio como curadoria) e DEC-018 registadas no
  decision-log.md. Item "Fotografia" da navegação passa a link
  funcional (`/#fotografia`).
  Revisão visual (2ª iteração): os 7 assets demo passaram de
  gradientes simples a composições abstratas por camadas (sugerindo
  géneros fotográficos), o watermark "DEMO" tornou-se um pequeno selo
  discreto no canto, a ordem das imagens foi escolhida
  deliberadamente para dar ritmo à composição, o hover ganhou um
  overlay subtil + leve aumento de brilho, e o indicador de vídeo
  ficou mais pequeno e integrado.
  Revisão visual (3ª e última iteração desta fase): os assets demo
  passaram de gráficos vetoriais nítidos (SVG) a imagens rasterizadas
  (.jpg) geradas localmente com desfoque gaussiano, grão e vinheta —
  muito mais próximas do aspeto de uma fotografia real, ainda 100%
  geradas por código (sem fotografias de terceiros; ver README da
  pasta demo para a origem exata). A tentativa de dar à Fotografia um
  container mais largo (`.container--wide`) foi revertida: a secção
  volta a usar exatamente o mesmo `.container` das restantes secções,
  para manter o mesmo eixo esquerdo/direito em toda a Home — o token
  `--content-max-width-wide` foi removido por deixar de ter uso. O
  espaço entre a introdução e a galeria foi reduzido.
  Ajuste final (4ª iteração): dentro do mesmo `.container` (sem voltar
  a alargá-lo), a galeria passou de um máximo de 4 para 3 colunas —
  cada imagem fica maior e com mais presença, sem alterar o container
  global. Gap entre imagens reduzido (`--space-lg` → `--space-md`),
  para uma sensação mais coesa de galeria do que de cartões isolados.
  Ordem das 7 imagens ajustada para abrir com uma imagem vertical
  claramente dominante. Com esta entrega, a apresentação visual da
  secção Fotografia fica fechada nesta fase.

## Em progresso

- Decisões técnicas ainda pendentes para produção (paleta final,
  tipografia final, light/dark mode, elemento visual da Hero e de
  Sobre mim, stack de base de dados de produção).
- Conteúdo e ligações finais de cada área (Tecnologia, Fotografia,
  Fitness) continuam pendentes — sem páginas próprias nesta fase.
- Página "Sobre" completa (fora da Home) continua pendente de conteúdo
  final — não foi criada nesta fase.
- Página "Tecnologia" completa (fora da Home, FR-005) continua pendente
  — a secção implementada é um resumo na Home, não a página dedicada.
- Página "Projetos" completa (fora da Home, FR-006) continua pendente —
  requer projetos reais e, no futuro, sistema de gestão de conteúdo.
- Página "Fotografia" completa (fora da Home, FR-007) continua
  pendente — a secção implementada é um resumo na Home.
- Assets DEMO da Fotografia (`static/images/photography/demo/`) devem
  ser removidos e substituídos por posts reais do Instagram assim que
  existir uma seleção aprovada (ver DEC-017/DEC-018).
- Estrutura de cartão de projeto ("Project Card") ainda não desenhada —
  deliberadamente adiada até existirem projetos reais que definam os
  campos necessários (título, categoria, tecnologias, links, etc.).
- Decidir se o item "Tecnologia" da navegação deve passar a link para
  `/#tecnologia`, tal como já aconteceu com "Sobre", "Projetos" e
  "Fotografia".
- PEND-012: decidir se Fitness recebe secção própria na Home ou
  permanece apenas como cartão na Explora.

## Próximo passo

- Decidir e implementar a próxima secção da Home (por exemplo,
  "Fitness" ou "Contacto"), apenas com conteúdo real aprovado — sem
  inventar texto, projetos ou fotografias.

## Nota

Não existem funcionalidades de software concluídas nesta fase além da
Foundation e das secções Hero, Explora, Sobre mim, Tecnologia, Projetos
em destaque e Fotografia/criação da Home.

A secção Tecnologia estende a estrutura de Home aprovada em DEC-009
(que não previa uma secção própria de Tecnologia, apenas o cartão na
Explora) — extensão registada em DEC-016 do decision-log.md. A secção
Projetos em destaque já estava prevista em DEC-009; a sua posição
(depois de Tecnologia) segue essa mesma extensão. A secção Fotografia
introduz duas decisões de produto novas: DEC-017 (Instagram como
plataforma de publicação, portfólio como curadoria, sem depender da
API do Instagram para funcionar — compatível com DEC-013/RNF-010 já
existentes) e DEC-018 (apresentação editorial/masonry com referência
conceptual ao Pinterest, e uso de assets DEMO temporários enquanto não
existir uma seleção real de posts).

Não implementar o portfólio final, conteúdo fictício, deployment, integrações,
autenticação completa ou infraestrutura complexa nesta fase.
