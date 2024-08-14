import streamlit as st
import pandas as pd
st.title("Gestão Financeira Pessoal")
st.header("Adicione suas receitas e despesas")
with st.form(key='revenue_form'):
    revenue_amount = st.number_input("Valor da Receita", min_value=0.0, step=0.01)
    revenue_category = st.selectbox("Categoria da Receita", ["Salário", "Investimentos", "Outros"])
    revenue_date = st.date_input("Data da Receita")
    revenue_submit_button = st.form_submit_button(label='Adicionar Receita')
with st.form(key='expense_form'):
    expense_amount = st.number_input("Valor da Despesa", min_value=0.0, step=0.01)
    expense_category = st.selectbox("Categoria da Despesa", ["Aluguel", "Alimentação", "Transporte", "Outros"])
    expense_date = st.date_input("Data da Despesa")
    expense_submit_button = st.form_submit_button(label='Adicionar Despesa')
if 'revenue_data' not in st.session_state:
    st.session_state['revenue_data'] = pd.DataFrame(columns=["Data", "Categoria", "Valor"])

if 'expense_data' not in st.session_state:
    st.session_state['expense_data'] = pd.DataFrame(columns=["Data", "Categoria", "Valor"])
if revenue_submit_button:
    new_revenue = {"Data": revenue_date, "Categoria": revenue_category, "Valor": revenue_amount}
    st.session_state['revenue_data'] = st.session_state['revenue_data'].append(new_revenue, ignore_index=True)

if expense_submit_button:
    new_expense = {"Data": expense_date, "Categoria": expense_category, "Valor": expense_amount}
    st.session_state['expense_data'] = st.session_state['expense_data'].append(new_expense, ignore_index=True)
st.header("Dados Financeiros")

st.subheader("Receitas")
st.dataframe(st.session_state['revenue_data'])

st.subheader("Despesas")
st.dataframe(st.session_state['expense_data'])
st.header("Análise Financeira")

total_revenue = st.session_state['revenue_data']['Valor'].sum()
total_expense = st.session_state['expense_data']['Valor'].sum()
balance = total_revenue - total_expense

st.metric(label="Saldo Total", value=f"R$ {balance:.2f}")

st.bar_chart(data=st.session_state['revenue_data'].groupby('Categoria')['Valor'].sum(), use_container_width=True)
st.bar_chart(data=st.session_state['expense_data'].groupby('Categoria')['Valor'].sum(), use_container_width=True)
