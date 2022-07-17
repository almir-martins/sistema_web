# Sistema Web

## Fase 1 - Planejamento

A ideia de criar esse projeto veio da observação de várias necessidades de trabalho reportadas na plataforma Workana onde muitos usuários cadastram ofertas de trabalho que necessitem de um sistema em nuvem que seja escalável e ao mesmo tempo simples.

A decisão pelo uso de Python com Streamlit se deu pela versatilidade da ferramenta, a agilidade que a bilioteca permite desenvolver protótipos e módulos, pela integração com várias ferramentas de visualização de dados além da facilidade de hospedagem em diversos serviços de cloud.

A maioria das ofertas de trabalho verificadas eram de automação de planilhas ou vizualização de dados em dashboards que saíssem da suíte da Microsoft mas que fosse simples e leve, requisitos que a biblioteca Streamlit tem de sobra aliada ao poder do Python.

## Fase 2 - Sistema de Login

Com o intuito de disponibilizar no futuro a aplicação desenvolvida como exemplo de desenvolvimento para ofertas de freelancers e também para testar o comportamento da aplicação em ambiente do servidor, que tem dinâmica diferente do localhost quando envolve browsers e redirecionamento de páginas, realizei o deploy da mesma em um servidor de aplicações.

Fiz o deploy no Heroku Cloud que além de gratuito e seguro já tenho familiaridade de uso. Outra vantagem do Heroku é o deploy direto do Github inclusive de forma automática, fazendo re-deploy sempre que um commit é realizado no repositório.
[URL da aplicação:](https://websistema.herokuapp.com/)

## Fase 3 - Sistema de Login

Nesta fase está sendo desenvolvida a etapa de validação de usuários para que possa haver controle de acesso, criação da sessão de usuários logado e as seguintes entregas:

- Tela de login
- Tela de cadastro
- Tela de "Esqueci minha senha"
- Tela de "Esqueci meu username"
- Criação de sessão e armazenamento de cookies

