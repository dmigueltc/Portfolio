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

## 0.2.6

- Secção Fotografia/criação na Home, posicionada depois de Projetos em
  destaque e antes do Footer. Implementada como galeria
  masonry/waterfall via CSS `columns` (sem JavaScript) — referência
  conceptual ao princípio visual do Pinterest (várias colunas, alturas
  naturais por proporção da própria imagem, ritmo editorial), sem
  copiar a plataforma nem construir galeria tradicional (sem filtros,
  paginação ou lightbox). 2 colunas em mobile, 3 em tablet, 4 em
  desktop — breakpoints coerentes com os já existentes.
- Removida da apresentação visual a lista de temas (Fotografia,
  Edição, Criação visual, Vídeo) e o "Em preparação" repetido da
  primeira versão — a galeria passa a ser o elemento dominante da
  secção, com apenas uma frase curta de introdução.
- Assets DEMO temporários adicionados em
  `static/images/photography/demo/` (6 SVGs abstratos gerados por
  código — gradientes com as cores do design system + texto "DEMO" —
  mais um README.md a documentar explicitamente que são temporários).
  Proporções variadas: portrait (3:4, 2:3, 4:5), landscape (4:3),
  square (1:1), e um item landscape com ícone de play embutido a
  representar vídeo. Nenhuma fotografia real, de terceiros, ou
  associada a qualquer post real do Instagram.
- Indicador discreto de vídeo (`.photo-card__play`, pequeno badge no
  canto, sempre visível — não depende de hover) no item de exemplo
  correspondente. Sem `<video>`, sem autoplay.
- `.photo-card` reutiliza a preparação já feita no incremento anterior
  para posts reais do Instagram (link externo acessível,
  `target="_blank"`, `rel="noopener noreferrer"`) — nesta fase cada
  item é um `<figure>` sem link, já que não existem posts reais.
- Duas decisões novas registadas no decision-log.md: **DEC-017**
  (Instagram como plataforma de publicação; portfólio como curadoria —
  decisão do incremento anterior, agora formalmente registada) e
  **DEC-018** (apresentação editorial/masonry com referência ao
  Pinterest + uso de assets DEMO temporários). PEND-012 atualizado:
  já só falta decidir sobre Fitness.
- Testes atualizados/novos: existência da galeria, variedade de
  proporções demo, identificação clara das imagens como temporárias
  (alt text + nota visível), indicador de vídeo sem autoplay, ausência
  de qualquer link/URL do Instagram ou API, ausência de conteúdo
  inventado, ausência de página "/fotografia/" dedicada, e posição
  correta na Home.

## 0.2.7

- Refinamento visual da galeria de Fotografia (sem alterar o conceito
  masonry nem a arquitetura — mesma DEC-018, sem nova decisão):
  - Assets demo redesenhados: passam de blocos de gradiente simples a
    composições abstratas por camadas (formas geométricas + gradientes)
    que sugerem géneros fotográficos diferentes — retrato (vinheta
    suave), arquitetura (skyline abstrato), street/urbano (diagonais de
    contraste), paisagem (horizonte), edição criativa (duotone
    diagonal), retrato suave (bokeh simulado). Continuam 100%
    abstratos, gerados por código, sem qualquer fotografia real ou de
    terceiros.
  - Novo 7º asset (`demo-07-landscape-wide.svg`, paisagem/horizonte)
    para mais variedade de ritmo na composição.
  - Watermark "DEMO" tornado discreto: passa de texto grande centrado
    com proporção (ex.: "DEMO · 3:4") a um pequeno selo no canto
    inferior esquerdo de cada imagem — a imagem volta a ser o primeiro
    elemento a chamar a atenção.
  - Ordem das 7 imagens na galeria escolhida deliberadamente (retrato
    alto, quadrado, horizontal, retrato, vídeo, retrato suave,
    horizontal largo) para dar ritmo intencional à composição, em vez
    de uma sequência arbitrária.
  - Vídeo demo redesenhado com o mesmo tratamento visual das
    fotografias (deixa de ser um bloco escuro com um grande ícone de
    play central); o indicador de vídeo (`.photo-card__play`) fica
    menor, mais discreto e no canto oposto ao watermark.
  - Hover/focus da galeria reforçado com um overlay subtil em
    gradiente + leve aumento de brilho, além do zoom já existente —
    sensação mais editorial, sem elementos pesados. `focus-visible`
    mantido; `prefers-reduced-motion` continua coberto pela regra
    global já existente em base.css.
  - Novo token `--content-max-width-wide` (90rem) e classe
    `.container--wide`, aplicados apenas à secção Fotografia, para lhe
    dar mais espaço horizontal sem tornar a secção full-bleed nem
    alterar o `.container` usado pelas restantes secções.
- Testes ampliados: as 7 imagens demo (incluindo a nova), contagem de
  itens da galeria, e confirmação de que a secção usa o container mais
  largo.

## 0.2.8

- Revisão final dos assets DEMO da Fotografia: substituídos os 7 SVGs
  vetoriais por imagens `.jpg` geradas localmente com um script
  auxiliar (`generate_demo_images.py`, fora da app Django) — gradientes
  + desfoque gaussiano + grão + vinheta, muito mais próximas do
  aspeto de uma fotografia desfocada do que gráficos vetoriais
  nítidos. Continuam 100% geradas por código, sem qualquer fotografia
  real ou de terceiros (ver README atualizado em
  `static/images/photography/demo/` a documentar a origem exata).
  Não foram usadas imagens externas/de stock — o ambiente de execução
  não tem acesso a bancos de imagens da internet, e mesmo que tivesse,
  a licença de qualquer imagem de terceiros teria de ser verificável e
  documentada, o que não é possível garantir de forma fiável nesta
  fase; a alternativa gerada localmente evita esse risco por completo.
- Watermark "DEMO" mantido, com o mesmo tratamento discreto (selo
  pequeno no canto).
- Nova ordem das 7 imagens na galeria, pensada para não parecer
  "organizada em blocos": horizontal → retrato alto → quadrado →
  retrato → vídeo → horizontal largo → retrato suave.
- Espaço entre a introdução e a galeria reduzido (`.photo__intro`:
  `--space-2xl` → `--space-lg`) — a galeria aparece mais depressa.
- **Correção de alinhamento**: a classe `.container--wide` e o token
  `--content-max-width-wide` (introduzidos na iteração anterior para
  dar mais largura à Fotografia) foram removidos. A secção volta a
  usar exatamente o `.container` das restantes secções — mesmo eixo
  esquerdo/direito em toda a Home (Explora, Sobre mim, Tecnologia,
  Projetos em destaque e Fotografia), confirmado em desktop, tablet e
  mobile. Nenhuma outra secção foi alterada para se ajustar à
  Fotografia — foi a Fotografia que voltou à consistência estrutural.
- Testes atualizados: extensões `.jpg` em vez de `.svg`; o teste do
  "container mais largo" foi substituído por um teste que confirma
  que Fotografia usa a mesma classe `.container` que Tecnologia e
  Projetos em destaque.
- Nenhuma decisão arquitetural nova — esta entrada aplica/reverte
  decisões de implementação já cobertas por DEC-018, sem alterar o
  seu conteúdo.

## 0.2.9

- Ajuste final de presença da galeria de Fotografia, sem tocar no
  container (continua exatamente `.container`, igual às restantes
  secções):
  - Máximo de colunas do masonry reduzido de 4 para 3
    (`.photo-grid`) — dentro da mesma largura, cada imagem fica
    maior e mais presente, em vez de mais compacta.
  - Gap entre colunas e entre itens reduzido (`--space-lg` →
    `--space-md`), para uma sensação mais coesa de galeria em vez de
    cartões isolados.
  - Ordem das 7 imagens ajustada: a imagem vertical mais forte
    (`demo-04-portrait-tall.jpg`) passa a abrir a composição, seguida
    de horizontal, quadrado, retrato, vídeo, horizontal largo e
    retrato suave.
- Mantidos sem alterações: os 7 assets `.jpg`, o watermark discreto,
  o indicador de vídeo, e a filosofia de hover (zoom subtil + overlay
  ligeiro), conforme pedido.
- Testes existentes confirmam que o comportamento se mantém (nenhum
  teste verifica número de colunas ou valores de gap diretamente,
  por serem detalhes puramente visuais de CSS); o teste de
  alinhamento (`.container` igual às restantes secções) continua a
  passar sem alterações.
- Nenhuma decisão arquitetural nova.
