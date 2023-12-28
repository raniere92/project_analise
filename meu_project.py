import streamlit as st
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt


def main():
    curso = pd.read_csv('curso.csv', sep=';')
   
    # Mostrando o DataFrame no Streamlit
    st.write("### Data Frame:")
    st.write(curso)
    
    st.write("### Quais são as modalidades ofertadas no IFRN:")
    curso.groupby('modalidade')['modalidade'].count()

    # Agrupar e contar as modalidades
    modalidades = curso.groupby('modalidade')['modalidade'].count()

    # Exibir as modalidades no Streamlit
    st.write("Modalidades oferecidas no IFRN:")
    st.write(modalidades)
    
    # cursos que são ofertados no ifcang
    st.write("### Cursos que são ofertados no ifcang:")
    curso.loc[curso.diretoria == 'DIAC/CANG', ['descricao']]
    
    # 10 campus com mais cursos ofertados
    #st.write("### 10 Campus com mais cursos ofertados:")
    #curso.groupby('diretoria')['diretoria'].sum().sort_values(ascending=False).head(10)
    
    # media de carga horaria dos curso no IFRN
    #st.write("### Media de carga horaria dos curso no IFRN:")
    #curso.groupby('carga_horaria')['carga_horaria'].count().mean()
    
    # area de atuação dos cursos 
    #st.write("### Área de atuação dos cursos:")
    #curso.groupby('eixo')['eixo'].count()
    
    
    # 5 maiores modalidades que são ofertadas no ifrn
    st.write("### 6 maiores modalidades que são ofertadas no IFRN:")
    curso_modalidade = curso.groupby('modalidade')['modalidade'].count().sort_values(ascending=False).head(6)
    x = curso_modalidade.index
    y = curso_modalidade.values
    fig = plt.figure(figsize=(14,8))
    plt.bar(x,y)
    st.pyplot(fig)
    
    #10 campus com mais cursos ofertados
    st.write("### 6 campus com mais cursos ofertados:")
    curso_campi = curso.groupby('diretoria')['diretoria'].count().sort_values(ascending=False).head(6)
    x = curso_campi.index
    y = curso_campi.values
    fig = plt.figure(figsize=(14,5))
    plt.bar(x,y)
    st.pyplot(fig)
    
    #quais são as natureza de participação que o IFRN oferta
    #curso.groupby('natureza_participacao')['natureza_participacao'].count()
    st.write("### Quais são as natureza de participação que o IFRN oferta:")
    curso_participacao = curso.groupby('natureza_participacao')['natureza_participacao'].count().sort_values(ascending=False).head(6)
    x = curso_participacao.index
    y = curso_participacao.values
    fig = plt.figure(figsize=(10,5))
    plt.bar(x,y)
    st.pyplot(fig)
    
    # 6 cursos com mais areas de atuação
    st.write("### 6 cursos com mais areas de atuação:") 
    curso_area = curso.groupby('eixo')['eixo'].count().sort_values(ascending=False).head(6)
    x = curso_area.index
    y = curso_area.values
    fig = plt.figure(figsize=(20,10))
    plt.bar(x,y)
    st.pyplot(fig)
    
    # quantidades de cursos por coordenador
    st.write("### Quantidades de cursos por coordenador:")
    curso_coordenador = curso.groupby('coordenador')['coordenador'].count().sort_values(ascending=False).head(5)
    x = curso_coordenador.index
    y = curso_coordenador.values
    fig = plt.figure(figsize=(20,10))
    plt.bar(x,y)
    st.pyplot(fig)
    

    # Carrega o arquivo CSV
    st.subheader('Visualização dos Dados Originais:')
    st.write(curso)

    st.subheader('Renomear Dados Nulos:')
    selected_column = st.selectbox('Selecione a coluna:', curso.columns)
    new_name = st.text_input('Digite o novo valor para os nulos:', 'Novo Nome')
    
    if st.button('Renomear'):
        # Renomeia os dados nulos na coluna selecionada
        rename_null_values:any(curso, selected_column, new_name)

        st.subheader('Visualização dos Dados Atualizados:')
        st.write(curso)

        # Salva as alterações de volta no arquivo CSV
        curso.to_csv('curso_atualizado.csv', index=False)
        st.success('Dados atualizados e salvos no arquivo curso_atualizado.csv')
        

if __name__ == '__main__':
    main()
    