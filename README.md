### MVP - Machine Learning & Analytics PUC RJ

**Nome:** Luis Carlos Firmino Pinheiro
**Matrícula:** 4052026000838
**Data:** 13/06/2026
**Dataset:** [SINISTROS DE TRÂNSITO - PRF](https://dados.gov.br/dados/conjuntos-dados/sinistros-de-transito-agrupados-por-ocorrencia)
**Tipo de problema:** Classificação

# Modelo de classificação de acidentes de trânsito em rodovias brasileiras

![header](image/README/header.jpg)

### O objetivo desse estudo, é a criação de um modelo que atue com base em informações escassas disponiveis no momento de uma ocorência, para determinar a gravidade e dimensionar a resposta adequada.

A ideia é que o modelo classifique sem saber ainda exatamente o que ocorreu, como uma espécie de *sistema de triagem*, que poderia atuar com fontes de deteccão de ocorrência como sensores de pista, cameras, ou descrição de testemunhas que passaram pelo local.

Além das informações básicas como horário, data, localização, o dataset utilizado possui informações como causa e quantidade de vitimas, que são preenchidas posteriormente durante o registro da ocorrência, essas e outras variaveis posteriores não serão utilizada no modelo,   justamente porque o modelo seria utilizando antes desse tipo de informação estar disponível.

## Sobre o Dataset

Os dados que serão utilizados são provenientes do [Portal Brasileiro de Dados Abertos](https://dados.gov.br/home), no dataset [SINISTROS DE TRÂNSITO - PRF](https://dados.gov.br/dados/conjuntos-dados/sinistros-de-transito-agrupados-por-ocorrencia).
Os dados originais são armazenados em um [google drive](https://drive.google.com/drive/folders/1eI64p7H7LRc-wWDnwjIdYmYbWurMbwbT) em subpastas com um csv para cada ano. O arquivo zip com todos os anos foi salvo em `./raw_data/dados_prf.zip`, e o script `./consolidar_arquivos.py` junta todos os zips e subpastas em um único arquivo `./data/dados_prf.parquet`, para facilitar a leitura no projeto.
