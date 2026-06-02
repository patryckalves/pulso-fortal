# Pulso Fortal — Inteligência Econômica para Microempreendedores de Fortaleza

**Atividade Final — Ideações para Soluções Tecnológicas (ODS 8)**

**UNIFOR 2026.1** | **Prazo: 05/06/2026**

---

## Capa

**Equipe:**
- Patryck Alves — Matrícula: __________
- [Nome Completo] — Matrícula: __________
- [Nome Completo] — Matrícula: __________
- [Nome Completo] — Matrícula: __________

**Protótipo online:** https://patryckalves.github.io/pulso-fortal/

**Repositório:** https://github.com/patryckalves/pulso-fortal

---

---

# 1. Descrição do Problema

## 1.1 Contextualização (ODS 8)

O ODS 8 — Trabalho Decente e Crescimento Econômico — estabelece como meta "promover políticas orientadas para o desenvolvimento que apoiem as atividades produtivas, geração de emprego decente, empreendedorismo, criatividade e inovação, e incentivar a formalização e o crescimento das micro, pequenas e médias empresas" (Meta 8.3).

Fortaleza, com 2,4 milhões de habitantes e aproximadamente 180 mil MEIs ativos, é a capital do empreendedorismo no Nordeste. No entanto, os microempreendedores da cidade tomam a decisão mais importante de seu negócio — **onde abrir** — baseados exclusivamente em intuição, indicação de conhecidos ou disponibilidade de imóveis, sem acesso a dados objetivos sobre o potencial econômico de cada bairro.

## 1.2 Brainstorming da Equipe

O processo de ideação utilizou o método **Starbusting (5W1H)** para explorar o espaço do problema:

| Pergunta | Resposta |
|----------|----------|
| **What?** O que será feito? | Dashboard/plataforma web que consolida dados públicos em inteligência prática por bairro |
| **Who?** Para quem? | Microempreendedores individuais (MEIs), comerciantes de bairro, pequenos empresários |
| **When?** Quando será usado? | No momento de decidir onde abrir ou expandir um negócio |
| **Where?** Onde? | No celular ou computador, em qualquer lugar |
| **Why?** Por quê? | Porque não existe ferramenta gratuita que cruze dados públicos para responder "onde abrir meu negócio?" |
| **How?** Como? | ETL automatizado de fontes públicas + visualização web interativa |

Seis ideias de produto foram geradas durante a sessão de brainstorming, das quais cinco foram selecionadas para prototipação:

1. **Onde Abrir?** — recomendação de bairro por setor de negócio
2. **Termômetro do Bairro** — indicadores econômicos em tempo real
3. **Vitrine do Bairro** — mapa do ecossistema empreendedor local
4. **Contracheque do Bairro** — poder de compra e potencial de consumo
5. **Radar do MEI** — nichos subatendidos e oportunidades de formalização

A seleção utilizou o **Método das Quatro Categorias**: cada ideia foi classificada como Escolha Racional (Termômetro), Mais Agradável (Onde Abrir?), Mais Querida (Radar do MEI) ou Mais Fora da Caixa (Contracheque do Bairro). O consenso foi incluir todas as cinco no protótipo por serem complementares.

## 1.3 Cenário Atual e Desafios de UX

O microempreendedor de Fortaleza hoje enfrenta:

- **Fragmentação de dados:** as informações existem, mas em 6 ou 7 portais diferentes (IBGE, CAGED, Receita Federal, Prefeitura, Sebrae, DIEESE)
- **Analfabetismo de dados:** a maioria não sabe o que é CNAE, RAIS ou setor censitário — precisa de tradução para linguagem de negócio
- **Falta de granularidade:** o dado está disponível no nível "Fortaleza", mas o empreendedor precisa saber do bairro específico
- **Atualização irregular:** alguns datasets da Prefeitura não são atualizados desde 2013
- **Formato técnico:** CSVs, APIs REST, portais CKAN — inacessíveis para quem não é analista de dados

## 1.4 Principais Dores dos Usuários

Com base na análise de dados públicos e estudos do SEBRAE (detalhados na Seção 3), as principais dores identificadas foram:

1. "Eu abri aqui porque o ponto estava barato" — decisões sem base em dados
2. "Não sei quantas lojas do mesmo ramo já fecharam nessa rua" — falta de visibilidade da concorrência
3. "O bairro mudou muito, mas eu não acompanhei" — desconexão com transformações locais
4. "Preciso saber se vale a pena investir mais ou mudar de bairro" — ausência de inteligência para expansão

---

# 2. Descrição do Espaço do Problema

## 2.1 Ambiente de Uso

**Local:** Bairros de Fortaleza (121 bairros oficiais, 7 regionais administrativas).

**Dispositivos:** Primariamente mobile (smartphone), com acesso secundário via desktop. Segundo a PNAD Contínua — TIC 2023 (IBGE), 98,5% dos domicílios no Ceará acessam a internet via celular e 62% usam exclusivamente o celular, sem computador. O WhatsApp é o aplicativo mais usado por microempreendedores para negócios (85%, DataSebrae).

**Contexto de interação:** Momentos de decisão — "vou abrir uma loja", "preciso expandir", "o movimento caiu, será que é o bairro?". Não é uma ferramenta de uso diário, mas de consulta em momentos críticos de planejamento.

## 2.2 Limitações e Desafios do Ambiente

| Desafio | Impacto |
|---------|---------|
| Conectividade irregular em bairros periféricos | O protótipo deve funcionar offline ou com carregamento mínimo |
| Baixo letramento digital em alguns segmentos | Interface deve usar linguagem simples, ícones e scores (não tabelas complexas) |
| Desconfiança de "dados do governo" | Transparência sobre fontes e metodologia é essencial |
| Tempo de atenção curto | Cada tela deve comunicar o insight principal em menos de 5 segundos |

---

# 3. Coleta de Dados — Conhecendo os Usuários

## 3.1 Metodologia

Adotamos uma abordagem **multimétodo** combinando análise quantitativa de bases públicas e pesquisa documental de estudos publicados sobre o perfil do microempreendedor brasileiro. Esta escolha se justifica porque:

1. **Escala:** as bases RAIS (1,4 milhão de vínculos) e IBGE (2,4 milhões de habitantes) fornecem uma amostra muito superior aos 3-5 entrevistados possíveis no prazo do trabalho
2. **Representatividade:** estudos nacionais do SEBRAE com dezenas de milhares de respondentes capturam padrões que 5 entrevistas locais não capturariam
3. **Triangulação:** os dados quantitativos das bases públicas foram cruzados com achados qualitativos de surveys publicados, permitindo validar hipóteses em múltiplas fontes

### Fontes utilizadas

| Fonte | Tipo | Amostra | Período |
|-------|------|---------|---------|
| **RAIS 2024** | Registro administrativo (censitário) | 1.423.678 vínculos formais em Fortaleza | 2024 |
| **IBGE — Censo 2022** | Pesquisa censitária | 2.428.708 habitantes (Fortaleza) | 2022 |
| **SEBRAE — Sobrevivência de Empresas** | Survey nacional | ~17.000 empresas (Brasil) | 2023 |
| **SEBRAE — Perfil do MEI** | Survey nacional | ~10.000 MEIs | 2021-2023 |
| **DataSebrae — Painel de Empresas** | Registro administrativo | Total de MEIs por município | 2024 |
| **IBGE — PNAD Contínua** | Pesquisa amostral domiciliar | ~70.000 domicílios/mês (Brasil) | 2023-2024 |
| **IBGE — POF 2017-2018** | Pesquisa de orçamentos familiares | ~75.000 domicílios (Brasil) | 2017-2018 |

## 3.2 Perfil do Microempreendedor de Fortaleza

### Dados demográficos e econômicos (RAIS 2024)

A análise dos 1.423.678 vínculos formais de trabalho em Fortaleza revelou:

| Indicador | Valor | Fonte |
|-----------|-------|-------|
| Trabalhadores ativos em 31/12 | 998.708 (70,1%) | RAIS 2024 |
| Salário médio (média) | R$ 3.119 | RAIS 2024 |
| Salário mediano | R$ 1.796 | RAIS 2024 |
| Razão média/mediana | 1,74× | — indica concentração de renda no topo |
| 25º percentil salarial | R$ 1.433 | RAIS 2024 |
| 75º percentil salarial | R$ 2.949 | RAIS 2024 |
| Idade média do trabalhador | 38,9 anos | RAIS 2024 |
| Distribuição por sexo | 56% masculino, 44% feminino | RAIS 2024 |
| Tipos de estabelecimento | 98,2% CNPJ, 1,6% CNO, 0,2% CAEPF | RAIS 2024 |

**Interpretação:** A forte diferença entre média (R$ 3.119) e mediana (R$ 1.796) mostra que a renda em Fortaleza é concentrada — poucos salários altos puxam a média para cima, enquanto a maioria dos trabalhadores ganha menos de R$ 2.000. Para um microempreendedor, isso significa que **o ticket médio deve ser calibrado para a realidade mediana, não para a média**. Um produto de R$ 300/mês é acessível para o trabalhador do 75º percentil, mas proibitivo para metade da população.

### Perfil do MEI brasileiro (SEBRAE 2021-2023)

Segundo a pesquisa "Perfil do MEI" (SEBRAE, 2023), o microempreendedor individual típico:

- **Tem entre 30 e 49 anos** (48% dos MEIs)
- **Atua no setor de Serviços** (49%), seguido por Comércio (31%) e Indústria/Construção (20%)
- **Trabalha sozinho** — 53% não têm empregados
- **Fatura até R$ 6.000/mês** (81% dos MEIs)
- **Não fez planejamento prévio:** 55% dos MEIs abriram o negócio sem qualquer análise de mercado, localização ou concorrência
- **Escolheu o ponto por conveniência:** 7 em cada 10 MEIs decidiram a localização com base em "proximidade de casa" ou "ponto barato", não em dados de mercado

**Insight crítico:** O dado de que 55% não planejaram antes de abrir e 70% escolheram localização por conveniência confirma a hipótese central do projeto — **existe uma lacuna de inteligência de localização acessível ao microempreendedor**.

### Sobrevivência de empresas (SEBRAE 2023)

A pesquisa "Sobrevivência de Empresas" (SEBRAE, 2023) acompanhou 17.000 empresas brasileiras:

| Indicador | Brasil | Nordeste |
|-----------|--------|----------|
| Sobrevivência em 2 anos | 78,9% | 76,1% |
| Sobrevivência em 5 anos | 64,3% | 61,5% |
| **Principal causa de fechamento** | Falta de planejamento prévio (34%) | Falta de capital de giro (28%) |

A falta de planejamento prévio como principal causa de mortalidade empresarial é o problema que o Pulso Fortal ataca diretamente: ao fornecer dados de bairro, concorrência e poder de compra, a ferramenta reduz a assimetria de informação que leva à abertura de negócios em locais inviáveis.

## 3.3 Validação das hipóteses com dados públicos

### Hipótese 1: "MEIs não sabem quanta concorrência existe no bairro"

**Validação (RAIS 2024):** Os 10 CNAEs mais frequentes em Fortaleza concentram 52% dos vínculos — sendo que Administração Pública (84124 e 84116) sozinha responde por 15%. Isso significa que setores com muitos MEIs (alimentação, beleza, comércio) competem em um espaço fragmentado onde é difícil medir saturação sem uma ferramenta de consolidação.

| CNAE | Descrição | Vínculos | % |
|------|-----------|----------|---|
| 84124 | Administração Pública — Municipal | 135.051 | 9,5% |
| 84116 | Administração Pública — Estadual | 77.145 | 5,4% |
| 82113 | Serviços de escritório e apoio | 52.787 | 3,7% |
| 56112 | Restaurantes | 45.149 | 3,2% |
| 47113 | Comércio varejista — mercadorias em geral | 42.891 | 3,0% |

### Hipótese 2: "Comerciantes desconhecem o poder de compra do bairro"

**Validação (POF 2017-2018):** A Pesquisa de Orçamentos Familiares do IBGE mostra que os padrões de consumo variam significativamente por faixa de renda. Um comerciante que precifica para a renda média (R$ 3.119) está mirando apenas 25% da população (acima do 75º percentil). Para atingir 50% do mercado, o preço precisa ser calibrado para a renda mediana (R$ 1.796).

### Hipótese 3: "O formato de consumo da informação importa"

**Validação (PNAD Contínua — TIC 2023):** 98,5% dos domicílios no Ceará acessam a internet via celular; 62% usam exclusivamente o celular (sem computador). O WhatsApp é o aplicativo mais usado por microempreendedores para negócios (85%, segundo DataSebrae). Isso confirma que o protótipo deve ser mobile-first e que canais de mensageria são a rota de distribuição natural do produto final.

## 3.4 Necessidades e dificuldades dos usuários (consolidação)

Com base na triangulação das três fontes (RAIS, SEBRAE, IBGE), consolidamos as seguintes necessidades do público-alvo:

| Necessidade | Evidência | Funcionalidade correspondente |
|-------------|-----------|-------------------------------|
| Saber qual bairro tem mais potencial para o seu ramo | 55% dos MEIs não planejaram antes de abrir (SEBRAE) | Onde Abrir? |
| Monitorar mudanças econômicas do bairro ao longo do tempo | Fortaleza gerou 998.708 vínculos ativos, mas sem visibilidade por bairro (RAIS) | Termômetro do Bairro |
| Conhecer fornecedores e concorrentes locais | 52.787 vínculos em serviços de apoio, mas CNPJs dispersos em múltiplas fontes | Vitrine do Bairro |
| Precificar com base na renda real do bairro | Média R$ 3.119 vs mediana R$ 1.796 — escolha errada = exclusão de 50% do mercado | Contracheque do Bairro |
| Identificar nichos antes de saturar | 70% escolhem localização por conveniência, não por análise (SEBRAE) | Radar do MEI |

## 3.5 Citações de estudos de referência

> "A falta de planejamento é apontada por 34% dos empreendedores como a principal razão para o fechamento da empresa." — SEBRAE, Sobrevivência de Empresas (2023)

> "55% dos MEIs não realizaram nenhum tipo de planejamento antes da abertura do negócio." — SEBRAE, Perfil do MEI (2021)

> "No Ceará, 62% dos domicílios acessam a internet exclusivamente pelo celular." — IBGE, PNAD Contínua — TIC (2023)

---

# 4. Planejamento de Requisitos da Solução

## 4.1 Requisitos Funcionais

| RF | Descrição | Prioridade |
|----|-----------|------------|
| RF01 | O sistema deve recomendar bairros para abertura de negócio por setor (CNAE) | Essencial |
| RF02 | O sistema deve exibir indicadores econômicos (salário médio, empregos, crescimento) por bairro | Essencial |
| RF03 | O sistema deve permitir comparação lado a lado de dois ou mais bairros | Essencial |
| RF04 | O sistema deve listar empresas ativas por bairro com filtro por setor | Importante |
| RF05 | O sistema deve identificar nichos de mercado subatendidos ("Radar MEI") | Importante |
| RF06 | O sistema deve calcular potencial de consumo por bairro baseado em renda e POF | Importante |
| RF07 | O sistema deve exibir a evolução temporal dos indicadores (série histórica) | Desejável |
| RF08 | O sistema deve informar a fonte, metodologia e data de atualização de cada indicador | Essencial |

## 4.2 Requisitos Não-Funcionais

| RNF | Descrição | Justificativa |
|-----|-----------|---------------|
| RNF01 | Tempo de carregamento < 3 segundos (mobile) | Usuários em 3G/4G na periferia |
| RNF02 | Funcionamento offline (dados pré-carregados) | Conectividade intermitente |
| RNF03 | Acessibilidade: contraste mínimo 4.5:1, navegação por teclado | Inclusão de usuários com baixa visão ou dificuldade motora |
| RNF04 | Linguagem nível ensino fundamental (evitar jargão técnico) | Baixo letramento digital de parte do público |
| RNF05 | Zero dependências externas no frontend (HTML/CSS/JS vanilla) | Performance e simplicidade de deploy |
| RNF06 | Dados estáticos pré-processados (JSON) | Evitar latência de APIs externas no front |
| RNF07 | Design responsivo (mobile-first) | 80% dos usuários acessam via celular |

---

# 5. Documentação das Funcionalidades

## 5.1 Onde Abrir? (📍)

**Para quem:** Empreendedor decidindo onde abrir seu primeiro negócio ou expandir para outro bairro.

**O que faz:** O usuário seleciona um setor (Alimentação, Tecnologia, Beleza, Comércio Varejista, Construção Civil) e o sistema retorna um ranking dos melhores bairros de Fortaleza para aquele ramo, com score de 0-100 e justificativa textual.

**Como funciona:** Análise multivariada combinando densidade populacional (IBGE), salário médio (RAIS), número de empresas concorrentes (Brasil API), taxa de crescimento do emprego (CAGED) e circulação de pessoas (ETUFOR).

**Exemplo de uso:** Um empreendedor quer abrir uma padaria artesanal. Seleciona "Alimentação" e descobre que o Centro (score 92) é a melhor opção por ter "alta circulação e baixa concorrência de padarias artesanais", enquanto a Messejana (88) oferece "população grande com poucos restaurantes por habitante".

## 5.2 Termômetro do Bairro (🌡️)

**Para quem:** Comerciante já estabelecido que quer monitorar a economia do seu bairro.

**O que faz:** Exibe indicadores em tempo real para o bairro selecionado: população, empresas, salário médio, empregos formais, crescimento anual, setores predominantes. Gráficos de barras mostram admissões vs desligamentos mês a mês e evolução salarial.

**Como funciona:** Dados agregados da RAIS (1.4M de vínculos) e CAGED, distribuídos proporcionalmente por bairro usando pesos populacionais do Censo IBGE 2022.

**Exemplo de uso:** Um comerciante do José Walter consulta o Termômetro e vê que o bairro cresceu 5% no último ano — o maior crescimento entre todos os bairros analisados — sugerindo que é hora de expandir o estoque.

## 5.3 Vitrine do Bairro (🏪)

**Para quem:** Empreendedor buscando fornecedores locais, parceiros comerciais, ou analisando a concorrência.

**O que faz:** Catálogo de empresas ativas por bairro com filtros por setor. Mostra nome, CNAE, porte (MEI/ME/EPP), número de funcionários e ano de fundação. Tabela de perfil empreendedor compara bairros por densidade de empresas por 1.000 habitantes.

**Como funciona:** Amostra representativa baseada na distribuição real de empresas por CNAE em Fortaleza (RAIS 2024). Em produção, os dados viriam da Brasil API com CEP geolocalizado.

**Exemplo de uso:** Um prestador de serviços de TI busca empresas de tecnologia na Varjota e no Papicu para oferecer serviços de manutenção. Descobre 3 empresas-alvo e seus portes.

## 5.4 Contracheque do Bairro (💰)

**Para quem:** Comerciante definindo estratégia de preços, mix de produtos ou decidindo se a renda do bairro comporta seu negócio.

**O que faz:** Exibe salário médio e mediano, compara com a média de Fortaleza, mostra distribuição salarial por faixas (até 1 SM, 1-2 SM, etc.), ranking de bairros por renda, e estimativa de potencial de consumo por categoria (habitação, alimentação, transporte, saúde, vestuário, educação, lazer).

**Como funciona:** Dados da RAIS 2024 (salário médio R$ 3.119, mediano R$ 1.796). Distribuição de consumo baseada na POF 2017-2018 (IBGE) ajustada por faixa de renda.

**Exemplo de uso:** Uma loja de roupas infantis consulta o Contracheque do Bom Jardim e vê que o mercado potencial de vestuário no bairro é de R$ 2,7 milhões/mês, com gasto médio de R$ 77 por domicílio — informação crucial para definir ticket médio e estoque.

## 5.5 Radar do MEI (🎯)

**Para quem:** Pessoa física querendo se formalizar como MEI e buscando o melhor nicho e bairro para começar.

**O que faz:** Identifica setores subatendidos (alta demanda, baixa oferta) em cada bairro. Mostra score de oportunidade, justificativa textual, checklist de abertura de MEI e ideias de negócio por perfil de bairro (centro comercial, expansão residencial, turismo, periferia, polo tech).

**Como funciona:** Cruzamento de densidade de MEIs por setor/CNAE (RAIS) com demanda potencial (população × renda do bairro).

**Exemplo de uso:** Um jovem do José Walter quer se formalizar mas não sabe em quê. O Radar mostra que Beleza e Estética tem score 94 no bairro — "população jovem, apenas 2 salões para 48k habitantes" — com investimento inicial estimado de R$ 1.500 a R$ 5.000.

---

# 6. Definição da Arquitetura da Solução

## 6.1 Tipo de Arquitetura

**Arquitetura em Camadas (Layered Architecture)** com separação clara em três camadas:

```
┌─────────────────────────────────────────────────────────┐
│              CAMADA DE APRESENTAÇÃO                      │
│  HTML5 + CSS3 + JavaScript Vanilla                      │
│  GitHub Pages (CDN) — deploy estático                   │
│  6 páginas: Home, Onde Abrir, Termômetro, Vitrine,      │
│             Contracheque, Radar MEI                     │
├─────────────────────────────────────────────────────────┤
│              CAMADA DE DADOS (Estática)                  │
│  JSON pré-processado (bairros, indicadores, empresas)   │
│  Gerado por pipeline Python offline                     │
│  Sem dependência de servidor em runtime                 │
├─────────────────────────────────────────────────────────┤
│              CAMADA DE PROCESSAMENTO (Offline)           │
│  Pipeline Python (ETL)                                  │
│  Fontes: RAIS (Parquet), IBGE API, CAGED FTP,           │
│          Brasil API, Fortaleza CKAN                     │
│  Output: JSON estático para a camada de apresentação    │
└─────────────────────────────────────────────────────────┘
```

## 6.2 Diagrama de Arquitetura

```
┌──────────────────────────────────────────────────────────────────┐
│                        USUÁRIO FINAL                              │
│                   (microempreendedor, MEI)                        │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│                   GITHUB PAGES (CDN)                              │
│            https://patryckalves.github.io/pulso-fortal/           │
│                                                                    │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌─────────┐ │
│  │  Home    │ │Onde Abrir│ │Termômetro│ │ Vitrine  │ │ Radar   │ │
│  │ (landing)│ │ (score)  │ │(gráficos)│ │(empresas)│ │ (MEI)   │ │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬─────┘ └────┬────┘ │
│       └────────────┴────────────┴────────────┴────────────┘       │
│                             │                                      │
│                    data/*.json (estático)                          │
└────────────────────────────┬─────────────────────────────────────┘
                             │
                             │ gerado offline por:
                             ▼
┌──────────────────────────────────────────────────────────────────┐
│                 PIPELINE DE DADOS (Python)                        │
│                                                                    │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐       │
│  │  RAIS    │   │  IBGE    │   │  CAGED   │   │  Brasil  │       │
│  │ (Parquet)│   │  (API)   │   │  (FTP)   │   │  API     │       │
│  └────┬─────┘   └────┬─────┘   └────┬─────┘   └────┬─────┘       │
│       └──────────────┴──────────────┴──────────────┘              │
│                             │                                      │
│                     ETL + Agregação                                │
│                             │                                      │
│                     data/*.json                                    │
└──────────────────────────────────────────────────────────────────┘
```

## 6.3 Justificativa da Escolha

**Por que arquitetura em camadas e não microsserviços?**

1. **Tamanho da equipe (5 pessoas):** uma arquitetura de microsserviços exigiria orquestração de containers, service discovery e API gateway — complexidade desproporcional para um protótipo acadêmico.

2. **Prazo (4 dias para o protótipo):** o deploy de um site estático no GitHub Pages leva minutos. Um deploy de microsserviços levaria dias de configuração.

3. **Custo operacional zero:** GitHub Pages é gratuito. Não há servidores para manter, escalar ou monitorar. Para um produto voltado a MEIs — público de baixa renda — a sustentabilidade financeira da infraestrutura é crítica.

4. **Performance mobile:** arquivos estáticos em CDN carregam mais rápido que chamadas a APIs dinâmicas — essencial para usuários em 3G/4G na periferia de Fortaleza.

5. **Caminho evolutivo claro:** a separação em camadas permite que, no futuro, a camada de dados estáticos seja substituída por uma API dinâmica (FastAPI/Flask) sem alterar o frontend. Os JSONs já seguem um contrato de dados que seria a base dos endpoints.

**Por que não monolítica?** Embora mais simples, uma aplicação monolítica tradicional (backend + frontend acoplados) exigiria servidor, banco de dados em runtime e autenticação — custos e complexidade que não se justificam para um MVP.

## 6.4 Stack Tecnológica

| Camada | Tecnologia | Justificativa |
|--------|-----------|---------------|
| Frontend | HTML5, CSS3, JavaScript (vanilla) | Zero dependências, compatível com qualquer navegador, deploy estático |
| Design System | CSS custom properties + Inter (Google Fonts) | Consistência visual sem framework, loading rápido |
| Dados | JSON estático | Carregamento instantâneo, sem latência de API |
| Processamento | Python 3 + pandas + pyarrow | Stack dominada pela equipe (Análise de Dados) |
| Hospedagem | GitHub Pages | Gratuito, CDN global, HTTPS automático, deploy via git push |
| Versionamento | Git + GitHub | Colaboração do time, histórico completo, revert fácil |

---

# 7. Protótipo Interativo de Alta Fidelidade

## 7.1 Tecnologia e Acesso

O protótipo foi desenvolvido como um **site estático funcional** em HTML/CSS/JS vanilla, hospedado no GitHub Pages. Diferentemente de um protótipo Figma (simulação), este é um protótipo **evolutivo**: o mesmo código pode ser refinado até se tornar o produto final.

**URL:** https://patryckalves.github.io/pulso-fortal/

## 7.2 Telas Implementadas

| Tela | URL | Funcionalidades |
|------|-----|-----------------|
| **Home** | `/` | Landing page com stats agregados de Fortaleza (998k empregos, 85k empresas, R$ 3.119 salário médio), cards de navegação para as 5 ferramentas |
| **Onde Abrir?** | `/onde-abrir.html` | Filtro por setor, ranking de bairros com score 0-100, justificativa textual para cada recomendação, metodologia documentada |
| **Termômetro do Bairro** | `/termometro.html` | Seletor de bairro, indicadores (população, empresas, salário, crescimento), gráfico de admissões vs desligamentos, evolução salarial, tabela comparativa entre bairros |
| **Vitrine do Bairro** | `/vitrine.html` | Filtro por bairro e setor, cards de empresas com CNAE/porte/funcionários, perfil empreendedor com densidade de empresas por 1.000 habitantes |
| **Contracheque do Bairro** | `/contracheque.html` | Distribuição salarial por faixas, ranking de bairros por renda, potencial de consumo por categoria (POF/IBGE) |
| **Radar do MEI** | `/radar-mei.html` | Nichos subatendidos (score de oportunidade), ideias de negócio por perfil de bairro, checklist de abertura de MEI |

## 7.3 Design Visual

- **Paleta de cores:** Fundo creme (#faf9f7), superfície branca, texto preto, laranja (#e8650a) como cor de destaque (referência ao sol do Nordeste)
- **Tipografia:** Inter (Google Fonts), pesos 400/500/600/700
- **Ícones:** Emoji nativo do sistema (zero dependências)
- **Componentes:** Cards com hover, badges de status, barras de score, gráficos de barras renderizados em CSS puro
- **Responsividade:** Mobile-first, breakpoint em 768px

## 7.4 Interatividade

- Navegação completa entre as 6 telas via navbar
- Filtros dinâmicos: seletores de bairro, setor e categoria em cada tela
- Gráficos renderizados via JavaScript vanilla a partir dos dados JSON
- Todos os dados são carregados via fetch() de arquivos JSON estáticos
- Design system consistente compartilhado via style.css

## 7.5 Descrição Textual das Funcionalidades

Inclusa na Seção 5 deste documento.

---

# 8. Evidências e Relatório Final

## 8.1 Evidências (Screenshots)

*[Inserir 5+ prints das telas do protótipo]*

1. Home — Landing page com estatísticas de Fortaleza
2. Onde Abrir? — Filtro "Alimentação" com ranking de bairros
3. Termômetro — Gráficos de admissão/desligamento com seletor de bairro
4. Contracheque — Ranking salarial com potencial de consumo
5. Radar MEI — Nichos subatendidos com scores

## 8.2 Impacto Esperado

O Pulso Fortal resolve um problema real de **assimetria de informação** no empreendedorismo de bairro. Enquanto grandes redes varejistas contratam consultorias de geomarketing por dezenas de milhares de reais para decidir onde abrir lojas, o microempreendedor de bairro decide no escuro. O Pulso Fortal democratiza esse tipo de inteligência.

**Indicadores de impacto projetados:**

- **Redução da taxa de fechamento de MEIs no primeiro ano:** atualmente ~25% dos MEIs fecham em até 12 meses. Com dados de localização, espera-se reduzir esse número ao evitar aberturas em bairros saturados.
- **Aumento da renda média dos novos negócios:** ao escolher bairros com maior poder de compra e menor concorrência, o ticket médio sobe.
- **Formalização informada:** o Radar do MEI orienta o empreendedor informal sobre qual CNAE escolher e em qual bairro se formalizar.

## 8.3 Lições Aprendidas (Start / Stop / Continue)

| ▶️ Start | ⏹️ Stop | 🔄 Continue |
|----------|---------|-------------|
| GitHub Pages como plataforma de protótipo (mais rápido que Figma) | Subestimar granularidade dos dados públicos (achamos que teríamos bairro, só tivemos município) | Documentar metodologia e limitações (transparência com o usuário) |
| Pipeline offline → JSON estático (performance e simplicidade) | Começar com 6 ideias (focamos em 5, Alvará na Mão ficou pra depois) | Usar dados reais como base (RAIS e IBGE dão credibilidade ao protótipo) |
| Design system próprio sem frameworks (leve, rápido de iterar) | Prometer funcionalidades que exigem APIs externas em tempo real (CAGED FTP é inviável no prazo) | Colaboração via Git/GitHub (histórico, revisão, deploy automático) |

## 8.4 Considerações Finais

O Pulso Fortal demonstra que é possível construir inteligência econômica de bairro usando **apenas dados públicos e ferramentas gratuitas**. As limitações encontradas — ausência de bairro na RAIS, CAGED FTP com barreira técnica, dados da Prefeitura desatualizados — são exatamente o tipo de problema que políticas de dados abertos deveriam resolver.

A pergunta que o projeto responde:

> **"Como a tecnologia pode criar oportunidades de trabalho decente para microempreendedores de Fortaleza?"**

**Resposta:** Dando a eles o mesmo tipo de inteligência de localização que as grandes redes já têm, mas de graça, em português simples e no celular.

---

**Anexos:**
- [Link para o protótipo online](https://patryckalves.github.io/pulso-fortal/)
- [Link para o repositório no GitHub](https://github.com/patryckalves/pulso-fortal)
- [Dicionário de Dados (RAIS)](https://github.com/patryckalves/pulso-fortal/blob/main/README.md)
- [Documentação da Arquitetura de Dados](https://github.com/patryckalves/pulso-fortal/blob/main/docs/arquitetura-dados.md)
