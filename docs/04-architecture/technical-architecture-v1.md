# Arquitetura Técnica V1

Este documento define a arquitetura técnica proposta para o Portfólio Miguel Cardoso, na Fase 4 — Arquitetura Técnica V1.

O objetivo é descrever uma solução clara, simples, segura, sustentável e preparada para crescer. Não é uma especificação de implementação final nem uma decisão técnica fechada para todas as fases futuras, mas sim uma base sólida para a implementação futura.

## 1. Escopo

A arquitetura deve suportar:

- portfólio profissional + hub pessoal;
- presença clara em PT-PT, EN e FR;
- áreas principais em Tecnologia, Fotografia e Fitness;
- possibilidade de expansão para novas áreas;
- navegação simples e conteúdo de fácil manutenção;
- conteúdo textual e visual organizado;
- segurança mínima adequada para um portfólio pessoal/profissional;
- desempenho e manutenção sem sobreengenharia.

## 2. Princípios de arquitetura

Os princípios base desta arquitetura são:

- simplicidade antes de complexidade;
- Python como linguagem backend confirmada;
- PHP excluído;
- arquitetura preparada para crescimento, mas sem sobreengenharia;
- conteúdo separado da apresentação sempre que fizer sentido;
- manutenção simples para diferentes pessoas e agentes AI;
- segurança considerada desde o início;
- performance e responsividade como requisitos de qualidade;
- independência de qualquer ferramenta de IA específica;
- documentação como fonte de verdade.

## 3. Decisão de desenho

### 3.1. Recomendação principal

Para este projeto, a recomendação técnica para a V1 é:

- arquitetura web em Python;
- aplicação monolítica modular, em vez de microserviços;
- frontend server-rendered ou híbrido leve, sem necessidade de SPA complexa;
- gestão de conteúdo simples e previsível;
- separação clara entre conteúdo, domínio, apresentação e integrações externas.

### 3.2. Framework recomendado

Entre as opções avaliadas, a opção mais adequada para este projeto é:

- Django como recomendação principal para a V1.

Motivos:

- forte alinhamento com gestão de conteúdo e manutenção;
- administração integrada e útil para um portfólio que pode crescer;
- templates e estrutura de projeto coerentes para sites pessoais/profissionais;
- boa curva de produtividade para sites com várias páginas e conteúdo editorial;
- bom suporte para multilíngue, segurança e organização do contexto do projeto;
- boa compatibilidade com um workflow de documentação e conteúdo claro.

### 3.3. Alternativas avaliadas

#### Django

Vantagens:
- administração integrada;
- ORM robusto;
- padrões bem definidos;
- boas práticas para aplicações web em Python;
- estreita adequação a portfólios com gestão de conteúdo.

Desvantagens:
- mais estrutura do que um protótipo simples;
- pode ser mais pesado do que um site estático muito pequeno;
- exige disciplina em organização para manter a simplicidade.

Conclusão:
- excelente fit para um portfólio profissional + hub pessoal com crescimento futuro.

#### FastAPI

Vantagens:
- excelente para APIs e serviços bem estruturados;
- desempenho muito bom;
- excelente para aplicações com lógica de domínio complexa.

Desvantagens:
- menos natural para conteúdo editorial e gestão de CMS sem extra configuração;
- exige mais decisões de organização para frontend e templates;
- o projecto não exige uma API complexa como requisito principal nesta fase.

Conclusão:
- relevante em cenários de APIs robustas, mas não como escolha principal para a V1 do portfólio atual.

#### Flask

Vantagens:
- minimalista;
- simples de aprender;
- ótimo para prototipagem e projetos pequenos.

Desvantagens:
- exige mais decisões de arquitetura manualmente;
- menos adequado para conteúdo complexo, gestão de páginas e internacionalização sem esforço extra;
- menos robusto para manutenção em crescimento sem organização forte.

Conclusão:
- útil como base educativa ou protótipo, mas menos adequada como solução principal deste projeto.

### 3.4. Decisão formal recomendada

A arquitetura V1 deve considerar Django como a opção principal para implementação web em Python, com a seguinte posição:

- escolha recomendada para a arquitetura técnica V1;
- mantida como opção principal de implementação futura;
- não deve ser tratada como uma decisão “impossível de mudar”, mas como a melhor aposta neste contexto atual.

Se a etapa técnica posterior provar que um modelo de API-first ou um stack mais leve é necessário, essa decisão pode ser revista com documentação explícita.

## 4. Arquitetura proposta

### 4.1. Visão geral

A arquitetura ideal para o projeto é uma aplicação web Python organizada por camadas, em vez de um conjunto de serviços distribuídos.

Estrutura conceptual:

- Camada de apresentação: páginas e templates do site
- Camada de conteúdo: textos, páginas, áreas, projetos, media
- Camada de domínio: regras de negócio ligadas ao conteúdo e ao portfólio
- Camada de infraestrutura: armazenamento, media, integrações externas, deployments
- Camada de segurança: autenticação futura, secrets, validação e HTTP security

### 4.2. Padrão recomendado

Padrão recomendado: aplicação monolítica modular.

Motivos:

- o projeto é um portfólio pessoal, não uma plataforma complexa;
- reduz custo de manutenção;
- facilita documentação, revisão e implementação por múltiplas IAs ou programadores;
- o conteúdo tem variedade e volume moderado, mas não exige microserviços;
- reduz necessidade de infraestruturas complexas e de deploying múltiplo.

## 5. Camadas da solução

### 5.1. Camada de apresentação

Responsável por:

- páginas públicas;
- navegação principal;
- home;
- páginas de área;
- páginas de detalhe de projetos;
- contacto;
- traduções.

Objetivo:

- manter UX consistente com a documentação de design;
- deixar a experiência visual clara e simples;
- garantir que a navegação e layout sejam adaptados ao conteúdo real.

### 5.2. Camada de conteúdo

Responsável por:

- textos e informações editoriais;
- descrição das áreas;
- detalhes dos projetos;
- links, media e metas de redes sociais;
- textos em PT-PT/EN/FR.

Objetivo:

- separar conteúdo de layout;
- facilitar manutenção ao longo do tempo;
- tornar possível a expansão para novas áreas sem duplicação absurda.

### 5.3. Camada de domínio

Responsável por:

- regras ligadas a temas do portfólio;
- gestão de áreas;
- gestão de projetos;
- gestão de conteúdos multimédia;
- regras de publicação e destaque.

Objetivo:

- manter lógica de negócio simples e previsível;
- evitar espalhar regras por templates ou views.

### 5.4. Camada de infraestrutura

Responsável por:

- gestão de media;
- gestão de secrets;
- envio de email futuro;
- analytics futuro;
- logs e observabilidade;
- backups e storage de dados;
- ambiente de produção.

Objetivo:

- garantir que a aplicação central permanece limpa;
- separar a lógica de negócio da infraestrutura externa.

## 6. Estrutura lógica recomendada

A estrutura lógica abaixo é conceptual e não determina a organização exata de ficheiros em código, mas define a divisão funcional esperada:

```text
app/
├── core/
│   ├── config/
│   ├── settings/
│   ├── urls/
│   └── middleware/
├── content/
│   ├── models/
│   ├── services/
│   ├── translations/
│   └── media/
├── pages/
│   ├── views/
│   ├── templates/
│   └── routes/
├── areas/
│   ├── technology/
│   ├── photography/
│   ├── fitness/
│   └── future-areas/
├── projects/
│   ├── models/
│   ├── filters/
│   └── detail-pages/
├── i18n/
│   ├── locale/
│   ├── translations/
│   └── language-switch/
├── security/
│   ├── validation/
│   ├── secrets/
│   └── headers/
├── static/
│   ├── css/
│   ├── js/
│   └── assets/
└── utils/
    ├── seo/
    ├── logging/
    └── helpers/
```

## 7. Gestão de conteúdo

### 7.1. Objetivo

A gestão de conteúdo deve ser simples, clara e fácil de manter, sem espalhar texto e dados pelo código.

### 7.2. Recomendação

- usar uma abordagem orientada a modelos para áreas, páginas, projetos, media e traduções;
- manter conteúdo estruturado e separável da apresentação;
- evitar duplicação excessiva de textos e campos;
- gerir media em diretórios organizados e por tipo.

### 7.3. Conteúdo principal

O sistema deve ser capaz de gerir:

- textos principais;
- páginas e secções;
- áreas do portfólio;
- projetos;
- fotografia e galerias;
- links externos;
- dados de contacto;
- linguagem e traduções.

## 8. Internacionalização

### 8.1. Requisito

O site suporta PT-PT, EN e FR.

### 8.2. Estratégia recomendada

- usar um sistema de tradução por locale;
- manter o idioma principal em PT-PT;
- separar o conteúdo traduzível do layout;
- usar routes ou estrutura de locale controlada de acordo com a decisão de UX e arquitetura final.

### 8.3. Regras

- textos não devem estar “hardcoded” em várias partes do sistema;
- a estrutura deve permitir adicionar novos idiomas sem reescrever o sistema inteiro;
- tradução deve ser fácil de manter por pessoas e agentes.

## 9. Segurança e privacidade

### 9.1. Fundamentos

A arquitetura deve considerar desde o início:

- validação de entrada;
- proteção contra XSS/CSRF;
- proteção contra SQL injection;
- gestão segura de secrets;
- HTTPS em produção;
- menor privilégio em acessos e admin;
- ausência de credenciais no Git;
- logs sem exposição de dados sensíveis.

### 9.2. Recomendação material

- usar um padrão de configuração via variáveis de ambiente;
- separar ambiente de desenvolvimento e produção;
- manter admin e funcionalidades sensíveis isoladas por autenticação futura;
- tratar uso de terceiros e media externa com cuidado.

## 10. Dados e persistência

### 10.1. Decisão atual

Ainda não existe decisão final de base de dados, mas a arquitetura deve preparar uma solução simples e robusta.

### 10.2. Direção recomendada

- base de dados relacional, por ser natural para conteúdo estruturado e gestão de projetos;
- suporte simples para paginação, relações e queries;
- compatibilidade com Django ORM em caso de adoção do Django.

### 10.3. Modelo de dados conceptual

Os principais modelos conceptuais previstos são:

- Área;
- Página;
- Project;
- Media; 
- Translation;
- ContactLink;
- SocialLink;
- Config;
- User (futuro, quando existir autenticação).

## 11. SEO e partilha social

A arquitetura deve permitir:

- metadados de páginas;
- títulos e descrições;
- Open Graph;
- URLs legíveis;
- sitemap;
- robots.txt;
- suporte a multilíngue;
- estrutura facilmente indexável por motores de busca.

A arquitetura não deve sacrificar performance ou clean design para satisfazer SEO; o SEO deve ser integrado ao conteúdo e à estrutura da aplicação.

## 12. Performance

### 12.1. Objetivos gerais

- carregamento simples e rápido;
- minimização de JS desnecessário;
- otimização de imagens e media;
- lazy loading quando apropriado;
- layout claro, sem dependências pesadas;
- boa experiência em mobile e em redes menos potentes.

### 12.2. Estratégia

- priorizar páginas simples e bem estruturadas;
- manter asset management previsível;
- otimizar media com qualidade e tamanho adequados;
- evitar adicionar soluções pesadas para um portfólio que ainda é pequeno.

## 13. Responsividade e UX

A arquitetura deve apoiar o design definido em UX V1:

- layout com foco em mobile-first;
- menu simples e legível em qualquer dispositivo;
- sem reliance em hover para funcionalidade essencial;
- páginas e blocos modulares;
- suporte fácil a nova informação sem quebrar layout.

## 14. Deployment e infraestruturas

### 14.1. Decisão atual

Hosting, deployment e infraestruturas não devem ser escolhidas nesta fase de documentação.

### 14.2. Recomendação de arquitetura de deployment

A arquitetura deve ser compatível com uma implementação de produção simples, por exemplo:

- aplicação Python em um ambiente de hosting previsível;
- assets estáticos servidos de forma simples;
- gestão de secret variables e logs;
- ambiente de staging e production claramente separado.

Não se deve assumir um host específico, um CDN obrigatório, ou um deployment complexo, pois isso é decisão futura.

## 15. Escalabilidade

### 15.1. Requisito

O projeto deve crescer sem exigir reescrita completa da base.

### 15.2. Como a arquitetura sustenta isso

- modularização funcional;
- separação de conteúdo e template;
- possibilidade de adicionar novas áreas sem desestruturar a aplicação;
- estrutura adequada para projetos, media, traduções e páginas futuras;
- facilidade para ampliar a base sem criar overhead de microserviços.

## 16. Sustentabilidade da arquitetura

A arquitetura proposta evita:

- microserviços sem necessidade;
- dependências excessivas;
- complexidade desnecessária;
- frameworks escolhidos apenas por tendência;
- soluções demasiado pesadas para um portfólio pessoal/profissional.

Princípio:

> complexidade apenas quando existir necessidade real.

## 17. Riscos e pontos de atenção

### 17.1. Riscos principais

- excesso de documentação sem implementação;
- proporções de arquitetura maiores do que o projeto necessita;
- tentar inverter o problema: “criar um CMS grande para um portfólio pequeno”;
- decidir uma base de dados sem necessidade imediata;
- criar uma arquitetura programática demasiado genérica sem conteúdo real.

### 17.2. Mitigação

- manter a arquitetura simples;
- manter ajustes de conteúdo e UX em foco;
- tratar cada camada como funcional e necessária;
- evitar etapas de infraestrutura que não sejam justificadas por necessidade real.

## 18. Decisão recomendada final

A solução recomendada para a V1 é:

- Python como linguagem backend;
- Django como framework principal recomendado;
- arquitetura monolítica modular;
- server-rendered pages com conteúdo organizado;
- gestão de conteúdo em modelos e templates;
- tradução multilíngue clara;
- foco em manutenção, clareza e performance;
- preparação para futuras áreas e projetos sem reestruturação completa.

Esta recomendação deve ser entendida como uma proposta de arquitetura técnica V1, útil para a fase de implementação, mas sujeita à validação final da arquitetura técnica e à decisão do proprietário do projeto.

## 19. Decisões que continuam pendentes

Estas decisões continuam fora do escopo formal da arquitetura V1:

- framework técnico final (ainda no caminho de confirmação, embora Django seja a recomendação);
- base de dados final;
- sistema de gestão de conteúdo final;
- hosting e deployment;
- autenticação futura;
- APIs e integrações externas;
- stack frontend final;
- estratégia de cache final;
- arquitetura de media final.

## 20. Validação

Este documento é coerente com:

- functional requirements V1;
- non-functional requirements V1;
- sitemap V1;
- information architecture;
- design system V1;
- context e identidade do projeto;
- decisões de Python e exclusão de PHP.

Também respeita o princípio de não criar complexidade desnecessária e mantém a portabilidade para futuras implementações e agentes de IA.

## 21. Conclusão

A arquitetura técnica V1 recomendada para o Portfólio Miguel Cardoso deve ser simples, segura, clara e extensível. A decisão mais localizada para o projeto atual é usar Python com uma aplicação web monolítica modular, com Django como recomendação principal, em vez de criar serviços distribuídos ou uma plataforma de conteúdo demasiadamente complexa.

Este desenho dá equilíbrio entre facilidade de manutenção, gestão de conteúdo, segurança, escalabilidade incremental e adaptação ao design proposto, sem comprometer a capacidade de crescer quando houver conteúdo real e decisões formais de implementação.
