# Arquitetura da Informação

Este documento descreve a organização conceptual do portfólio Miguel Cardoso. Não define implementação técnica, modelos de base de dados, rotas finais, templates ou componentes.

## Princípios

- O site deve funcionar como portfólio profissional + hub pessoal.
- O conteúdo deve ser compreensível para visitantes sem conhecimentos técnicos.
- A navegação deve permitir profundidade progressiva para visitantes profissionais.
- Tecnologia e Fotografia têm maior peso inicial que Fitness.
- A estrutura deve permitir adicionar novas áreas no futuro sem reconstruir a aplicação.
- Não criar páginas vazias apenas por antecipação.

## Públicos

### Público principal

Seguidores e público geral, especialmente pessoas provenientes do Instagram:

- amigos;
- familiares;
- conhecidos;
- seguidores;
- pessoas sem conhecimentos técnicos.

### Público secundário

- recrutadores;
- empresas;
- profissionais de tecnologia;
- programadores;
- potenciais clientes;
- colaboradores;
- parceiros profissionais.

## Profundidade progressiva

```text
Visitante comum
→ compreensão simples
→ exploração visual
→ interesses

Visitante profissional
→ áreas técnicas
→ projetos
→ tecnologias
→ detalhes
→ contacto
```

## Home — estrutura conceptual aprovada

### 1. Hero

Objetivo:
Apresentar Miguel Cardoso de forma imediata, simples e memorável.

Conteúdo conceptual:

```text
Miguel Cardoso

Tecnologia · Fotografia · Fitness

[Elemento visual]

Explorar ↓
```

Elemento visual possível:

- fotografia;
- composição;
- vídeo curto;
- animação;
- elemento gráfico;
- outro conteúdo visual.

Decisão atual:
O elemento visual não deve ser dependência obrigatória da página.

Pendente:
Elemento visual definitivo da Hero.

### 2. Explora

Título:
EXPLORA

Conceito:
“O que faço, gosto e crio.”

Áreas iniciais:

- Tecnologia.
- Fotografia.
- Fitness.

Regras:

- Usar cartões visuais e interativos futuramente.
- Cada cartão poderá ter nome, descrição, ligação e imagem/elemento visual opcional.
- Imagens não são obrigatórias para todas as áreas.
- Hover pode existir em desktop apenas como enriquecimento visual.
- Em mobile, a funcionalidade não pode depender de hover.

Pendente:
Conteúdo e ligações finais de cada área.

### 3. Sobre mim

Objetivo:
Responder de forma curta à pergunta “Quem é o Miguel?”.

Regras:

- Não ser autobiografia longa.
- Incluir texto curto.
- Incluir elemento visual sem depender de fotografia pessoal.
- Ligar para uma página Sobre mais completa, caso essa página seja aprovada.

Pendente:
Conteúdo final da página Sobre e decisão sobre página completa.

### 4. Projetos em destaque

Objetivo:
Preparar apresentação futura de projetos relevantes.

Regras:

- Não existem projetos pessoais finais definidos.
- A Home deve poder receber projetos posteriormente sem alteração estrutural.
- Deve existir possibilidade futura de adicionar, editar, remover, destacar e ocultar projetos.

Pendente:
Projetos reais e sistema de gestão de conteúdo.

### 5. Fotografia/criação

Objetivo:
Dar peso real à fotografia, edição de fotografia, vídeo e criação de conteúdo.

Regras:

- A área deverá ter maior peso que Fitness.
- Deve estar preparada para fotografias, edição, vídeo e criação digital.
- Não criar conteúdo fictício apenas para preencher a interface.

Pendente:
Estrutura final de galeria, álbuns, vídeos e media.

### 6. Contacto

Objetivo:
Permitir contacto e ligação a presença externa.

Possibilidades futuras:

- contacto direto;
- redes sociais;
- GitHub;
- LinkedIn;
- Instagram;
- outras plataformas relevantes.

Decisão atual:
Instagram terá importância especial como origem inicial de visitantes, mas o site não deve depender do Instagram para funcionar.

Pendente:
Canais finais e proteção contra spam.

### 7. Footer

Objetivo:
Encerrar a navegação com ligações essenciais, idioma e informação institucional mínima.

Pendente:
Conteúdo final.

## Áreas conceptuais

### Tecnologia

Área de maior peso. Pode incluir desenvolvimento, tecnologia, hardware, computadores, otimização e troubleshooting de PC.

### Fotografia

Área de maior peso. Pode incluir fotografia, edição de fotografia, vídeo e criação de conteúdo digital.

### Fitness

Interesse/hobby pessoal. Deve ter presença proporcional ao seu peso atual.

### Áreas futuras

Gaming, Viagens, serviços profissionais ou outras áreas podem ser adicionadas futuramente quando houver conteúdo real e decisão aprovada.

## Serviços futuros

A arquitetura deve permitir futura apresentação de serviços profissionais, como desenvolvimento web, tecnologia, fotografia, edição de fotografia, edição de vídeo e criação de conteúdo.

Não criar página de serviços vazia nesta fase.

## Pendências de arquitetura da informação

- Sitemap final.
- Páginas finais além da Home.
- Relação entre áreas, projetos e conteúdos visuais.
- Conteúdo definitivo das páginas.
- Estrutura final de URLs, incluindo idiomas.
