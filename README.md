📊 Integração e Visualização de Dados de Vendas com Python, MySQL e Power BI
📅 Período
Junho de 2025 - Até o momento

📝 Descrição do Projeto
Este projeto tem como objetivo centralizar, tratar e visualizar os dados de vendas de uma empresa, utilizando Python, MySQL e Power BI para garantir uma solução eficiente, escalável e analítica.

🚩 Etapas do Projeto
✅ 1. Extração de Dados
Automatizei a unificação de várias planilhas de um arquivo Excel. As planilhas continham informações como:

Empresas

Vendedores

Valores de vendas

Comissões

Formas de pagamento

✅ 2. Tratamento e Consolidação
Utilizei Python com a biblioteca Pandas para consolidar os dados em um único DataFrame:

python
Copiar
Editar
dados_unificado = pd.concat([dadosCJ, dadosCF, dadosCM, dadosDJ, dadosDF, dadosDM], ignore_index=True)
✅ 3. Armazenamento em Banco de Dados
Criei uma função para enviar os dados consolidados para um banco de dados MySQL. Após a importação, realizei um segundo tratamento direto via comandos SQL, para garantir a integridade e a consistência das informações.

✅ 4. Visualização com Power BI
Exportei os dados do MySQL para o Power BI, onde desenvolvi um dashboard interativo para a análise inicial das vendas.

🛠️ Tecnologias Utilizadas
Python (Pandas)

MySQL

Power BI

Excel
