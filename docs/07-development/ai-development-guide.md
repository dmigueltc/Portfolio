# Guia de Desenvolvimento Assistido por IA

Este projeto pode ser trabalhado por diferentes ferramentas de IA e programadores. Nenhuma IA é fonte de verdade. A fonte de verdade é o repositório e a documentação.

## Ferramentas previstas

Planeamento e documentação:

- ChatGPT.
- OpenAI Codex.

Implementação principal futura:

- Claude Code.

Outras ferramentas possíveis:

- GitHub Copilot.
- Gemini.
- Outras ferramentas compatíveis com repositórios Git.

## Antes de implementar

Antes de qualquer funcionalidade significativa:

1. Ler `PROJECT_CONSTITUTION.md`.
2. Ler `PROJECT_STATUS.md`.
3. Ler `docs/11-ai/PROJECT_CONTEXT.md`.
4. Verificar `docs/04-architecture/decisions/decision-log.md`.
5. Consultar requisitos em `docs/02-requirements/`.
6. Consultar arquitetura e design relevantes.
7. Confirmar se a decisão está aprovada, pendente ou futura.
8. Não implementar decisões pendentes.
9. Atualizar documentação se a implementação alterar alguma decisão.

## Regras atuais

- A implementação autorizada nesta fase limita-se à Development Foundation V1.
- Não criar o portfólio final, componentes visuais finais ou conteúdo fictício.
- Não configurar deployment, hosting, PostgreSQL ou serviços externos sem decisão.
- Não criar CI/CD ou funcionalidades avançadas sem necessidade documentada.
- Não assumir PostgreSQL como decisão final.
- Não depender do Instagram para funcionamento do site.

Consultar `development-foundation-v1.md` para o scope técnico desta fase.

## Responsabilidade dos agentes

Cada agente deve:

- trabalhar em alterações pequenas e focadas;
- preservar documentação válida;
- registar decisões relevantes;
- marcar pendências explicitamente;
- evitar decisões arquiteturais sem autorização;
- manter Português de Portugal como idioma principal da documentação e interface principal.

## Continuidade

Quando passar trabalho para outra IA ou programador, atualizar `docs/11-ai/HANDOFF.md` ou criar um resumo de handoff com:

- estado atual;
- ficheiros alterados;
- decisões tomadas;
- pendências;
- riscos;
- próximo passo recomendado.
