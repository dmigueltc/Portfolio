# Instruções para GitHub Copilot

## Estado do projeto

O projeto está na FASE 1 — Levantamento e Planeamento.

Não implementar funcionalidades, componentes, frontend, backend, base de dados, autenticação, CI/CD ou dependências nesta fase sem autorização explícita.

## Tecnologia

Decisões atuais:

- Python está confirmado como linguagem de backend.
- PHP não será utilizado.
- Django é uma possibilidade a avaliar na fase de arquitetura técnica, não uma decisão final.
- PostgreSQL é uma possibilidade preliminar, não uma decisão final.
- Frontend final será definido na fase de arquitetura técnica.

## Fonte de verdade

Antes de sugerir alterações significativas, consultar:

- `PROJECT_CONSTITUTION.md`
- `PROJECT_STATUS.md`
- `docs/11-ai/PROJECT_CONTEXT.md`
- `docs/04-architecture/decisions/decision-log.md`
- requisitos em `docs/02-requirements/`

## Princípios

- Priorizar código simples, legível e mantível quando existir fase de implementação.
- Seguir a documentação existente como fonte de verdade.
- Manter alterações pequenas e relacionadas com a tarefa.
- Não adicionar dependências sem justificação.
- Não alterar arquitetura sem autorização e documentação.
- Não transformar decisões pendentes em implementação.

## Segurança

- Não inserir credenciais, tokens, API keys ou secrets no repositório.
- Tratar configurações sensíveis como variáveis de ambiente.
- Considerar segurança desde a conceção das alterações.

## Testes

- Testar alterações quando existir código testável.
- Propor testes adequados quando forem criadas funcionalidades.

## Documentação

- Atualizar documentação quando forem alterados requisitos, decisões, comportamento ou instruções de desenvolvimento.
- Manter Português de Portugal como idioma principal da documentação e da interface principal.
