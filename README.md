Desafio b2bflow - Python + Supabase + Z-API

Projeto desenvolvido para processo seletivo de estágio em Desenvolvimento Python.

O sistema realiza a leitura de contatos armazenados no Supabase e envia mensagens personalizadas via Z-API (WhatsApp).

---

Tecnologias utilizadas

- Python
- Supabase
- Z-API (WhatsApp API)
- Requests
- python-dotenv

---

Estrutura da tabela (Supabase)

A tabela deve se chamar:

**contatos**

Campos:

| campo     | tipo |
|----------|------|
| nome     | text |
| telefone | text |

### Exemplo de dados:

| nome  | telefone       |
|------|----------------|
| Luís  | 5512992438842 |


---

Variáveis de ambiente (.env)

Crie um arquivo `.env` na raiz do projeto:


SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase

ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token_da_zapi

---

Instalação

Instale as dependências:

</bash>
pip install supabase requests python-dotenv

Execute o projeto com:

python main.py

O sistema busca até 3 contatos no Supabase

Para cada contato, monta a mensagem personalizada:

Olá, <nome> tudo bem com você?

Envia a mensagem via Z-API automaticamente para o WhatsApp

Observações

O projeto foi feito com foco em boas práticas e integração de APIs
Código simples, organizado e funcional ponta a ponta

Desenvolvido para o processo seletivo da b2bflow 
