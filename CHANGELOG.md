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
