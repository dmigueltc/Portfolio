# Requisitos Não Funcionais V1

Este documento define os requisitos não funcionais V1 para o portfólio Miguel Cardoso. O objetivo é descrever os requisitos de qualidade, segurança, desempenho, manutenção e experiência do utilizador sem tomar decisões técnicas definitivas nesta fase.

IMPORTANTE: Esta fase é EXCLUSIVAMENTE documental. Não implementar, não instalar dependências, não fazer commits nem push nesta etapa.

## 1. Contexto

O projecto é um "Portfólio profissional + hub pessoal" cuja identidade pública é Miguel Cardoso.

Mensagem principal:
"Sou estudante de Engenharia Informática, interessado em desenvolvimento, tecnologia e criação de conteúdo."

Público principal: seguidores, amigos, familiares, conhecidos e público geral (principalmente visitantes provenientes do Instagram).
Público secundário: recrutadores, profissionais, empresas, potenciais clientes e colaboradores.

Áreas principais: Tecnologia (maior peso), Fotografia (maior peso), Fitness (hobby). O site deve permitir adicionar novas áreas no futuro sem reconstruir a aplicação.

Idiomas obrigatórios: PT-PT (principal), EN, FR.

Direção visual: Minimalista pessoal/criativa — clean, profissional, pessoal, criativo, agradável, simples sem ser vazio.

## 2. Documentação a ler (pré-requisitos)

Antes de alterar este documento, consultar:
- README.md
- docs/11-ai/PROJECT_CONTEXT.md
- PROJECT_CONSTITUTION.md
- PROJECT_STATUS.md
- AGENTS.md
- docs/04-architecture/information-architecture.md
- docs/04-architecture/sitemap-v1.md
- docs/04-architecture/decisions/decision-log.md
- docs/02-requirements/functional-requirements.md

Se existir conflito entre documentos, registar o conflito e indicar qual decisão/documento parece ser mais recente.

## 3. Objetivo

Criar/atualizar: docs/02-requirements/non-functional-requirements.md

Descrever COMO o sistema deve funcionar em termos de qualidade, segurança, desempenho, manutenção e experiência do utilizador, sem definir tecnologias específicas.

## 4. Categorias (sugestão de identificação)

- NFR-001 — Performance
- NFR-002 — Responsividade
- NFR-003 — Acessibilidade
- NFR-004 — Segurança
- NFR-005 — Privacidade e protecção de dados
- NFR-006 — SEO
- NFR-007 — Compatibilidade
- NFR-008 — Manutenibilidade
- NFR-009 — Escalabilidade
- NFR-010 — Qualidade do código
- NFR-011 — Internacionalização
- NFR-012 — Gestão de assets
- NFR-013 — Disponibilidade e recuperação
- NFR-014 — Observabilidade e erros
- NFR-015 — Experiência do utilizador
- NFR-016 — Segurança de conteúdo
- NFR-017 — Versionamento e colaboração
- NFR-018 — Sustentabilidade da arquitetura

Os identificadores podem ser ajustados conforme o padrão do repositório.

## 5. Performance (NFR-001)

Requisitos e orientações:
- Carregamento rápido e experiência snappy.
- Evitar JavaScript desnecessário e recursos bloqueadores.
- Optimização de imagens (formats modernos quando apropriado) e media.
- Lazy-loading quando adequado.
- Evitar assets pesados; preferir compressão e optimização.
- Minimizar requests críticos e optimizar a ordem de carregamento.
- Boa experiência em conexões móveis e dispositivos modestos.

Nota: Não definir números rígidos sem justificação. Objectivos mensuráveis podem ser definidos mais tarde na fase de testes.

## 6. Responsividade (NFR-002)

Requisitos:
- Suporte para smartphone, tablet, laptop e desktop.
- Mobile como experiência de primeira classe.
- Não depender de hover para funcionalidades essenciais.
- Layouts que se adaptem a diferentes resoluções sem cortar conteúdo essencial.

## 7. Acessibilidade (NFR-003)

Requisitos:
- Contraste adequado e legível.
- Navegação por teclado e foco visível.
- Texto alternativo em imagens relevantes.
- Semântica HTML correcta e labels apropriados.
- Hierarquia de títulos clara e conteúdo compreensível.
- Redução de movimento quando pedido pelo utilizador.
- Suporte a tecnologias assistivas (readers, etc.).

Nota: Aderir a boas práticas próximas das WCAG; não declarar conformidade formal sem testes.

## 8. Segurança (NFR-004)

Orientações principais:
- Validação e sanitização de entrada.
- Protecções contra XSS e CSRF (quando aplicável).
- Protecção contra SQL Injection e validação de uploads.
- Gestão segura de autenticação futura e armazenamento de passwords.
- Gestão segura de secrets (variáveis de ambiente) e princípio do menor privilégio.
- Dependências actualizadas e revisão de segurança periódica.
- HTTPS em ambiente de produção e headers de segurança apropriados.
- Protecções contra abuso (rate-limiting, validação de formulários).
- Logging sem exposição de dados sensíveis.

Nota: Documentar requisitos; não implementar agora.

## 9. Privacidade e protecção de dados (NFR-005)

Considerações:
- RGPD/GDPR (quando aplicável).
- Minimização de dados pessoais e justificativa para qualquer armazenamento.
- Formulários de contacto e tratamento de consentimento quando necessário.
- Cookies e analytics: documentar e pedir decisão posterior.
- Política de privacidade futura.

## 10. SEO (NFR-006)

Requisitos:
- Títulos e meta descriptions adequados.
- URLs legíveis e canónicas.
- Open Graph / social sharing metadata.
- sitemap.xml e robots.txt preparados.
- Dados estruturados quando fizer sentido.
- Suportar internacionalização/idiomas em URLs e metadados.

Nota: SEO não deve prejudicar performance ou acessibilidade.

## 11. Compatibilidade (NFR-007)

Requisitos:
- Suporte razoável para browsers modernos.
- Não forçar suporte para browsers antigos sem necessidade.

## 12. Manutenibilidade (NFR-008)

Princípios:
- Código e conteúdos devem ser legíveis e simples.
- Separação clara de responsabilidades.
- Estrutura que permita a uma nova pessoa localizar e editar conteúdos, assets e traduções.
- Evitar duplicação e complexidade desnecessária.
- Comentários apenas quando esclarecem o que não é óbvio.

## 13. Escalabilidade (NFR-009)

Requisitos:
- Permitir crescimento gradual (novos projetos, fotografias, áreas, idiomas, media).
- Evitar arquitectura excessivamente complexa antecipando necessidades hipotéticas.
- Preparado para crescer, simples no presente.

## 14. Qualidade do código (NFR-010)

Princípios:
- Nomes claros e consistentes.
- Funções / componentes com responsabilidade limitada.
- Tratamento adequado de erros.
- Evitar código morto e duplicação.
- Dependências justificadas.

Nota: Não escolher ferramentas de linting/formatting nesta fase.

## 15. Internacionalização (NFR-011)

Requisitos:
- Suportar PT-PT (padrão), EN e FR.
- Separar conteúdo traduzível da estrutura.
- Evitar textos hardcoded espalhados pelo código.
- Permitir adicionar idiomas futuramente com facilidade.

## 16. Gestão de assets (NFR-012)

Requisitos:
- Organização previsível de imagens, fotografias, vídeos, ícones e fontes.
- Nomes claros e evitar duplicação.
- Optimização e respeito por licenciamento/direitos de utilização.
- Não armazenar dados sensíveis em assets.

## 17. Disponibilidade e recuperação (NFR-013)

Requisitos:
- Backups quando existirem dados persistentes.
- Documentação de deployment e recuperação.
- Possibilidade de restaurar versões anteriores através do Git.

## 18. Observabilidade e erros (NFR-014)

Requisitos:
- Tratar erros de forma previsível e não expor stack traces ao utilizador.
- Registar erros relevantes em produção quando apropriado.
- Separar mensagens para utilizador das mensagens técnicas.

## 19. Experiência do utilizador (NFR-015)

Requisitos:
- Intuitivo para utilizadores não técnicos.
- Navegação clara e descoberta eficiente de informação.
- Evitar excesso de menus e animações perturbadoras.
- Estados claros para links, botões e formulários.
- Funcionamento robusto em mobile.

## 20. Segurança de conteúdo (NFR-016)

Requisitos:
- Evitar uploads inseguros e ficheiros perigosos.
- Validar e restringir tipos de ficheiro e tamanho quando existir upload.
- Proteger contra conteúdo externo não confiável e scripts incorporados.

## 21. Colaboração e Multi-IA (NFR-017)

Requisitos:
- Manter independência de qualquer IA como fonte única de verdade.
- Fomentar trabalho via Git, branches, commits e revisão.
- Preservar decision log e documentação.

## 22. Sustentabilidade da arquitectura (NFR-018)

Princípios:
- Evitar dependências e frameworks por moda.
- Evitar microserviços e sistemas demasiado complexos para a escala do projecto.
- Complexidade justificada por necessidade real.

## 23. Critérios de aceitação

Cada requisito não funcional deve ter critérios de aceitação verificáveis quando possível. Se depender de implementação, marcar "Validar na fase de testes".

## 24. Pendências (decisões técnicas ainda por tomar)

Manter pendentes:
- framework Python
- frontend
- base de dados
- CMS
- sistema de autenticação
- hosting e deployment
- CDN
- analytics
- sistema de email
- sistema de uploads
- estratégia final de cache
- monitorização e backups
- estrutura definitiva de assets
- arquitectura de tradução

## 25. Validação final

Depois de atualizar o documento, validar coerência com:
- docs/04-architecture/sitemap-v1.md
- docs/02-requirements/functional-requirements.md
- docs/11-ai/PROJECT_CONTEXT.md
- docs/04-architecture/decisions/decision-log.md

Procurar requisitos duplicados, contradições e evitar decisões técnicas prematuras. Garantir PT-PT como idioma do documento.

Mostrar no final:
- ficheiros alterados
- número de NFRs criados/atualizados
- principais requisitos
- decisões que continuam pendentes
- eventuais conflitos encontrados

Nota: NÃO fazer commit nem push como parte desta operação.
