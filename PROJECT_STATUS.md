# Estado do Projeto

## Versão

0.2.2

## Fase

FASE 5 — Development Foundation V1

## Estado

Development Foundation V1 validada. Home com Hero e secção Explora
implementadas (Tecnologia e Fotografia em destaque, Fitness secundária),
ainda sem páginas próprias por área, sem projetos reais e sem as
restantes secções da Home (Sobre mim, Projetos em destaque,
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

## Em progresso

- Decisões técnicas ainda pendentes para produção (paleta final,
  tipografia final, light/dark mode, elemento visual da Hero, stack de
  base de dados de produção).
- Conteúdo e ligações finais de cada área (Tecnologia, Fotografia,
  Fitness) continuam pendentes — sem páginas próprias nesta fase.

## Próximo passo

- Decidir e implementar a próxima secção da Home (por exemplo, "Sobre
  mim" ou "Projetos em destaque"), apenas com conteúdo real aprovado —
  sem inventar texto, projetos ou fotografias.

## Nota

Não existem funcionalidades de software concluídas nesta fase além da
Foundation, do incremento visual da Home e da secção Explora.

Não implementar o portfólio final, conteúdo fictício, deployment, integrações,
autenticação completa ou infraestrutura complexa nesta fase.
