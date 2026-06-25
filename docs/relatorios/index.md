# Relatórios

## Pesquisa na Formação — IFES Campus Serra

Relatório institucional sobre a participação em pesquisa dos **egressos da graduação**
(Sistemas de Informação e Engenharia de Controle e Automação) e a trajetória dos
**discentes do mestrado PPComp**, incluindo tempo de formação por curso, fomento FAPES/FACTO
e produtividade docente.

[Abrir relatório completo](pesquisa-na-formacao.html){ .md-button .md-button--primary }

!!! note "Sobre os dados"
    Valores individuais de orçamento são apresentados como **% do total** (não em reais) para
    não expor pesquisadores. O tempo de formação é lido pela **mediana do atraso** por curso —
    SI e ECA têm naturezas distintas (diurno 4 anos vs noturno 6 anos) e não são comparáveis
    entre si. Durações abaixo de 3 semestres do previsto são sinalizadas como possível artefato
    do ingresso inferido da matrícula.

## Formandos × Pesquisa — versão analítica detalhada

Versão completa e operacional do relatório de formandos: distribuição por curso e cotas,
fomento por agência, tempo de formação **ajustado ao currículo de cada curso** (SI 8 sem · ECA 12 sem),
funil IC → TCC, ecossistema do orientador (IC × projetos FAPES), pipeline graduação → mestrado
e painel de fomento (recorte IFES Serra). Cada seção traz um quadro **"Como ler e decidir"**.

[Abrir relatório detalhado](formandos-pesquisa-detalhado.html){ .md-button }

!!! warning "Dados nominais"
    Esta versão **identifica pessoas** (bolsistas, orientandos e orientadores) para uso interno
    da gestão. Trate conforme a política de privacidade da diretoria.

## Docentes — Veículos e Impacto de Publicação

Análise da produção dos docentes do Campus Serra a partir dos currículos **Lattes**:
revistas e congressos onde publicam, classificados por impacto internacional
(**SJR/SCImago**, quartil Q1–Q4) e **Qualis CAPES** (periódicos 2017–2020 e conferências CC).
Cruza a **qualidade do veículo** com o **impacto real** — citações, **FWCI**, **h/g/m-index**,
percentis e crédito fracionado por autoria, via **OpenAlex** (casado por DOI). Inclui ranking
por impacto, por qualidade média, por sub-área, pesquisadores em ascensão, o **score combinado
revistas + congressos** e uma seção final de **fórmulas e referências** de cada métrica.

[Abrir análise de docentes](docentes-veiculos-impacto.html){ .md-button }

!!! note "Sobre os dados"
    Métricas derivadas de fontes públicas (Lattes, SCImago, Qualis CAPES, OpenAlex). Congressos
    têm Qualis apenas na área de Computação (lista CC 2016); eventos de Engenharia/Educação ficam
    fora. As citações e o FWCI vêm do **OpenAlex**, casados por **DOI** (1:1, sem ambiguidade de
    homônimo) — não do Google Scholar, cujo acesso automatizado é bloqueado; tendem a ser menores
    que os do Scholar, mas consistentes e comparáveis entre docentes.

## Rede de Colaboração dos Docentes 🚧

Site **interativo**: digite ou clique num pesquisador e veja a sua **ego-rede** de coautoria
(colaboradores, força das conexões, métricas). Inclui detecção de **comunidades** (Louvain)
ordenadas por relevância (impacto Qualis), e análise de padrões por **área, autores, coautores
e projetos**. Zoom, pan e controle de espalhamento.

[Abrir rede de colaboração](rede-colaboracao.html){ .md-button }

!!! warning "Under development"
    Versão preliminar — dados e métricas em validação. Coautoria/projetos cruzados por nome
    (sujeito a homônimo); coautores externos ao campus não entram no grafo.

## Edital PRPPG 13/2026 — Pesquisador de Produtividade (PPP)

Análise de **elegibilidade** dos docentes do Campus Serra ao **Edital PRPPG 13/2026** (Programa
Pesquisador de Produtividade). Aplica os critérios do edital ao **Lattes**: pontuação bibliográfica
por **percentil de citação** (Tabela 1, proxy WoS/Scopus via **OpenAlex**, janela 2021–2026) e
**orientações concluídas**, classificando cada docente na modalidade **PQ-1/PQ-2/PQ-3** que alcança.
Traz o **panorama** por modalidade, as **shortlists** de confirmados e de "com chance", e um ranking
interativo com o cálculo aberto artigo a artigo.

[Abrir análise do edital](ppp-edital-13-2026.html){ .md-button }

!!! note "Sobre os dados"
    Pontuação é um **piso** (lower bound): o cache OpenAlex guarda só os artigos mais citados (com
    **DOI**), então subestima quem publica muito ou teve pico antes de 2021 e ignora produção sem DOI
    (livros, capítulos, eventos, periódicos nacionais), que também pontua. O nível da orientação
    (IC × stricto sensu) não consta nos dados — usa-se o total concluído. **Vínculo a PPG stricto
    sensu** e **colaboração internacional** (exigências PQ-1/PQ-2) não estão nos dados e exigem
    conferência manual do Lattes.

## Dashboard de Impacto dos Docentes

Painel interativo dos indicadores de **impacto científico** do Campus Serra, via **OpenAlex**
(citações casadas por DOI do Lattes): **ascensão** (artigo de cada docente que mais ganhou citações
nos últimos 2 anos), **produção de elite** (top 10%/1%), **eficiência** (crédito fracionado por
autoria), **concentração** (curva de Lorenz + Gini), **benchmark por área** (FWCI mediano),
**qualidade de veículo** (% Q1/Q2 SJR e A1-A2 Qualis) e **sparkline** de citações/ano. Inclui
**base teórica** com referências de cada métrica.

[Abrir dashboard de impacto](dashboard-impacto-docentes.html){ .md-button }

!!! warning "Simulação — uso interno"
    Estimativas a partir de dados públicos do **OpenAlex** (só obras com **DOI** indexadas) — **não é o
    Google Scholar** e **não tem todos os artigos**; números tendem a ser menores que no Scholar, porém
    consistentes entre docentes. **Não** é avaliação oficial de desempenho — não usar para ranquear pessoas.
