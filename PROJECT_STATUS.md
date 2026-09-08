# Estado do Projeto

## Versão

0.2.3

## Fase

FASE 5 — Development Foundation V1

## Estado

Development Foundation V1 validada. Home com Hero, Explora e Sobre mim
implementadas, ainda sem páginas próprias por área, sem projetos reais
e sem as restantes secções da Home (Projetos em destaque,
Fotografia/criação, Contacto).

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
  (`/#sobre`), incluindo a partir de páginas sem essa secção.

## Em progresso

- Decisões técnicas ainda pendentes para produção (paleta final,
  tipografia final, light/dark mode, elemento visual da Hero e de
  Sobre mim, stack de base de dados de produção).
- Conteúdo e ligações finais de cada área (Tecnologia, Fotografia,
  Fitness) continuam pendentes — sem páginas próprias nesta fase.
- Página "Sobre" completa (fora da Home) continua pendente de conteúdo
  final — não foi criada nesta fase.

## Próximo passo

- Decidir e implementar a próxima secção da Home (por exemplo,
  "Projetos em destaque" ou "Fotografia/criação"), apenas com conteúdo
  real aprovado — sem inventar texto, projetos ou fotografias.

## Nota

Não existem funcionalidades de software concluídas nesta fase além da
Foundation e das secções Hero, Explora e Sobre mim da Home.

Não implementar o portfólio final, conteúdo fictício, deployment, integrações,
autenticação completa ou infraestrutura complexa nesta fase.
