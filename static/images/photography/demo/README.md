# Assets DEMO — temporários

Estes ficheiros JPG são imagens geradas por código (gradientes,
formas simples, desfoque gaussiano, grão e vinheta, com as cores do
design system) — **não são fotografias reais do Miguel**, nem
imagens de terceiros, nem posts do Instagram, e não representam
nenhum trabalho, cliente, localização, data ou projeto real. Não têm
origem/licença de terceiros a documentar, porque não são de
terceiros: foram geradas localmente por
`generate_demo_images.py` (script auxiliar, fora do projeto Django).

Cada ficheiro sugere abstratamente um género fotográfico diferente
(retrato, arquitetura, edição criativa, street, paisagem), com um
tratamento de desfoque/grão/vinheta que se aproxima mais de uma
fotografia desfocada do que os gráficos vetoriais nítidos usados
antes — mas continuam a ser demonstração, não fotografia real.

Servem para avaliar, na secção Fotografia da Home:

- composição masonry/editorial e o seu ritmo visual;
- espaçamento e proporções (portrait, landscape, square);
- responsividade em diferentes larguras de ecrã;
- integração visual do item que representa vídeo
  (`demo-05-video.jpg`, sem ícone de play embutido — o indicador é
  feito em HTML/CSS, ver `.photo-card__play` em layout.css).

Cada imagem tem um pequeno selo "DEMO" discreto no canto inferior
esquerdo (watermark gerado no próprio script).

Quando existirem posts reais selecionados do Instagram (ver DEC-017 e
DEC-018 em `docs/04-architecture/decisions/decision-log.md`), estes
ficheiros devem ser removidos e substituídos pelas imagens/thumbnails
reais, ligadas ao respetivo post do Instagram.

Esta pasta e o seu conteúdo não devem ser tratados como conteúdo
final do portfólio.
