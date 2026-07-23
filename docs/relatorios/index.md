# Relatórios

## Extensão — Campus Serra (SRC)

Painel analítico das **ações de extensão e ensino** do Campus Serra, extraídas do **SRC**
(Sistema de Registro e Emissão de Certificados): **201 ações**, **525 atividades** e
**757 extensionistas**, com **+4.845 pessoas atingidas**. Inclui busca por palavra-chave,
página por ação/atividade/extensionista, jornada do formado, pendências e **dados abertos**
(JSON sem dados pessoais + `llms.txt` para IA).

[Abrir painel de extensão](campus-serra/index.html){ .md-button .md-button--primary }
[Painel no GitHub Pages :material-open-in-new:](https://ifesserra-lab.github.io/src/){ .md-button }

!!! note "Privacidade"
    Público-alvo aparece **apenas como contagens** (sem nomes/CPF/e-mail). Equipe e
    coordenadores(as) são **crédito público** de execução. Gerado pela lib
    [`src`](https://github.com/ifesserra-lab/src).

## Pesquisa × Extensão — Campus Serra

Cruzamento, por nome, entre os **coordenadores de pesquisa** (Horizon: FAPES/FACTO · Lattes ·
OpenAlex) e os **extensionistas** do SRC. Mostra que **78% dos coordenadores de pesquisa também
fazem extensão** e que **fazer extensão não reduz o impacto científico** (FWCI mediano acima da
média mundial), além de um gráfico de dispersão citações × pessoas impactadas e as listas de
"faz os dois" e "pesquisa sem extensão".

[Abrir Pesquisa × Extensão](pesquisa-x-extensao.html){ .md-button .md-button--primary }

!!! note "Convenções e limites"
    Dados **agregados e públicos** (crédito de coordenação/execução) — sem CPF, e-mail ou dados de
    alunos. Cruzamento por **nome normalizado** (sujeito a homônimo). O Horizon cobre os
    **coordenadores de pesquisa** (não todos os docentes); citações/FWCI via OpenAlex (só DOI,
    subestima).

## Índice de Extensão — 5 dimensões (FORPROEX)

Leitura da extensão do Campus Serra organizada nas **cinco dimensões dos Indicadores Brasileiros
de Extensão Universitária** (FORPROEX, 2017): Política de Gestão, Infraestrutura, Política
Acadêmica, Relação Universidade-Sociedade e Produção Acadêmica — preenchidas só com dados
verificáveis do SRC e do Horizon, com as **lacunas assinaladas**. Inclui a seção de **fontes com
resumo** e a ressalva de que FWCI/citações medem impacto científico, não impacto de extensão.

[Abrir Índice de Extensão](indice-extensao.html){ .md-button .md-button--primary }

!!! note "Como ler"
    Não é uma nota única: é um painel por dimensão. Cruzamentos por nome (sujeito a homônimo);
    idade e público em contagens (sem CPF/nome). Lacunas (satisfação/impacto social percebido,
    orçamento) exigem coleta que hoje não está no SRC.

## Captação de Projetos — FAPES + FACTO

Evolução e volume da **captação de projetos** dos professores do campus: gráfico de linha de
**projetos por ano** (FAPES + FACTO), **captação por ano** em índice, **bolsistas ao longo dos
anos**, **rubricas** do orçamento, e a **liderança de captação** por coordenador (FAPES e FACTO)
e por financiadora.

[Abrir relatório de captação](captacao-projetos.html){ .md-button .md-button--primary }

!!! note "Convenções e limites"
    Valores em **ordem de grandeza** (totais), **faixa + %** (por coordenador/financiadora) e
    **índice** (captação por ano) — sem cifras exatas. **FAPES** e **FACTO** são fontes distintas
    (não somadas); a FACTO entra no captado do campus só nos projetos **coordenados por docente**
    do campus. A curva de bolsistas inclui **B-UnAC** (ensino/EAD), não só pesquisa.

## ROI e Impacto da Pesquisa — painel multidimensional

Relatório técnico-metodológico de **retorno do investimento em pesquisa** do Campus Serra,
combinando quatro abordagens internacionais — **Payback Framework**, **CAHS Framework**,
**bibliometria responsável** (Manifesto de Leiden / DORA) e **estudos de caso no modelo REF** —
com **monetização seletiva**. Painel de **7 dimensões** (inputs, científico, formação, inovação,
social, econômico, casos), matriz Payback/CAHS, candidatos a estudo de caso e plano de
implementação. Inclui anexo de **artigos-fonte** (OpenAlex por DOI) e referências.

[Abrir relatório de ROI](roi-impacto-pesquisa.html){ .md-button .md-button--primary }

!!! danger "Dados preliminares — não é fonte da verdade"
    Este relatório é um **exercício metodológico exploratório**, gerado automaticamente a partir
    de fontes com **lacunas, duplicidades, homônimos e autodeclarações não auditadas** (Lattes,
    FAPES, FACTO, SigPesq, OpenAlex). Os números são **estimativas preliminares, sujeitas a
    revisão**, e **não devem ser usados como registro oficial**, avaliação individual ou base de
    decisão sem **conferência manual** com as fontes primárias. Use como **panorama**.

!!! note "Convenções e limites"
    **Valores financeiros não são expostos em cifra exata**: totais em **ordem de grandeza** e
    valores por coordenador/projeto em **faixa + %**. Todos os totais são **distintos** (obra
    co-autorada / dissertação co-orientada conta uma vez). O **ROI financeiro (%) não é
    reportado** por ausência de benefício monetizado. FACTO entra no **saldo do campus** apenas
    nos projetos **coordenados por docente do campus** (equipe não soma).

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

## Egressos — Impacto na Carreira 🚧

Painel do impacto de **ensino, pesquisa e extensão** na trajetória de **28 egressos** que passaram
pela mesma base no campus — monitoria, bolsa de IC (**FAPES/Prodest**) e o laboratório de extensão
(**LEDS/IFES**) — e hoje ocupam posições sênior em engenharia de software, dados, consultoria,
liderança técnica e gestão de TI (vários no exterior). Três visões: **dashboard executivo**
(crescimento salarial estimado, análise do grupo, **indicadores de impacto** — dispersão, fomento
FAPES, fluxo formação→trilha→destino e internacionalização), **panorama por egresso** (linha do
tempo e cards A–AB) e **evolução salarial ano a ano**.

[Abrir painel executivo](egressos/index.html){ .md-button .md-button--primary }
[Painel no GitHub Pages :material-open-in-new:](https://ifesserra-lab.github.io/egressos/){ .md-button }

!!! danger "Experimental — em construção"
    Metodologia ainda em desenvolvimento; **dados e conclusões preliminares, sujeitos a alteração**.
    Salários são **estimativas de mercado por anos de experiência** (Stack Overflow + câmbio + IPCA),
    **não** salários reais. Não usar como registro oficial.

!!! note "Privacidade"
    **Anonimizado**: egressos identificados só por letra (**A–AB**); **sem nomes, empresas ou
    localidades reais**. A origem comum institucional (LEDS/IFES, Prodest/FAPES, Morpheus Jr.) é
    crédito público de execução.
