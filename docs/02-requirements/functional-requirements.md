# Requisitos Funcionais V1

Este documento define os requisitos funcionais documentados para a primeira versão do portfólio Miguel Cardoso. O objetivo desta fase é descrever o que a estrutura e o conteúdo devem permitir apresentar ou permitir fazer, sem transformar esta documentação numa especificação técnica.

## Escopo e princípios

- O projeto encontra-se na Fase 1 — Levantamento e Planeamento.
- Esta documentação é orientada para requisitos de conteúdo, navegação e experiência do utilizador.
- Não se devem incluir decisões técnicas definitivas que ainda estejam pendentes.
- Nenhuma funcionalidade deve depender de uma IA específica.
- O conteúdo deve ser mantido de forma simples e organizada, sem dispersão desnecessária pelo código.
- O conteúdo e a estrutura devem permanecer compatíveis com a arquitetura da informação V1 e com o sitemap aprovado.

## Formato de registo

```text
ID:
FR-XXX

Nome:

Descrição:

Prioridade:
Must Have / Should Have / Could Have / Won't Have — V1 / A definir

Estado:
Aprovado / Proposto / Pendente / Futuro

Dependências:

Critérios de aceitação:

Observações:
```

## Requisitos funcionais

### FR-001 — Navegação

Nome:
Navegação principal clara e orientada às áreas do portfólio.

Descrição:
A navegação do site deve permitir ao visitante aceder facilmente às principais áreas do portfólio e compreender a estrutura geral do projeto.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Sitemap V1 e arquitetura da informação.

Critérios de aceitação:
- O site apresenta uma navegação principal clara para as áreas principais.
- A navegação inclui, no mínimo, as páginas/conceitos de Home, Sobre, Tecnologia, Fotografia, Fitness, Projetos e Contacto.
- A navegação permite uma leitura simples para visitantes comuns e um acesso rápido para visitantes profissionais.
- A navegação evita depender de elementos visuais ou interações complexas como único mecanismo de descoberta.

Observações:
A secção Explora deve ser entendida como parte da Home, e não como uma página independente, salvo decisão futura.

### FR-002 — Home

Nome:
Apresentação inicial do portfólio na Home.

Descrição:
A página inicial deve apresentar Miguel Cardoso de forma imediata, pessoal e profissional, funcionando como ponto de entrada para o restante sítio.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Posicionamento, identidade pública, estrutura da Home e conteúdo editorial.

Critérios de aceitação:
- A Home apresenta claramente o nome Miguel Cardoso.
- A Home apresenta a mensagem principal de posicionamento.
- A Home inclui um elemento visual, sem depender de fotografia pessoal obrigatória.
- A Home permite ao visitante entrar na exploração do site.
- A Home funciona sem depender de conteúdo futuro inexistente.
- A Home ainda pode ser completada futuramente sem exigir uma revisão estrutural completa.

Observações:
A estrutura da Home inclui Hero, Explora, Sobre mim, Projetos em destaque, Fotografia/criação, Contacto e Footer.

### FR-003 — Explora

Nome:
Secção Explora na Home.

Descrição:
A Home deve incluir uma secção de exploração das principais áreas do portfólio, permitindo ao visitante identificar rapidamente os temas e interesses principais.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Arquitetura da informação, conteúdo da Home e definições futuras das áreas.

Critérios de aceitação:
- A secção Explora apresenta as áreas principais do portfólio.
- A secção inclui, pelo menos, Tecnologia, Fotografia e Fitness.
- A secção permite, no futuro, incluir novas áreas sem reconstrução completa da estrutura.
- Cada área pode existir sem necessitar de imagem obrigatória.
- A apresentação não assume que todas as áreas tenham o mesmo peso visual.

Observações:
Não deve existir um compromisso de que todas as áreas tenham imagem, elementos visuais ou conteúdo detalhado na V1.

### FR-004 — Sobre mim

Nome:
Apresentação do Miguel e ligação para a página Sobre.

Descrição:
A Home deve incluir uma apresentação curta de Miguel e preparar um acesso para uma visão mais completa futura, sem requerer um perfil biográfico excessivo.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Conteúdo editorial, sitemap V1 e página Sobre.

Critérios de aceitação:
- A Home inclui um resumo curto sobre Miguel.
- A Home permite acesso à página Sobre, quando esta existir.
- A apresentação é suficiente para visitantes comuns sem necessidade de profundidade técnica.
- A estrutura permite evoluir para uma visão mais completa no futuro.

Observações:
A página Sobre deve ser acessível e compreensível para público não técnico, sem depender de fotografia pessoal.

### FR-005 — Tecnologia

Nome:
Área de tecnologia como eixo principal do portfólio.

Descrição:
A área Tecnologia deve prepararse para apresentar conteúdos relacionados com desenvolvimento, tecnologia, experiências, estudos, hardware, software, projetos e outros temas relevantes.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Arquitetura da informação, conteúdo futuro e decisão editorial.

Critérios de aceitação:
- A área Tecnologia está presente no sitemap e na navegação principal.
- A área pode, no futuro, incluir competências, projetos, estudos e experiências.
- A área não exige a criação de conteúdo fictício para preencher espaço.
- A informação pode ser apresentada com diferentes níveis de profundidade para públicos distintos.

Observações:
A área deve ter peso superior a Fitness e deve ser compatível com o conceito de profundidade progressiva.

### FR-006 — Projetos

Nome:
Estrutura para apresentação de projetos reais e futuros.

Descrição:
A área Projetos deve permitir futura apresentação de projetos, com a possibilidade de adicionar, editar, remover, ocultar e destacar itens, sem criar projetos fictícios.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Conteúdo editorial final, gestão de conteúdo e arquitetura futura.

Critérios de aceitação:
- A área Projetos está incluída na estrutura do portfólio.
- A estrutura permite futuramente adicionar e gerir projetos.
- Os projetos podem ser destacados ou ocultados sem afectar o restante conteúdo.
- A área funciona sem exigir que existam projetos finais nesta primeira versão.
- Não são criados projetos fictícios para “preencher” o site.

Observações:
Cada projeto pode futuramente incluir título, descrição, imagem, categoria, tecnologias, estado, links, data e conteúdo detalhado.

### FR-007 — Fotografia

Nome:
Área de fotografia, edição e criação visual.

Descrição:
A área Fotografia deve preparar o espaço para apresentar fotografias, galerias, edição, vídeo e criação de conteúdo visual, mantendo uma estrutura flexível para crescimento gradual.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Conteúdo real, proposta visual e gestão de media.

Critérios de aceitação:
- A área Fotografia está presente na estrutura principal.
- A área pode incluir fotografias, edição, vídeo e criação de conteúdo.
- A área permite adicionar conteúdo progressivamente sem exigir galeria fictícia.
- A partir da documentação, é possível compreender que a área não deve ser preenchida com conteúdos inventados.

Observações:
A arquitetura deve permitir um crescimento gradual em galerias, álbuns e séries sem exigir uma decisão final de negócio ou técnica.

### FR-008 — Fitness

Nome:
Área de Fitness com presença proporcional e sem competir com as áreas principais.

Descrição:
A área Fitness deve existir como interesse pessoal/hobby, mantendo uma presença discreta e proporcional, sem transformar o site num espaço de treino, nutrição ou performance.

Prioridade:
Should Have.

Estado:
Aprovado.

Dependências:
Arquitetura da informação e definição de conteúdo editorial.

Critérios de aceitação:
- A área Fitness aparece na navegação e na estrutura geral do site.
- A presença visual e editorial de Fitness é inferior à de Tecnologia e Fotografia.
- A área não se transforma em um site de treino ou nutrição.
- A área funciona como parte do portfólio pessoal sem desviar a atenção do foco principal.

Observações:
A presença da área deve ser simples e discreta, com espaço para evolução futura apenas quando existir conteúdo real e decisão formal.

### FR-009 — Contacto

Nome:
Secção de contacto e canais de contacto.

Descrição:
A página ou secção de Contacto deve permitir encontrar formas de contacto relevantes e encaminhar o visitante para plataformas externas apropriadas.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Canais reais, segurança contra spam e decisão de comunicação.

Critérios de aceitação:
- O site oferece um caminho claro para contacto.
- O Contacto pode incluir redes sociais relevantes, incluindo Instagram, GitHub e LinkedIn, quando aplicável.
- O sítio não depende da API nem da disponibilidade do Instagram para funcionar.
- A estrutura permite evoluir para outros canais em qualquer momento.

Observações:
Instagram assume relevância especial como origem principal de tráfego, mas não deve ser a base funcional do site.

### FR-010 — Idiomas

Nome:
Suporte multilíngue com língua principal em PT-PT.

Descrição:
O portfólio deve suportar conteúdos em PT-PT, Inglês e Francês, mantendo o português de Portugal como idioma principal da comunicação pública.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Estratégia de tradução e arquitetura futura da interface.

Critérios de aceitação:
- O conteúdo principal é desenvolvido em PT-PT.
- O site permite suporte futuro a EN e FR.
- O conteúdo traduzível é organizado de forma separada da estrutura.
- O site não duplicará páginas inteiras apenas para traduzir texto.
- A arquitetura permite adicionar outros idiomas no futuro.

Observações:
O idioma principal deve continuar a ser PT-PT, sem converter a base documental para outra variedade linguística.

### FR-011 — Redes sociais

Nome:
Presença de redes sociais relevantes no ecossistema do portfólio.

Descrição:
O projeto deve permitir a ligação a redes sociais relevantes que apoiem a presença digital e a comunicação com o público, sem colocar dependências técnicas excessivas.

Prioridade:
Should Have.

Estado:
Aprovado.

Dependências:
Decisão final dos canais relevantes e regras de apresentação.

Critérios de aceitação:
- O projeto possui espaço para indicar redes sociais relevantes.
- O Instagram pode ter importância especial na comunicação.
- As redes sociais podem ser apresentadas como ligações sem depender de API externa.
- As redes sociais não substituem a navegação principal do site.

Observações:
O site não deve depender de plataformas externas para funcionar, mesmo que estas tenham peso estratégico.

### FR-012 — Conteúdo futuro

Nome:
Preparação para conteúdos futuros, sem forçar conteúdo inexistente.

Descrição:
O conceito do projeto deve facilitar a adição de conteúdo futuro, incluindo textos, imagens, links, informações pessoais e referências, sem espalhar esta informação de forma desordenada.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Arquitetura futura de gestão de conteúdo e documentação editorial.

Critérios de aceitação:
- O site pode receber novos conteúdos sem obrigar a reorganização estrutural completa.
- O conteúdo pode crescer além das áreas iniciais sem quebrar a lógica do site.
- O conteúdo futuro não é inventado para preencher páginas vazias.
- A arquitetura contempla a manutenção simples de textos e ligações.

Observações:
A criação de conteúdos reais e verificáveis deve prevalecer sobre a criação de conteúdo fictício apenas como preenchimento visual.

### FR-013 — Gestão de conteúdo

Nome:
Estrutura de manutenção simples e organizada do conteúdo.

Descrição:
O projeto deve permitir que o conteúdo principal do portfólio, incluindo projetos, áreas, textos, imagens, links e informações pessoais, seja mantido de forma organizada e sustentável.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Arquitetura técnica futura e decisão de sistema de gestão de conteúdo.

Critérios de aceitação:
- O conteúdo não fica desnecessariamente espalhado pelo código.
- A estrutura permite uma manutenção mais simples das informações públicas.
- A arquitetura futura pode separar conteúdo e apresentação sempre que fizer sentido.
- A documentação permite que outra IA ou programador compreenda de forma clara a origem e a organização da informação.

Observações:
A decisão final sobre a solução de gestão de conteúdo permanece pendente, mas o requisito de manutenção simples está aprovado.

### FR-014 — SEO / partilha social

Nome:
Preparação para descoberta e partilha do site.

Descrição:
O projeto deve preparar uma base para melhor descoberta no motor de busca e para partilha em redes sociais sem depender de uma solução específica ou de uma plataforma externa.

Prioridade:
Should Have.

Estado:
Aprovado.

Dependências:
Conteúdo final, estrutura de páginas e estratégia de comunicação.

Critérios de aceitação:
- O site deve ter uma estrutura clara e legível para motores de busca.
- As páginas principais devem ser compreensíveis e organizadas.
- A partilha em redes sociais deve poder usar títulos e descrições apropriadas.
- A estrutura não exige uma solução técnica específica para garantir a sua existência.

Observações:
Este requisito é funcional e orientado a conteúdo, não a uma implementação técnica específica no momento.

### FR-015 — Acessibilidade

Nome:
Experiência acessível e compreensível.

Descrição:
O conteúdo e a navegação devem ser acessíveis, legíveis e claros para públicos diversos, sem depender apenas de interações complexas ou de hover como mecanismo principal de navegação.

Prioridade:
Must Have.

Estado:
Aprovado.

Dependências:
Estrutura da informação, UX/UI futura e decisões visuais.

Critérios de aceitação:
- O conteúdo principal é legível e compreensível.
- A navegação é clara e direta para visitantes sem conhecimentos técnicos.
- O site não depende apenas de hover para permitir a exploração das áreas principais.
- A experiência permanece funcional em diferentes níveis de profundidade de leitura.

Observações:
A acessibilidade deve ser tratada como princípio orientador, sem transformar este requisito num conjunto de decisões técnicas definitivas nesta fase.

## Decisões ainda pendentes

Estes pontos continuam fora do escopo obrigatório desta fase e não devem ser transformados em requisitos funcionais aprovados até haver decisão formal:

- stack frontend;
- framework Python;
- base de dados;
- CMS ou sistema de gestão de conteúdo final;
- sistema de autenticação;
- deployment e hosting;
- paleta de cores definitiva;
- dark/light mode;
- detalhes finais de UI;
- conteúdo definitivo das páginas;
- projetos reais finais;
- canais de contacto definitivos;
- escolha do elemento visual principal da Hero.

## Observações finais

- Este documento está alinhado com o sitemap V1, com a arquitetura da informação e com o contexto documental do projeto.
- A prioridade da V1 é estabelecer clareza de conteúdo e orientação estrutural em vez de escolhas técnicas definitivas.
- Qualquer futura implementação deve continuar a respeitar estes requisitos e as decisões documentadas no repositório.


## Requisitos pendentes

- Sistema final de gestão de conteúdo.
- Estrutura final para projetos, fotografia, vídeos e serviços.
- Conteúdo definitivo das páginas.
- Formulário de contacto ou alternativa.
- Integração com Instagram ou simples ligação externa.
- Funcionalidades avançadas como pesquisa, filtros, blog, analytics, newsletter, PWA, API pública, dark mode e tags.
