# Levantamento de Requisitos

Este é o documento principal da FASE 01 — Levantamento de Requisitos.

O objetivo é recolher respostas e decisões do proprietário do projeto antes de transformar qualquer possibilidade em requisito aprovado. Todas as decisões começam como pendentes.
## Atualização pelo planeamento mestre

Algumas questões deste documento já receberam decisões no planeamento mestre do projeto. As decisões consolidadas devem ser consultadas em:

- `docs/02-requirements/functional-requirements.md`
- `docs/02-requirements/non-functional-requirements.md`
- `docs/02-requirements/requirements-matrix.md`
- `docs/04-architecture/information-architecture.md`
- `docs/04-architecture/decisions/decision-log.md`

Questões ainda sem decisão explícita continuam pendentes. Não transformar possibilidades em requisitos obrigatórios sem validação.

## Como preencher

- Responder à pergunta no campo `Decisão`.
- Manter `Estado: Pendente` até existir uma decisão explícita.
- Não transformar sugestões em requisitos sem validação.
- Quando uma decisão for aprovada, refletir o resultado nos documentos de requisitos adequados.

## 1. Identidade

```text
ID:
DISC-001

Pergunta:
Quem é o proprietário do portfólio e que nome deve ser apresentado publicamente?

Contexto:
O website será uma presença digital profissional, mas ainda não existem dados pessoais aprovados para publicação.

Opções, quando aplicável:
Nome completo / Nome profissional / Marca pessoal / A definir.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-002

Pergunta:
Qual deve ser a primeira impressão transmitida ao visitante?

Contexto:
O projeto pretende ser minimalista, profissional, moderno e confortável para os olhos.

Opções, quando aplicável:
Programador / Profissional de tecnologia / Criador visual / Perfil multidisciplinar / A definir.

Decisão:

Estado:
Pendente
```

## 2. Público

```text
ID:
DISC-003

Pergunta:
Quem será o público prioritário do portfólio?

Contexto:
Possíveis visitantes incluem recrutadores, empresas, clientes, programadores, profissionais de tecnologia, pessoas interessadas em fotografia e visitantes gerais.

Opções, quando aplicável:
Recrutadores / Empresas / Clientes / Programadores / Profissionais de tecnologia / Fotografia / Visitantes gerais.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-004

Pergunta:
Existem públicos secundários que também devem orientar conteúdo, navegação ou tom de comunicação?

Contexto:
O website poderá representar diferentes áreas de interesse e trabalho.

Opções, quando aplicável:
Listar públicos secundários e respetiva importância.

Decisão:

Estado:
Pendente
```

## 3. Conteúdo

```text
ID:
DISC-005

Pergunta:
Que tipos de conteúdo devem existir na primeira versão?

Contexto:
O proprietário ainda não possui um projeto pessoal final para destacar como projeto principal.

Opções, quando aplicável:
Texto institucional / Projetos / Galeria / Vídeo / Skills / Experiência / Contacto / A definir.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-006

Pergunta:
Que conteúdo deve ser evitado até existir validação real?

Contexto:
O projeto não deve criar conteúdo fictício, biografias inventadas ou projetos inexistentes.

Opções, quando aplicável:
Projetos fictícios / Testemunhos / Métricas / Clientes / Experiência não validada / Outros.

Decisão:

Estado:
Pendente
```

## 4. Navegação

```text
ID:
DISC-007

Pergunta:
Quais páginas ou secções devem existir na primeira versão?

Contexto:
Possibilidades incluem Home, Sobre mim, Skills, Projetos, Experiência, Fotografia, Vídeo, Tecnologia, PC/Hardware, Fitness e Contacto.

Opções, quando aplicável:
Classificar cada área como confirmado, provável, em discussão ou futuro.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-008

Pergunta:
O website deve ser organizado como página única, várias páginas ou abordagem híbrida?

Contexto:
A decisão influencia navegação, SEO, manutenção e arquitetura, mas ainda não deve ser definida tecnicamente.

Opções, quando aplicável:
Página única / Várias páginas / Híbrido / A definir.

Decisão:

Estado:
Pendente
```

## 5. Projetos

```text
ID:
DISC-009

Pergunta:
Como deve ser apresentado um projeto?

Contexto:
Campos possíveis incluem título, descrição, tecnologias, imagens, vídeo, links, GitHub, estado, data, categoria, destaque, idiomas e visibilidade.

Opções, quando aplicável:
Selecionar campos obrigatórios, opcionais e futuros.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-010

Pergunta:
Como o proprietário deverá adicionar, editar, remover, publicar e despublicar projetos?

Contexto:
O sistema deverá permitir adicionar projetos futuramente sem alterar a estrutura principal da aplicação.

Opções, quando aplicável:
Django Admin / Painel próprio / Processo documentado / A definir na arquitetura.

Decisão:

Estado:
Pendente
```

## 6. Fotografia

```text
ID:
DISC-011

Pergunta:
A fotografia deve ter uma área própria no website?

Contexto:
Fotografia, edição de imagem e vídeo têm importância real no projeto e não devem ser tratados apenas como conteúdo secundário.

Opções, quando aplicável:
Área própria / Integrada em projetos / Futuro / A definir.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-012

Pergunta:
Como deve ser organizada a fotografia?

Contexto:
Possibilidades incluem galeria, categorias, projetos fotográficos, álbuns, fotografias individuais, equipamento, data, localização, tags e destaque.

Opções, quando aplicável:
Galeria / Álbuns / Projetos fotográficos / Categorias / A definir.

Decisão:

Estado:
Pendente
```

## 7. Vídeo

```text
ID:
DISC-013

Pergunta:
O website deve apresentar vídeos próprios, vídeos incorporados ou ambos?

Contexto:
O projeto poderá incluir edição de vídeo e criação de conteúdo digital.

Opções, quando aplicável:
Vídeos próprios / Vídeos incorporados / Ambos / Futuro / A definir.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-014

Pergunta:
Que informação deve acompanhar cada vídeo?

Contexto:
Possibilidades incluem thumbnail, descrição, categoria, projeto relacionado e plataforma externa.

Opções, quando aplicável:
Selecionar campos obrigatórios, opcionais e futuros.

Decisão:

Estado:
Pendente
```

## 8. Skills

```text
ID:
DISC-015

Pergunta:
Que categorias de skills devem existir?

Contexto:
As áreas em análise incluem programação, tecnologia, hardware, fotografia, edição, vídeo, conteúdo digital e fitness.

Opções, quando aplicável:
Técnicas / Criativas / Hardware / Ferramentas / Soft skills / A definir.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-016

Pergunta:
As skills devem ter níveis, descrições ou apenas listagem?

Contexto:
A forma de apresentação deve evitar exagero e manter credibilidade.

Opções, quando aplicável:
Lista simples / Categorias / Níveis / Descrições / A definir.

Decisão:

Estado:
Pendente
```

## 9. Experiência

```text
ID:
DISC-017

Pergunta:
O website deve incluir experiência profissional, académica, pessoal ou combinação destas?

Contexto:
A informação ainda precisa de validação e não deve ser inventada.

Opções, quando aplicável:
Profissional / Académica / Pessoal / Projetos / Futuro / A definir.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-018

Pergunta:
Como devem ser tratadas áreas futuras ou ainda sem trabalhos publicados?

Contexto:
O sistema deve permitir evolução sem apresentar conteúdo fictício.

Opções, quando aplicável:
Ocultar até existir conteúdo / Mostrar como área futura / Página em preparação / A definir.

Decisão:

Estado:
Pendente
```

## 10. Contacto

```text
ID:
DISC-019

Pergunta:
Que formas de contacto devem estar disponíveis?

Contexto:
Possibilidades incluem formulário, email, redes profissionais, GitHub, LinkedIn e outras plataformas. Não inventar contactos reais.

Opções, quando aplicável:
Formulário / Email / GitHub / LinkedIn / Outras plataformas / A definir.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-020

Pergunta:
Que proteção contra spam será necessária?

Contexto:
A decisão influencia segurança, usabilidade e dependências externas.

Opções, quando aplicável:
Validação simples / CAPTCHA / Honeypot / Moderação manual / A definir.

Decisão:

Estado:
Pendente
```

## 11. Administração

```text
ID:
DISC-021

Pergunta:
Que conteúdos o proprietário deve conseguir gerir sem editar código?

Contexto:
O objetivo inclui adicionar, editar, remover, publicar e despublicar conteúdo, imagens, projetos, traduções, categorias e informações pessoais.

Opções, quando aplicável:
Projetos / Fotografias / Vídeos / Skills / Textos / Traduções / Categorias / Dados pessoais.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-022

Pergunta:
O Django Admin deve ser suficiente para a primeira versão ou será necessário outro painel?

Contexto:
O Django Admin deve ser considerado, mas a decisão final pertence à fase de arquitetura.

Opções, quando aplicável:
Django Admin / Painel personalizado / Híbrido / Decidir na arquitetura.

Decisão:

Estado:
Pendente
```

## 12. Multilingue

```text
ID:
DISC-023

Pergunta:
Que conteúdos devem ser traduzíveis?

Contexto:
O website deve suportar PT-PT, EN e FR, mas a implementação técnica ainda não deve ser definida.

Opções, quando aplicável:
Páginas / Projetos / Fotografias / Vídeos / Skills / SEO / Interface / A definir.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-024

Pergunta:
O que deve acontecer quando uma tradução não existir?

Contexto:
Esta decisão afeta experiência do utilizador, SEO e manutenção.

Opções, quando aplicável:
Mostrar PT-PT / Ocultar conteúdo / Mostrar aviso / A definir.

Decisão:

Estado:
Pendente
```

## 13. SEO

```text
ID:
DISC-025

Pergunta:
Que requisitos de SEO devem ser considerados para a primeira versão?

Contexto:
Possibilidades incluem títulos, descriptions, URLs, sitemap, robots.txt, Open Graph, dados estruturados e SEO multilingue.

Opções, quando aplicável:
Classificar como Must Have, Should Have, Could Have ou Won't Have — V1.

Decisão:

Estado:
Pendente
```

## 14. Acessibilidade

```text
ID:
DISC-026

Pergunta:
Que nível de acessibilidade deve orientar a primeira versão?

Contexto:
O website deve considerar contraste, navegação por teclado, alt text, semântica HTML, leitores de ecrã, foco, tamanho de texto e movimento.

Opções, quando aplicável:
Boas práticas essenciais / WCAG como referência / A definir.

Decisão:

Estado:
Pendente
```

## 15. Performance

```text
ID:
DISC-027

Pergunta:
Que objetivos de performance devem ser definidos?

Contexto:
O website deve ser rápido e poderá ter imagens e vídeos, exigindo otimização.

Opções, quando aplicável:
Core Web Vitals / Tempo de carregamento alvo / Orçamento de JavaScript / A definir.

Decisão:

Estado:
Pendente
```

## 16. Segurança

```text
ID:
DISC-028

Pergunta:
Que requisitos de segurança administrativa são obrigatórios?

Contexto:
Possibilidades incluem autenticação administrativa, autorização, passwords, sessões, CSRF, XSS, SQL injection e HTTPS.

Opções, quando aplicável:
Classificar por prioridade e fase.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-029

Pergunta:
Que regras devem existir para uploads de imagens, vídeos ou ficheiros?

Contexto:
Uploads podem introduzir riscos de segurança, validação, armazenamento e performance.

Opções, quando aplicável:
Tipos permitidos / Tamanho máximo / Validação / Antivírus / Armazenamento / A definir.

Decisão:

Estado:
Pendente
```

## 17. Manutenção

```text
ID:
DISC-030

Pergunta:
Que tarefas de manutenção devem ser documentadas para alguém que não desenvolveu o sistema?

Contexto:
A documentação de manutenção é considerada requisito do projeto.

Opções, quando aplicável:
Adicionar projetos / Editar projetos / Apagar projetos / Gerir fotografias / Gerir vídeos / Alterar skills / Alterar conteúdo / Adicionar traduções.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-031

Pergunta:
Com que frequência se espera atualizar o conteúdo?

Contexto:
A frequência influencia administração, manutenção e eventual necessidade de automação.

Opções, quando aplicável:
Raramente / Mensalmente / Semanalmente / Conforme necessário / A definir.

Decisão:

Estado:
Pendente
```

## 18. Funcionalidades futuras

```text
ID:
DISC-032

Pergunta:
Que funcionalidades devem ser explicitamente consideradas como futuras ou fora da V1?

Contexto:
Funcionalidades como pesquisa, filtros, blog, comentários, autenticação pública, analytics, newsletter, CMS personalizado, API pública, PWA, dark mode, animações, tags, favoritos, rede social ou IA não estão aprovadas.

Opções, quando aplicável:
Classificar cada possibilidade como em discussão, futuro, rejeitado ou Won't Have — V1.

Decisão:

Estado:
Pendente
```

```text
ID:
DISC-033

Pergunta:
Existem funcionalidades que não devem ser consideradas em nenhuma fase?

Contexto:
Definir limites ajuda a evitar complexidade técnica desnecessária.

Opções, quando aplicável:
Listar funcionalidades excluídas e motivo.

Decisão:

Estado:
Pendente
```

