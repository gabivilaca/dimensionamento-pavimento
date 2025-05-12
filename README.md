# Dimensionamento de Pavimentos Flexíveis

Esta ferramenta foi desenvolvida para auxiliar no cálculo das espessuras das camadas de pavimentos flexíveis, com base nas diretrizes do **DNIT**. O objetivo é fornecer uma interface simples e intuitiva para calcular as espessuras das camadas de revestimento, base e sub-base, além de exibir os resultados em um gráfico visual.

## Parâmetros de Entrada

Os seguintes parâmetros devem ser fornecidos para realizar os cálculos:

- **N**: Número de solicitações (N)
- **CBRn**: CBR Subleito (CBRn)
- **CBRSB**: CBR Sub-base (CBRSB)
- **KR**: KR (Coeficiente de Revestimento)
- **KB**: KB (Coeficiente de Base)
- **KSB**: KSB (Coeficiente de Sub-base)

## Como Usar

1. Insira os valores dos parâmetros listados acima nos campos correspondentes.
2. Clique no botão **"Calcular Espessuras"**.
3. Visualize os resultados das espessuras calculadas para as camadas de **Revestimento**, **Base** e **Sub-base**.
4. Confira o gráfico gerado, que exibe as camadas dimensionadas de forma visual.

## Tecnologias Utilizadas

- **React**: Biblioteca para construção da interface do usuário.
- **CSS**: Estilização personalizada para tornar a aplicação visualmente agradável.
- **JavaScript**: Lógica de cálculo das espessuras.
- **HTML**: Estruturação da interface.

## Estrutura do Projeto

- **`app/page.tsx`**: Componente principal da aplicação, responsável por renderizar a interface e gerenciar os cálculos.
- **`components/ui`**: Contém os componentes reutilizáveis, como `Card`, `Input`, `Button` e `Label`.
- **`styles`**: Arquivos CSS para estilização da aplicação.

## Exemplo de Uso

### Entrada
```json
{
  "N": 1000000,
  "CBRn": 5,
  "CBRSB": 10,
  "KR": 1.2,
  "KB": 1.5,
  "KSB": 1.8
}
```
### Saída
Revestimento (R): 5 cm
Base (B): 15 cm
Sub-base (h20): 20 cm

### Licença
Ferramenta desenvolvida por Gabriella Vilaça, sob orientação do Prof. Pedro Eugênio – PPGES / Escola Politécnica da UPE