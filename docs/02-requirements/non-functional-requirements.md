# Requisitos Não Funcionais

Este documento organiza requisitos de qualidade, restrições e princípios técnicos para o portfólio Miguel Cardoso.

## Requisitos aprovados

### RNF-001 — Simplicidade e manutenção

Categoria:
Manutenção.

Descrição:
A solução deve privilegiar simplicidade, código legível, baixo acoplamento e facilidade de manutenção.

Prioridade:
Must Have.

Estado:
Aprovado.

Critérios de aceitação:
Pendentes até existir arquitetura técnica e código avaliável.

### RNF-002 — Direção visual minimalista pessoal/criativa

Categoria:
Usabilidade / Design.

Descrição:
A experiência visual deve ser clean, minimalista, profissional, pessoal, criativa, confortável para os olhos e com excelente legibilidade.

Prioridade:
Must Have.

Estado:
Aprovado.

Critérios de aceitação:
A documentação de design deve refletir a direção “Minimalismo sem ser vazio; criatividade sem ser exagerada.”

### RNF-003 — Evitar excesso visual

Categoria:
Usabilidade.

Descrição:
O site deve evitar excesso de elementos, cores, animações, estética tecnológica exagerada e complexidade visual cansativa.

Prioridade:
Must Have.

Estado:
Aprovado.

Critérios de aceitação:
Pendentes até à fase de UX/UI.

### RNF-004 — Responsividade

Categoria:
Responsividade.

Descrição:
O site deve ser utilizável em desktop e mobile. Funcionalidades não podem depender exclusivamente de hover.

Prioridade:
Must Have.

Estado:
Aprovado.

Critérios de aceitação:
Pendentes até à fase de UX/UI e testes.

### RNF-005 — Acessibilidade

Categoria:
Acessibilidade.

Descrição:
O site deve considerar legibilidade, contraste, navegação por teclado, texto alternativo, semântica HTML, foco visível, leitores de ecrã e movimento reduzido.

Prioridade:
Must Have.

Estado:
Aprovado como princípio; métricas finais pendentes.

Critérios de aceitação:
Pendentes até à definição da estratégia de acessibilidade.

### RNF-006 — Performance

Categoria:
Performance.

Descrição:
O site deve ser rápido e preparado para otimização de imagens, media, CSS, JavaScript e carregamento de fontes.

Prioridade:
Must Have.

Estado:
Aprovado como princípio; métricas finais pendentes.

Critérios de aceitação:
Pendentes até à definição de objetivos mensuráveis.

### RNF-007 — Segurança desde o início

Categoria:
Segurança.

Descrição:
A arquitetura futura deve considerar autenticação administrativa, autorização, proteção contra CSRF, XSS, SQL injection, validação de uploads, proteção de secrets, HTTPS, backups e logs.

Prioridade:
Must Have.

Estado:
Aprovado como princípio; controlos finais pendentes.

Critérios de aceitação:
Pendentes até à fase de segurança e arquitetura técnica.

### RNF-008 — Conteúdo desacoplado da apresentação

Categoria:
Arquitetura / Manutenção.

Descrição:
Conteúdo e apresentação devem estar separados sempre que fizer sentido, para facilitar edição, tradução, expansão e manutenção.

Prioridade:
Should Have.

Estado:
Aprovado como princípio.

Critérios de aceitação:
Pendentes até à definição da arquitetura técnica.

### RNF-009 — Tokens de design para cores

Categoria:
Design / Manutenção.

Descrição:
As cores devem ser centralizadas através de tokens ou variáveis de design, evitando valores dispersos por muitos ficheiros.

Prioridade:
Should Have.

Estado:
Aprovado.

Critérios de aceitação:
Pendentes até existir implementação visual.

### RNF-010 — Independência de plataformas externas

Categoria:
Disponibilidade / Manutenção.

Descrição:
O site pode ligar ao Instagram e outras plataformas, mas não deve depender da API ou disponibilidade do Instagram para funcionar.

Prioridade:
Should Have.

Estado:
Aprovado.

Critérios de aceitação:
Pendentes até à definição da integração externa.

## Decisões pendentes

- Paleta de cores final.
- Light/Dark mode.
- Métricas de performance.
- Nível formal de acessibilidade.
- Estratégia final de SEO.
- Compatibilidade mínima de browsers e dispositivos.
- Estratégia de backups, logs e gestão de secrets.
