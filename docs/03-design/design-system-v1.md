# Design System V1

Este documento define uma proposta inicial de design system para o portfólio Miguel Cardoso. O objetivo é criar uma base visual clara, simples e extensível, sem obrigar a implementação técnica nem a escolha final de framework.

## 1. Escopo

Este design system serve como guia para futuras decisões de UI e desenvolvimento frontend. A intenção é suportar:

- home e navegação;
- páginas temáticas;
- áreas principais (Tecnologia, Fotografia, Fitness);
- projetos e conteúdos futuros;
- tradução em PT-PT, EN e FR;
- expansão para novas áreas sem redimensionar o sistema visual inteiro.

Não define interfaces técnicas, CSS final ou componentes implementados. Em vez disso, estrutura os princípios e os tokens visuais que qualquer implementação futura deve seguir.

## 2. Direção visual

### Decisão recomendada

A direção visual recomendada para a V1 é:

- minimalista pessoal/criativa;
- clean e elegante;
- profissional sem perder personalidade;
- visualmente equilibrado;
- simples sem ser vazio;
- moderno sem cair em excesso tecnológico ou “template genérico”.

Princípio central:

> Minimalismo sem ser vazio; criatividade sem ser exagerada.

## 3. Princípios gerais

- Menos é mais, mas não sem personalidade.
- O design deve parecer “Miguel Cardoso”, não um template genérico.
- Tecnologia e Fotografia devem receber maior peso visual que Fitness.
- A estrutura deve aceitar novas áreas no futuro sem exigir redesign completo.
- As interações devem ser discretas, com foco em clareza e conforto visual.
- O design deve funcionar para público geral e para visitantes profissionais.

## 4. Paleta proposta

### Decisão recomendada

Como ainda não existe paleta final, recomenda-se uma paleta neutra e sofisticada, em tons quentes e naturais, com foco em conforto visual.

### Tokens conceptuais

```text
--color-background: #F5F1EC
--color-surface: #FAF7F4
--color-surface-strong: #EFE7E0
--color-text: #1B1A18
--color-text-muted: #5F5A54
--color-border: #D8D0C8
--color-accent: #A9754F
--color-accent-soft: #D9B998
--color-success: #3A5A48
--color-warning: #8E6F3A
--color-error: #7C4039
```

### Justificação

- o fundo neutro permite foco no conteúdo e no trabalho visual;
- o texto escuro em fundo claro garante legibilidade;
- o accent em tom terroso/açoado adiciona personalidade sem perder sobriedade;
- a gama cromática é pequena e controlada, reduzindo fadiga visual;
- a paleta permite evolução futura sem reconstrução completa da identidade.

### Regras

- Não utilizar mais do que 3 a 5 cores dominantes na interface.
- O accent deve ser usado com moderação.
- O design deve funcionar com contraste adequado em texto, botões e links.
- A cor deve ser administrada por tokens, não espalhada em vários ficheiros.

### Light/Dark mode

Decisão recomendada:

- manter como pendente para a fase técnica;
- permitir arquitetura que suporte tema futuro sem duplicar estilos desnecessariamente;
- não assumir que ambos os modos serão implementados na V1.

## 5. Tipografia

### Decisão recomendada

A proposta de tipografia deve ser moderna, elegante e confortável para leitura em português, inglês e francês.

### Sistema recomendado

- Fonte principal: Inter, Manrope ou outra sans moderna sem ser demasiado tecnológica.
- Fonte secundária: uma serif discreta apenas para momentos de destaque, como pequenos elementos editoriais ou frases curtas, se houver decisão posterior.
- A base deve evitar excesso de famílias tipográficas.

### Hierarquia conceptual

```text
Display / Hero: 48–64px
H1: 32–40px
H2: 24–32px
H3: 20–24px
Body: 16–18px
Small / captions: 12–14px
Labels / eyebrow: 11–12px
```

### Regras

- O texto principal deve ser simples e confiável.
- “Explorar”, “Sobre”, “Contacto”, “Projetos” e títulos de secção devem ser facilmente identificáveis.
- A tipografia deve suportar traduções mais longas em EN/FR sem quebra visual.
- A base da UI deve priorizar até 2 pesos de fonte principais para reduzir inconsistência.

## 6. Escala de espaçamento

### Escala recomendada

```text
XS = 4px
SM = 8px
MD = 12px
LG = 16px
XL = 24px
2XL = 32px
3XL = 48px
4XL = 64px
5XL = 96px
```

### Regras

- O layout deve respirar, sem parecer vazio.
- A Home deve ter espaços generosos em Hero e secções de conteúdo.
- O espaçamento deve servir a hierarquia e não a decoração.
- O sistema deve ser simples e consistente ao longo de todas as páginas.

## 7. Grid e layout

### Recomendações

- largura máxima do conteúdo: 1200px;
- grid baseada em 12 colunas, quando útil;
- gutters moderados (16–24px);
- uso de whitespace como ferramenta de organização;
- layouts limpos e com pouco ruído visual;
- evitar layouts densos ou sobrecarregados.

### Regra de composição

- primeiro: conteúdo e hierarquia;
- depois: decoração;
- a decoração não deve competir com a mensagem.

## 8. Radius, borders e sombras

### Decisão recomendada

- radius moderado e consistente;
- borders discretos;
- sombras mínimas e suaves;
- preferir contraste e clareza em vez de efeitos volumosos.

### Tokens conceptuais

```text
--radius-sm: 8px
--radius-md: 12px
--radius-lg: 18px
--shadow-soft: 0 8px 24px rgba(17, 17, 17, 0.05)
--border-width: 1px
```

## 9. Componentes principais

### Header / Navigation

Objetivo:
- facilitar navegação rápida;
- permitir identificação do site e das áreas principais;
- manter sensação leve e simples.

Quando usar:
- em todas as páginas;
- em versões mobile e desktop.

Quando não usar:
- quando a página é extremamente simples e não precisa de navegação secundária.

Comportamento:
- menu simples e legível;
- opções principais claras;
- foco em acesso às áreas principais sem excesso de opções;
- no mobile, menu com comportamento direto, sem depender de hover.

### Hero

Objetivo:
- identificar Miguel Cardoso imediatamente;
- apresentar a mensagem principal;
- introduzir a jornada de descoberta.

Elementos recomendados:
- nome;
- frase de posicionamento;
- elemento visual opcional;
- CTA principal “Explore”.

Regra:
- o Hero não deve depender obrigatoriamente de fotografia pessoal;
- pode usar composição, tipografia ou elemento gráfico e permitir evolução futura.

### Section

Objetivo:
- organizar visualmente o conteúdo por blocos;
- garantir ritmo e clareza.

Regras:
- cada secção deve ter uma hierarquia clara;
- títulos devem ser simples e diretos;
- o espaçamento deve variar de forma lógica.

### Area Card

Objetivo:
- representar Tecnologia, Fotografia e Fitness como áreas principais;
- facilitar a exploração do conteúdo.

Quando usar:
- na Home, Explora e em lisings de áreas.

Regras:
- devem ter identidade visual própria sem exagerar;
- suporte para imagem ou só texto, conforme o conteúdo;
- não obrigar a imagem em todas as áreas.

### Project Card

Objetivo:
- apresentar projetos futuros quando existam.

Quando usar:
- em listagens e destaques.

Regras:
- manter visual discreto;
- não criar projetos fictícios;
- permitir ocultar, destacar e destacar visualmente sem quebrar layout.

### Button / Link

Objetivo:
- guiar ação e navegação.

Estados:
- default;
- hover/focus;
- active/pressed;
- disabled (se aplicável).

Regra:
- devem possuir contraste adequado e estados visíveis.

### Tag / Label

Objetivo:
- categorizar projetos, áreas, tecnologias ou conteúdos.

Regras:
- discretos, consistentes, legíveis;
- não competir com o conteúdo principal.

### Footer

Objetivo:
- fechar navegação e disponibilizar informações essenciais.

Conteúdo recomendado:
- ligações principais;
- idioma;
- redes sociais relevantes;
- informação institucional mínima.

## 10. Estados e interações

### Hover

- deve ser subtil;
- não deve ser o único mecanismo de descobrimento;
- útil em desktop, mas não essencial em mobile.

### Focus

- o foco visual deve ser sempre evidente para teclado;
- links, botões e campos devem ter estados claros.

### Feedback visual

- hover, active e focus devem ser consistentes;
- as transições devem ser modestas e rápidas.

## 11. Motion

### Decisão recomendada

O site pode usar microinterações discretas para dar vida, mas sem espetáculo.

### Princípios

- fade sutil;
- transformações pequenas e suaves;
- transições curtas e previsíveis;
- hover mínimo;
- entrada de elementos em desaceleração moderada.

### Evitar

- animações constantes;
- elementos a saltar;
- parallax excessivo;
- efeitos que dificultem leitura;
- efeitos que prejudiquem performance.

### Acessibilidade

- respeitar redução de movimento;
- evitar animações que atrapalhem o uso de teclado ou leitura.

## 12. Imagem e media

### Regra principal

Usar imagens quando acrescentarem valor ao conteúdo, não apenas para preencher espaço.

### Recomendações

- Fotografia deve ter maior presença visual por natureza;
- areas sem imagem podem usar composição textual ou elemento gráfico;
- não presumir que todas as secções necessitam de imagem;
- imagens devem manter espaço visual limpa e não competir com texto.

### Estrutura futura

- suportar fotografias, galerias, vídeo e conteúdo visual sem congelar o sistema;
- permitir crescimento gradual sem exigir abordagem visual totalmente diferente.

## 13. Componentes por página

A estrutura visual será guiada por um padrão consistente de secções, espaçamento e hierarquia, mas sem repetir o mesmo bloco em todos os locais.

Componentes recorrentes:
- header;
- nav;
- hero;
- section heading;
- intro text;
- text + media block;
- cards;
- listagem de projetos;
- lista de áreas;
- footer.

## 14. Regras de manutenção

- centralizar tokens e valores de design;
- manter pouca variedade de cores e tamanhos;
- evitar duplicação de estilos em vários pontos do sistema;
- preservar flexibilidade para novas áreas e traduções;
- manter a transparência para futuras mudanças sem refazer o desenho completo.

## 15. Decisões recomendadas e pendentes

### Decisões recomendadas

- Paleta neutra com accent quente e sofisticado.
- Fundo claro como base visual recomendada.
- Design minimalista, com ênfase em texto, whitespace e composição.
- Menu simples e responsável em mobile.
- ausência de fotografia pessoal como elemento obrigatório na primeira iteração.
- uso discreto de microinterações.

### Decisões pendentes

- paleta final do proprietário;
- tipo de fonte final;
- light/dark mode;
- elemento visual definitivo da Hero;
- tipo exato de fotografia/galeria para a área de criação;
- voce e estrutura final de componentes por conteúdo real.

## 16. Conclusão

Este design system V1 procura criar uma base visual robusta, elegante e sustentável, mantendo o projeto fiel ao conceito de portfólio profissional + hub pessoal. A intenção não é “perfeitamente fechado”, mas extremamente preparado para crescer sem perder identidade, legibilidade ou intenção editorial.
