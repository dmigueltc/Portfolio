# Responsive Strategy V1

Este documento define a estratégia responsiva para a primeira versão do portfólio Miguel Cardoso. O foco é garantir uma experiência clara, acessível e agradável em mobile, tablet e desktop, sem depender de hover para a navegação ou para elementos essenciais.

## 1. Objetivo

A estratégia responsiva deve garantir que o site funcione bem para:

- mobile;
- tablet;
- laptop;
- desktop;
- múltiplas larguras de ecrã.

O objetivo principal não é “reduzir o desktop para mobile”, mas sim desenhar a experiência para cada contexto.

## 2. Princípios responsivos

- Mobile como prioridade de utilização.
- Conteúdo e navegação devem permanecer claros em qualquer ecrã.
- Hover não pode ser requisito essencial.
- Layouts devem adaptar com recorrência a espaçamento e hierarquia, não apenas a largura.
- As áreas principais devem manter relevância visual em qualquer dispositivo.
- O design deve continuar minimalista em resoluções pequenas.

## 3. Abordagem geral

A abordagem recomendada é mobile-first, com expansão elegante para tablet e desktop.

### Mobile

- menu simples e imediatamente legível;
- blocos de conteúdo empilhados verticalmente;
- texto e botões consoante o tamanho do ecrã;
- imagens com uso criterioso e sem sobrecarregar a interface;
- explorar áreas em sequência clara, sem necessidade de hover.

### Tablet

- organização em colunas suaves;
- manter legibilidade e ritmo visual;
- permitir maior densidade sem perder espaço de respiração.

### Desktop

- layouts mais amplos e com melhor aproveitamento da linha de leitura;
- manter a mesma identidade visual e a mesma hierarquia do mobile;
- não criar excesso de colunas ou blocos densos.

## 4. Breakpoints conceptuais

Não é necessário fixar uma stack técnica nesta fase, mas uma estratégia conceptual útil é:

```text
Mobile: 0–767px
Tablet: 768–1023px
Desktop: 1024px+
```

### Regras

- Estas larguras são orientações de design, não decisões técnicas obrigatórias.
- O sistema deve adaptar-se continuamente, não apenas em saltos rígidos.
- Tipografia, grid e espaçamento devem reagir conforme a largura disponível.

## 5. Navegação responsiva

### Mobile

- menu simples, direto e de fácil descoberta;
- reduzido número de itens visíveis ao mesmo tempo;
- ações principais facilmente acessíveis;
- altura e target de toque adequados.

### Desktop

- navegação mais ampla e mais enxuta;
- manter clareza sem criar excesso de itens.

### Regra

A navegação essencial deve funcionar sem hover, sem depender do mouse, e sem exigir interações ocultas ou ambíguas.

## 6. Grid e estrutura

### Mobile

- 1 coluna predominante;
- secções empilhadas com ritmo visual moderado;
- text blocks e cards não demasiado largos.

### Tablet

- 2 colunas em algumas secções, especialmente em áreas com conteúdo paralelo.

### Desktop

- grid mais amplo para apresentar áreas principais, projetos e galerias quando apropriado;
- manter whitespace e legibilidade.

### Regras

- evitar layouts densos em qualquer resolução;
- os cards e blocos devem respeitar espaço e hierarquia;
- não transformar cada página numa grelha de “cards” sem sentido.

## 7. Tipografia responsiva

### Regras

- títulos devem reduzir gradualmente para mobile;
- body text deve manter legibilidade com 16px ou superior em geral;
- captions e labels devem manter contraste e clareza;
- o texto em EN/FR deve ser testado em termos de comprimento e quebra de linha.

### Prioridade

- legibilidade > estética ornamental;
- design consistente > adaptações extravagantes.

## 8. Espaçamento responsivo

### Regras

- mobile deve ter espaçamento mais compacto mas não apertado;
- desktop pode usar mais espaço para respirar e para reforçar hierarquia;
- as secções devem manter ritmo visual em todas as telas.

### Escala recomendada

- mobile: espaçamentos compactos dentro de uma escala geral;
- desktop: maior proporção de whitespace para destacar grandes blocos de conteúdo.

## 9. Imagem e media responsivas

### Regras

- imagens devem escalar com qualidade sem ocuparem demasiado espaço em mobile;
- evitar media excessivamente pesadas;
- não usar imagens para preencher espaço sem função;
- galerias e blocos visuais devem preservar navegação clara.

### Estratégia recomendada

- fotografia: maior presença visual em ecrãs maiores;
- mobile: priorizar imagens nítidas, sem bloquear o conteúdo textual;
- galerias em mobile devem ser simples e consistentes.

## 10. Componentes e comportamento por dispositivo

### Header

- mobile: menu direto e reduzido;
- desktop: navegação mais completa, mantendo simplicidade.

### Hero

- mobile: texto visível em bloco compacto, elemento visual discreto;
- desktop: maior impacto visual, com melhor equilíbrio de texto e imagem/composição.

### Cards

- mobile: empilhados ou 2 por linha apenas quando fizer sentido;
- desktop: podem expandir para 3 ou mais colunas quando a estrutura o justificar.

### Galerias

- mobile: organização simples e legível;
- desktop: mais flexibilidade, mas mantendo hierarquia.

## 11. Acessibilidade visual responsiva

### Regras

- texto legível em qualquer resolução;
- foco visível em mobile e desktop;
- targets de toque suficientes em mobile;
- contraste preservado em todos os tamanhos;
- layout não deve depender de hover para navegação.

## 12. Idiomas e responsividade

O design deve suportar traduções longas sem quebrar a UX.

### Regras

- botões e navegações devem suportar texto mais longo em EN/FR;
- layouts não devem depender de uma frase curta;
- o menu e os blocos de conteúdo devem permitir expansão sem colapso visual.

## 13. Estados vazios responsivos

Em qualquer resolução, os estados vazios devem ser silenciosos e honestos.

### Exemplos

- sem projetos: bloco simples e limpo;
- sem fotografia disponível: estrutura visual clara, sem texto desconfortável;
- sem contacto final: suporte discreto e sem sensação de incompletude.

## 14. Decisões recomendadas

- mobile-first como base da estratégia;
- hover como enriquecimento, não como requisito;
- menu simples e funcional em mobile;
- postura visual clara em todos os tamanhos;
- espaço respirável em desktop e calm em mobile;
- imagens usadas com intenção, não decorativamente.

## 15. Decisões pendentes

- breakpoints finais dependendo da implementação real;
- revisão exacta de tipografia em mobile vs desktop;
- estratégia visual final da galeria de fotografia;
- soluções de menu e navegação finais dependendo da arquitetura técnica.

## 16. Conclusão

A estratégia responsiva proposta mantém o site simples, elegante e acessível em qualquer dispositivo. A prioridade é garantir que a experiência funciona em mobile como primeira classe, sem comprometer a identidade minimalista e profissional do portfólio, e mantendo flexibilidade para crescer com novos conteúdos e áreas.
