# 📦 Sistema de Inventário Doméstico – Python + Tkinter
Este projeto é uma aplicação desktop desenvolvida em Python para controle de inventário doméstico.
O sistema permite cadastrar, visualizar, atualizar e excluir itens de uma base de dados, além de associar imagens aos registros.

🚀 Tecnologias utilizadas
Python 3

Tkinter + ttk → Interface gráfica

PIL (Pillow) → Manipulação de imagens

tkcalendar → Seleção de datas

Banco de dados (SQLite, integrado pelo arquivo view.py)

Messagebox / Filedialog → Interações e seleção de arquivos

🎮 Funcionalidades
✔ Cadastro de itens com nome, descrição, local, marca/modelo, valor, data de compra e número de série.
✔ Upload de imagem associada ao item.
✔ Consulta em tabela interativa com scrollbars.
✔ Funções de CRUD completo:

Adicionar novos itens

Atualizar informações já cadastradas

Excluir itens selecionados

Visualizar a imagem vinculada
✔ Exibição automática de:

Quantidade total de itens

Valor total do inventário

🏗 Estrutura do código
enseri() → insere novo item no banco de dados.

atualizar() → carrega dados para edição e confirma atualização.

deletar() → remove item selecionado.

escolher_imagem() → permite anexar imagem ao item.

mostrar() → popula a tabela com todos os registros e calcula totais.

📊 Exemplo de uso
O usuário cadastra um notebook: nome, valor, marca, data de compra, número de série e anexa uma foto.

O item aparece na tabela interativa com os demais registros.

O sistema atualiza automaticamente o valor total e a quantidade de itens cadastrados.

É possível editar informações ou deletar registros quando necessário.

💡 Aprendizados
Construção de interfaces gráficas completas com Tkinter.

Integração de CRUD com banco de dados em aplicações desktop.

Manipulação de imagens (Pillow).

Organização de código com camada de visualização e banco (view.py).
