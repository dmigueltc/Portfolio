# Sitemap Oficial V1

Este documento define a primeira versão oficial do sitemap conceptual do portfólio Miguel Cardoso.

Não define rotas técnicas finais, templates, modelos, componentes, base de dados ou implementação. O objetivo é orientar a estrutura de páginas, navegação e conteúdo previsto para a futura fase de UX/UI e arquitetura técnica.

## Estado do documento

- Versão: V1.
- Fase do projeto: FASE 1 — Levantamento e Planeamento.
- Estado: Documentação aprovada como base de planeamento, sujeita a revisão antes da implementação.
- Implementação: não iniciada.

## Princípios usados

- O site é um portfólio profissional + hub pessoal.
- O público principal inicial vem sobretudo do Instagram e pode não ter conhecimentos técnicos.
- O público secundário inclui recrutadores, empresas, programadores, profissionais de tecnologia, potenciais clientes, colaboradores e parceiros.
- A navegação deve permitir profundidade progressiva.
- Tecnologia e Fotografia têm maior peso inicial que Fitness.
- Fitness é uma área pessoal/hobby e deve ter presença proporcional.
- O site não deve depender do Instagram para funcionar.
- Não criar páginas vazias apenas por antecipação.
- Não inventar projetos, serviços, biografia, contactos ou conteúdo visual inexistente.

## Legenda de estado

- V1: previsto para a primeira versão do site, dependendo da validação final de conteúdo e UX/UI.
- Futuro: preparado conceptualmente, mas não deve ser implementado na primeira versão sem nova decisão.
- Não decidido: ainda precisa de decisão explícita antes de ser tratado como requisito.

## Sitemap V1 proposto

```text
/
├── Home
├── Sobre
├── Tecnologia
├── Fotografia
├── Fitness
├── Projetos
└── Contacto
```

A estrutura acima é conceptual. URLs finais, slugs por idioma e organização técnica serão definidos numa fase posterior.

## Páginas principais — V1

### 1. Home

Estado:
V1.

Objetivo:
Apresentar Miguel Cardoso de forma imediata, simples, pessoal e profissional, funcionando como ponto de entrada para visitantes comuns e visitantes profissionais.

Conteúdo previsto:

- Hero com nome “Miguel Cardoso”.
- Frase/posicionamento curto.
- Referência às áreas Tecnologia, Fotografia e Fitness.
- Secção Explora com cartões para áreas principais.
- Apresentação curta “Sobre mim”.
- Área para projetos em destaque, quando existirem projetos reais.
- Área visual de fotografia/criação, sem conteúdo fictício.
- Contacto e ligações relevantes.
- Footer.

Observações:

- A Home é obrigatória na V1.
- O elemento visual da Hero ainda não está decidido.
- Projetos em destaque só devem aparecer com conteúdo real ou com uma solução editorial aprovada que não simule projetos inexistentes.

### 2. Sobre

Estado:
V1, pendente de conteúdo final.

Objetivo:
Explicar quem é o Miguel de forma mais completa que a apresentação curta da Home.

Conteúdo previsto:

- Apresentação pessoal/profissional.
- Formação em Engenharia Informática.
- Interesses principais.
- Relação entre desenvolvimento, tecnologia e criação de conteúdo.
- Ligação para áreas relevantes do site.

Observações:

- Não deve ser uma autobiografia longa.
- Não utilizar fotografia pessoal inicialmente.
- Deve ser compreensível para público não técnico.

### 3. Tecnologia

Estado:
V1.

Objetivo:
Apresentar a área de tecnologia como uma das áreas principais do portfólio.

Conteúdo previsto:

- Desenvolvimento e programação.
- Desenvolvimento web.
- Tecnologia.
- Hardware e computadores.
- Otimização e troubleshooting de PC.
- Ligações para projetos ou conteúdos relacionados, quando existirem.

Observações:

- Esta área tem maior peso inicial.
- O detalhe técnico deve ser progressivo para não afastar visitantes comuns.
- Conteúdo definitivo ainda está pendente.

### 4. Fotografia

Estado:
V1.

Objetivo:
Dar presença real à fotografia, edição de fotografia, vídeo e criação de conteúdo.

Conteúdo previsto:

- Fotografia.
- Edição de fotografia.
- Criação visual.
- Possível ligação a vídeo ou criação de conteúdo digital.
- Espaço para imagens reais, álbuns, séries ou projetos fotográficos quando existirem.

Observações:

- Esta área tem maior peso inicial.
- Não criar galeria fictícia para preencher espaço.
- Estrutura final de galeria, álbuns, imagens individuais e metadados ainda não está decidida.

### 5. Fitness

Estado:
V1, com presença proporcional.

Objetivo:
Representar Fitness como interesse pessoal/hobby, sem competir com o peso de Tecnologia e Fotografia.

Conteúdo previsto:

- Breve enquadramento do interesse.
- Possível ligação a evolução pessoal ou conteúdos futuros, se aprovados.

Observações:

- Deve ser simples e discreto na V1.
- Não criar rotina, planos, métricas ou conteúdo detalhado sem decisão futura.

### 6. Projetos

Estado:
V1 como estrutura preparada; conteúdo real pendente.

Objetivo:
Preparar a apresentação de projetos reais, técnicos, criativos ou pessoais.

Conteúdo previsto:

- Lista de projetos reais quando existirem.
- Detalhe de projeto, se aprovado na arquitetura futura.
- Categoria ou área associada.
- Estado do projeto.
- Tecnologias, imagens, links ou GitHub quando aplicável.

Observações:

- Ainda não existem projetos pessoais finais definidos.
- Não criar projetos fictícios.
- A gestão de adicionar, editar, remover, destacar e ocultar projetos está aprovada como necessidade futura, mas a implementação está pendente.

### 7. Contacto

Estado:
V1.

Objetivo:
Permitir ligação com Miguel Cardoso e orientar visitantes para canais externos relevantes.

Conteúdo previsto:

- Contacto direto, se aprovado.
- GitHub, se aplicável.
- LinkedIn, se aplicável.
- Instagram com importância especial.
- Outras plataformas relevantes, se aprovadas.

Observações:

- Não inventar contactos reais.
- Formulário de contacto ainda não está decidido.
- Proteção contra spam ainda não está decidida.
- O site não deve depender da API ou disponibilidade do Instagram.

## Páginas secundárias — V1

### Página de detalhe de projeto

Estado:
Não decidido para V1.

Objetivo possível:
Apresentar detalhes de um projeto individual.

Conteúdo possível:

- Título.
- Descrição.
- Área/categoria.
- Tecnologias.
- Imagens ou vídeo.
- Links externos.
- GitHub.
- Estado.
- Data.
- Idiomas.

Observações:
A decisão depende da existência de projetos reais e da arquitetura de conteúdo.

### Página de detalhe de fotografia ou álbum

Estado:
Não decidido para V1.

Objetivo possível:
Apresentar fotografias, álbuns ou séries com maior detalhe.

Conteúdo possível:

- Imagens reais.
- Descrição.
- Categoria.
- Data.
- Equipamento.
- Localização, se aplicável.
- Tags, se aprovadas.

Observações:
A estrutura final de fotografia ainda não está definida.

## Navegação principal — V1

A navegação principal deverá privilegiar clareza para visitantes comuns e acesso rápido às áreas principais.

Estrutura proposta:

```text
Home
Explora
Sobre
Projetos
Contacto
```

Comportamento conceptual:

- `Home` leva ao início.
- `Explora` pode levar à secção da Home ou agrupar Tecnologia, Fotografia e Fitness.
- `Sobre` leva à página ou secção sobre Miguel.
- `Projetos` leva à área de projetos, mesmo que inicialmente funcione como estrutura preparada.
- `Contacto` leva à página ou secção de contacto.

Não decidido:

- Se Tecnologia, Fotografia e Fitness aparecem diretamente na navegação principal ou dentro de Explora.
- Se Home será página única, várias páginas ou abordagem híbrida.
- URLs finais e slugs multilingues.

## Navegação complementar — V1

A navegação complementar pode incluir:

- seleção de idioma;
- ligações para redes sociais;
- GitHub;
- LinkedIn;
- Instagram;
- links no footer.

Estado:
Parcialmente V1, com canais finais pendentes.

## Navegação futura

Áreas ou páginas futuras que não devem ser criadas vazias na V1:

- Serviços.
- Gaming.
- Viagens.
- Blog/artigos.
- Timeline/evolução.
- Página avançada de media/vídeo.
- Pesquisa.
- Filtros avançados.
- Newsletter.
- Área pública com autenticação.
- API pública.
- PWA.
- Funcionalidades avançadas ligadas ao Instagram.

## Áreas obrigatórias — V1

- Identidade Miguel Cardoso.
- Posicionamento pessoal/profissional.
- Home com estrutura conceptual aprovada.
- Tecnologia.
- Fotografia/criação.
- Fitness com peso proporcional.
- Contacto ou ligações externas relevantes.
- Suporte conceptual a PT-PT, EN e FR.
- Direção visual minimalista pessoal/criativa.

## Áreas opcionais — V1

- Página Sobre completa, se o conteúdo for validado.
- Página Projetos com estrutura preparada, mesmo que sem destaques reais.
- Página dedicada a cada área, se a decisão de navegação favorecer várias páginas.
- Links externos adicionais além de Instagram, GitHub e LinkedIn.
- Elementos visuais alternativos à fotografia pessoal.

## Áreas futuras

- Serviços profissionais.
- Novas áreas pessoais ou criativas.
- Gaming.
- Viagens.
- Blog ou artigos.
- Timeline/evolução.
- Galeria avançada.
- Vídeo avançado.
- Integração avançada com redes sociais.

## Não decidido

- Paleta de cores final.
- Light/Dark mode.
- Stack técnica final detalhada.
- Base de dados final.
- Sistema final de gestão de conteúdo.
- Conteúdo definitivo das páginas.
- Elemento visual definitivo da Hero.
- Projetos reais.
- Fotografia pessoal.
- Logótipo.
- Formulário de contacto.
- Proteção contra spam.
- URLs finais por idioma.
- Sitemap técnico final.
- Se a navegação final será single-page, multi-page ou híbrida.

## Considerações multilingues

O sitemap deve ser preparado para:

- Português de Portugal como idioma principal.
- Inglês como idioma adicional.
- Francês como idioma adicional.

Não decidido:

- Estrutura final dos URLs por idioma.
- Comportamento quando uma tradução não existir.
- Conteúdos traduzíveis finais.

## Observação final

Este sitemap V1 é uma base oficial de planeamento. Deve ser revisto antes da fase de UX/UI e novamente antes da arquitetura técnica, para evitar transformar decisões ainda pendentes em implementação prematura.
