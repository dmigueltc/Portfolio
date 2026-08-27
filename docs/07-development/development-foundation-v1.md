# Development Foundation V1

## 1. Objetivo

Este documento especifica a base técnica que deverá ser preparada antes da
implementação das páginas e do design final do Portfólio Miguel Cardoso.

É uma especificação para a futura implementação, não uma implementação. Deve
ser suficientemente clara para ser executada por Claude Code, Codex, GitHub
Copilot, Gemini ou outro agente, sem depender do histórico desta conversa.

As categorias usadas neste documento são:

- **Requisito**: comportamento ou propriedade que a solução deve suportar.
- **Solução recomendada**: abordagem preferida para a V1, ainda sujeita a
  validação durante a implementação.
- **Decisão aprovada**: decisão já registada como aprovada na documentação do
  projeto.
- **Decisão pendente**: assunto que não deve ser fechado ou implementado sem
  aprovação explícita.

## 2. Scope

A Foundation V1 cobre a preparação conceptual da base Django:

- estrutura do projeto;
- configuração por ambientes;
- dependências;
- templates, static e media;
- preparação para i18n;
- persistência e modelos iniciais;
- administração;
- segurança inicial;
- testes e qualidade;
- fluxo Git;
- documentação para agentes.

Não cobre conteúdo definitivo, design final, deployment, serviços externos ou
funcionalidades completas do portfólio.

## 3. Princípios de implementação

- simplicidade antes de complexidade;
- cada linha de código futura deve existir por uma razão;
- modularidade funcional sem criar dezenas de apps;
- conteúdo separado da apresentação;
- nomes claros e estrutura previsível;
- progressive enhancement em vez de uma aplicação cliente pesada;
- dependências apenas quando existir uma necessidade concreta;
- decisões pendentes não devem ser transformadas silenciosamente em decisões
  finais;
- não criar conteúdo fictício como se fosse real;
- segurança e acessibilidade devem ser consideradas desde o início;
- a documentação do repositório é a fonte de verdade, independentemente da IA
  que executar a implementação.

Regra orientadora: **complexidade apenas quando existir necessidade real**.
Para a V1 não introduzir microserviços, API separada, React, Vue, Angular,
SPA, Redis, Celery, Kubernetes, múltiplas bases de dados ou serviços externos
sem justificação e aprovação documentadas.

## 4. Stack técnica V1

### Decisões aprovadas

- Python é a linguagem de backend.
- PHP não será utilizado.
- PT-PT é o idioma principal; EN e FR são idiomas adicionais.

### Solução recomendada para V1

- Python;
- Django;
- arquitetura monolítica modular;
- Django Templates;
- HTML semântico;
- CSS organizado segundo o design system;
- JavaScript mínimo e modular;
- progressive enhancement quando apropriado;
- Django Admin como solução base de administração de conteúdo.

Django é recomendado por fornecer routing, templates, ORM, formulários,
internacionalização, autenticação e autorização futuras, proteções de
segurança, Django Admin e uma estrutura de manutenção adequada a um site
editorial com várias áreas.

React, Vue, Angular, SPA e uma separação frontend/backend não fazem parte da
V1. Só podem ser reconsiderados se uma necessidade concreta justificar o
overhead adicional.

## 5. Estrutura de diretórios

Estrutura conceptual recomendada:

```text
project/
├── manage.py
├── config/
│   ├── settings/
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── core/
│   ├── pages/
│   ├── projects/
│   ├── photography/
│   └── contact/
├── templates/
│   ├── base.html
│   ├── includes/
│   └── components/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── media/
├── locale/
├── tests/
├── requirements/
├── docs/
├── .env.example
├── .gitignore
└── README.md
```

Finalidades:

- `manage.py`: entrada dos comandos Django.
- `config/`: configuração técnica do projeto, URLs e servidores WSGI/ASGI.
- `apps/`: módulos funcionais Django.
- `templates/`: templates partilhados e apresentação server-rendered.
- `static/`: CSS, JavaScript e imagens estáticas versionadas.
- `media/`: ficheiros carregados pelo conteúdo; não deve conter secrets.
- `locale/`: traduções de interface geridas pelo mecanismo i18n.
- `tests/`: testes transversais; testes específicos também podem viver nos
  respetivos apps.
- `requirements/`: ficheiros de dependências por contexto.
- `docs/`: documentação do projeto.

A estrutura é uma proposta de implementação. O agente pode ajustar nomes sem
alterar a separação funcional ou introduzir abstrações desnecessárias.

## 6. Estrutura Django

O projeto deve ter um pacote `config` separado dos apps de domínio. As
settings devem ser organizadas por ambiente sem duplicar configuração
inadvertidamente. `urls.py` deve delegar para os apps, mantendo no nível
principal apenas routing global.

Templates, static, media e locale devem ter caminhos explícitos e consistentes.
O `README.md` técnico futuro deve explicar como iniciar o projeto, executar
testes e configurar o ambiente.

## 7. Apps Django

### `core` — app técnica

Responsável por configuração comum, contexto global, páginas de erro,
metadados partilhados e utilitários estritamente necessários. Não deve tornar-
se um depósito de lógica sem dono.

### `pages` — app de conteúdo

Responsável por páginas institucionais e secções editoriais, incluindo Home,
About e páginas gerais quando houver conteúdo real.

### `projects` — app de conteúdo

Responsável por projetos, categorias, estados de publicação, destaque e
páginas de detalhe.

### `photography` — app de conteúdo

Responsável por fotografias, galerias e metadata visual. É separado porque
Fotografia é uma área de peso elevado e tem requisitos próprios de media.

### `contact` — app funcional

Deve ser criado apenas quando existir uma necessidade concreta de formulário
ou fluxo de contacto. A Foundation pode reservar o módulo sem implementar o
formulário final.

Não criar apps separados para cada pequena secção ou para funcionalidades
futuras sem conteúdo e comportamento definidos. Fitness e novas áreas podem
ser representados por conteúdo estruturado antes de justificar um app próprio.

## 8. Configuração do projeto

A configuração futura deve:

- separar settings comuns de settings por ambiente;
- manter `DEBUG`, hosts, URLs, email e storage configuráveis;
- usar `INSTALLED_APPS`, middleware e templates de forma explícita;
- evitar lógica de ambiente espalhada por views e modelos;
- falhar de forma clara quando faltar uma configuração obrigatória em
  produção;
- manter comandos de execução documentados no README técnico.

## 9. Ambientes

Devem ser distinguidos conceptualmente:

- **development**: desenvolvimento local, debug controlado e SQLite aceitável;
- **testing**: execução automatizada, dados isolados e configurações
  determinísticas;
- **production**: `DEBUG=False`, hosts explícitos, HTTPS, storage, base de
  dados, logs e backups definidos.

A implementação futura não deve usar configurações de desenvolvimento em
produção nem assumir que media local é adequado para produção.

## 10. Gestão de dependências

A solução recomendada é `requirements/` com ficheiros simples, por exemplo
`base.txt`, `development.txt` e `production.txt`, ou um `requirements.txt`
caso a implementação prove que a separação não é necessária.

Cada dependência deve:

- ter uma razão documentada;
- ser compatível com a versão de Python/Django escolhida;
- ser mantida numa versão controlável;
- ser removida quando deixar de ser necessária.

As funcionalidades nativas de Python e Django devem ser preferidas quando
forem suficientes. Nenhuma dependência deve ser instalada nesta fase
documental.

## 11. Variáveis de ambiente

`.env.example` deve documentar nomes e exemplos não sensíveis, sem valores
reais. Os valores reais devem ser fornecidos pelo ambiente de execução e
nunca versionados.

Categorias esperadas:

- `DJANGO_SETTINGS_MODULE`;
- `SECRET_KEY`;
- `DEBUG`;
- `ALLOWED_HOSTS`;
- URL e credenciais da base de dados;
- caminhos ou configuração de media/static;
- email;
- integrações futuras, apenas quando aprovadas.

Passwords, API keys, tokens, secret keys e credenciais nunca devem entrar no
Git, nos testes, em logs ou no conteúdo de exemplo.

## 12. Templates

### Solução recomendada

- Django Templates;
- `base.html` como layout comum;
- includes para elementos partilhados;
- componentes simples apenas quando reduzirem duplicação;
- HTML semântico e acessível;
- conteúdo fornecido pelo contexto, não hardcoded repetidamente em templates.

Templates não devem conter regras de negócio complexas. A interface deve
continuar funcional sem depender de hover ou JavaScript para ações essenciais.
O design final será implementado numa fase posterior, respeitando o design
system, UX e responsive strategy existentes.

## 13. Static files

Organização inicial:

```text
static/
├── css/
│   ├── tokens.css
│   ├── base.css
│   ├── layout.css
│   └── components/
├── js/
│   └── modules/
└── images/
```

CSS deve ser organizado, reutilizável e alinhado com o design system, sem
estilos espalhados sem critério. JavaScript deve ser mínimo, modular e
progressivo; não deve criar uma SPA nem duplicar lógica do servidor.

Não implementar componentes visuais nesta Foundation.

## 14. Media files

Fotografia é uma área principal e a Foundation deve preparar suporte
conceptual para:

- imagens originais e versões otimizadas;
- thumbnails e diferentes dimensões;
- galerias e ordem de apresentação;
- metadata e texto alternativo;
- formatos modernos quando suportados;
- validação de tipo, tamanho e conteúdo;
- limites de upload;
- armazenamento organizado;
- possibilidade futura de vídeo.

**Requisito:** media deve ser tratada de forma segura, organizada e separada
de static files.

Development storage não é production storage. A estratégia definitiva de
storage, processamento e distribuição de media é uma **DECISÃO PENDENTE**.
Não escolher agora um serviço externo nem assumir uma CDN.

## 15. Internacionalização

### Requisito aprovado

O site deve suportar PT-PT, EN e FR, com PT-PT como idioma padrão e principal.

### Preparação recomendada

- ativar e configurar o mecanismo Django i18n na implementação;
- distinguir traduções de interface de traduções de conteúdo;
- preparar seleção/troca de idioma acessível;
- definir fallback para PT-PT quando uma tradução alternativa não existir;
- manter textos de interface traduzíveis, sem duplicação hardcoded;
- estruturar conteúdo para poder adicionar idiomas no futuro.

Django i18n é a solução recomendada para mensagens de interface. A forma
definitiva de armazenar traduções de conteúdo (ficheiros, campos relacionados
ou outro modelo) é **DECISÃO PENDENTE**. A localização definitiva das URLs
também é **DECISÃO PENDENTE**; não assumir um formato de URLs sem aprovação.

## 16. Base de dados

**DECISÃO PENDENTE:** a base de dados final não está aprovada.

SQLite é aceitável para desenvolvimento local e testes iniciais pela sua
simplicidade. PostgreSQL é a opção provável/recomendada para produção, mas
continua pendente até à fase de implementação/deployment.

A implementação futura deve usar Django ORM e migrations, preservar
integridade referencial e separar configuração de desenvolvimento e produção.
Backups, retenção, recuperação, segurança de credenciais e acesso restrito
devem ser definidos antes de produção. Não configurar PostgreSQL nesta fase.

## 17. Modelos iniciais

Modelos conceptualmente necessários para a evolução da Foundation:

- `Area`: áreas do portfólio, incluindo Tecnologia, Fotografia e Fitness;
- `Page`: páginas e conteúdo editorial;
- `Project`: projetos, categorias, estado e destaque;
- `Category`: classificação reutilizável quando o conteúdo real a justificar;
- `Gallery`: agrupamento de fotografias;
- `Photo`/`Media`: ficheiros, metadata, dimensões, alt text e relação com
  galerias;
- `Link`: links externos e sociais;
- tradução/content locale: estrutura a decidir conforme a estratégia
  multilíngue aprovada.

`ContactSubmission`, autenticação de utilizadores, vídeos e modelos de
analytics podem ficar para fases posteriores. A Foundation não deve criar
todos estes modelos sem conteúdo e comportamento validados. Modelos futuros
devem ser normalizados, migráveis e administráveis sem editar HTML manualmente.

## 18. Administração / Django Admin

Django Admin é a solução base recomendada para administração de conteúdo V1;
não deve ser introduzido um CMS externo.

O objetivo é permitir gerir futuramente áreas, páginas, projetos, categorias,
fotografias, galerias, traduções e links através de modelos estruturados.
A organização deve usar listagens, pesquisa, filtros e campos claros quando
isso trouxer valor.

Permissões devem seguir o princípio do menor privilégio. O Admin não deve ser
exposto publicamente sem autenticação, HTTPS, configuração segura e proteção
operacional adequada. Não criar o Admin funcional nesta fase.

## 19. Segurança inicial

Requisitos para a implementação futura:

- `SECRET_KEY` fora do Git;
- `DEBUG` configurável e desativado em produção;
- `ALLOWED_HOSTS` explícitos;
- proteção CSRF;
- escaping e proteção contra XSS;
- ORM e queries parametrizadas contra SQL injection;
- validação de formulários e dados;
- uploads com validação, limites e nomes/storage seguros;
- autenticação e autorização futuras com menor privilégio;
- cookies e sessões com flags adequadas;
- security headers e HTTPS em produção;
- dependências atualizadas;
- Admin protegido;
- logs sem dados sensíveis;
- backups protegidos;
- rate limiting considerado quando necessário.

Estes são requisitos e áreas de validação, não uma promessa de segurança
automática por usar Django. A segurança deverá ser verificada com testes e
revisão na implementação.

## 20. Testes

A estratégia inicial deve privilegiar testes úteis e não volume artificial:

- testes unitários para regras de domínio;
- testes de modelos quando existirem;
- testes de URLs;
- testes de views;
- testes de formulários;
- testes de permissões e segurança relevantes;
- testes das funcionalidades críticas.

Uma funcionalidade está suficientemente testada quando os seus caminhos
principais, entradas inválidas relevantes e permissões aplicáveis estão
cobertos, e os testes reproduzem um comportamento esperado documentado.
Não criar dezenas de testes sem valor.

## 21. Qualidade de código

- nomes claros e consistentes;
- funções e módulos com responsabilidades pequenas;
- separação entre views, regras de domínio e apresentação;
- evitar duplicação;
- evitar abstrações prematuras;
- seguir convenções Django e Python;
- tratar erros explicitamente;
- comentários apenas quando acrescentarem contexto;
- decisões técnicas importantes documentadas.

Regra: **cada linha de código deve existir por uma razão**. A Foundation não
deve transformar um portfólio numa demonstração académica excessivamente
complexa.

## 22. Git e branches

Fluxo recomendado:

```text
main
  ↓
feature/fase branch
  ↓
commit
  ↓
push
  ↓
Pull Request
  ↓
review
  ↓
merge
  ↓
main
```

Branches representam trabalho ou fase, não uma IA específica. Exemplo:
`agents/foundation-v1`; não é necessário criar branches como `agents/claude`
ou `agents/copilot`. A IA é a ferramenta, e o projeto deve permanecer
independente dela.

## 23. Documentação para IA

Antes de implementar, qualquer agente deve consultar:

- `PROJECT_CONSTITUTION.md`;
- `PROJECT_STATUS.md`;
- `AGENTS.md`;
- `CLAUDE.md` e `GEMINI.md`;
- `.github/copilot-instructions.md`;
- `docs/11-ai/PROJECT_CONTEXT.md`;
- requisitos em `docs/02-requirements/`;
- design em `docs/03-design/`;
- arquitetura em `docs/04-architecture/`;
- esta Foundation.

Se encontrar conflito, o agente deve identificar o conflito, documentá-lo,
propor alternativa e aguardar aprovação. Nunca deve alterar silenciosamente
uma decisão documentada. A Foundation não depende de Claude nem de qualquer
integração de IA específica.

## 24. Critérios de conclusão da Foundation

Estes critérios pertencem à futura implementação e não devem ser executados
nesta fase documental. A Foundation será considerada implementada quando:

- a estrutura Django criada estiver documentada e iniciar localmente;
- ambientes development e testing estiverem separados;
- configuração sensível vier do ambiente;
- templates base estiverem funcionais;
- static files estiverem configurados;
- a preparação i18n base funcionar para PT-PT, EN e FR;
- persistência e migrations estiverem coerentes com a decisão aprovada;
- testes base passarem;
- requisitos de segurança inicial estiverem configurados e validados;
- a documentação de execução estiver atualizada;
- nenhuma tecnologia não aprovada tiver sido introduzida.

## 25. O que NÃO implementar nesta fase

Ficam explicitamente fora do scope:

- código da aplicação;
- projeto Django;
- dependências;
- base de dados ou migrations;
- deployment, domínio ou hosting;
- frontend e componentes visuais;
- design final da Home e das páginas;
- animações;
- galerias finais;
- projetos reais e conteúdo definitivo;
- CMS avançado;
- sistema de contacto final;
- autenticação completa;
- analytics e monitorização;
- SEO final;
- otimizações avançadas;
- infraestrutura complexa;
- integrações externas;
- Claude, integração com Claude ou outro serviço de IA.

## 26. Decisões pendentes

Continuam pendentes:

- versão exata de Python/Django;
- base de dados de produção, com PostgreSQL como opção provável;
- estratégia definitiva de traduções de conteúdo;
- estratégia definitiva de URLs multilíngues;
- storage e processamento de media;
- hosting e deployment;
- sistema de contacto e email;
- analytics e monitorização;
- autenticação e autorização além do Admin;
- detalhes finais de infraestrutura;
- conteúdo, projetos, galerias, Hero, paleta e tema visual.

Estas pendências não devem ser fechadas por inferência durante a
implementação.

## 27. Próxima fase

A próxima fase é a implementação da base técnica por um agente escolhido
posteriormente, com preferência inicial pelo Claude Code. Essa preferência
não constitui dependência nem decisão de integração.

O agente deverá transformar esta especificação em código apenas depois de
confirmar decisões pendentes, atualizar o estado de implementação e validar os
critérios de conclusão. A Foundation prepara o trabalho para qualquer agente,
não para uma IA específica.
