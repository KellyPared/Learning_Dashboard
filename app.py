from dash import Dash, dcc, html, Input, Output
import plotly.express as px
from data.student_demographics import demographics
import pandas as pd

#Start a dash instance
app = Dash(__name__)

colors = {
    'background': '#ffffff',
    'text': '#000000'
}

demographics_df = pd.DataFrame(demographics)
# Create a bar graph of student GPAs
graph_data = px.bar(demographics_df, x='Name', y='GPA',
                    template='plotly_dark',
                    labels={
                        'GPA': 'Student GPA'})

#make the colors different for the graph
graph_data.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

#add a scatterplot table √'Hours on Social Media': 1, 'Distance to School (miles)': 3
fig = px.scatter(demographics_df, x="Age", y="Distance to School (miles)",
                 size="Hours on Social Media", color="Grade", hover_name="Name",
                 log_x=True, size_max=60)

app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])


# Create a dropdown menu of student names
dropdown_menu = dcc.Dropdown(
    id='student-dropdown',
    options=[{'label': student['Name'], 'value': student['Name']} for student in demographics],
    value=demographics_df['Name'].iloc[0]
)

# Create a student demographic table
def create_demographic_table(student_name):
      # Find the row in the dataframe that matches the selected student name
    student_row = demographics_df.loc[demographics_df['Name'] == student_name]
    
    # If the row is not found, return an empty list
    if student_row.empty:
        return []
    
    # Create a table of the demographics of a student
    return html.Table([
        html.Tr([html.Td('Name:'), html.Td(student_row['Name'].iloc[0])]),
        html.Tr([html.Td('Age:'), html.Td(str(student_row['Age'].iloc[0]))]),
        html.Tr([html.Td('Grade:'), html.Td(str(student_row['Grade'].iloc[0]))]),
        html.Tr([html.Td('DOB:'), html.Td(student_row['DOB'].iloc[0])]),
        html.Tr([html.Td('Siblings:'), html.Td(str(student_row['Siblings'].iloc[0]))]),
        html.Tr([html.Td('Hours on Social Media:'), html.Td(str(student_row['Hours on Social Media'].iloc[0]))]),
        html.Tr([html.Td('Distance to School (miles):'), html.Td(str(student_row['Distance to School (miles)'].iloc[0]))]),
        html.Tr([html.Td('Athletic:'), html.Td(str(student_row['Athletic'].iloc[0]))]),
        html.Tr([html.Td('In the Band:'), html.Td(str(student_row['In the Band'].iloc[0]))]),
        html.Tr([html.Td('GPA:'), html.Td(str(student_row['GPA'].iloc[0]))])
    ],
        style={'color': 'black'})


# DFix the layout of the app
app.layout = html.Div([
    html.H1(
        children='Student Demographics', 
        style={'backgroundColor': colors['background'],
        'color': colors['text']}),
    
    #dash interactive visualizations
    dcc.Graph(
        id='gpa-bar-chart',
        figure=graph_data,
        style={
        'backgroundColor': colors['background'],
        'color': '#333333'
    }
    ),

    html.Div([
        html.H2('Student Demographic Information'),
        dropdown_menu,
        html.Div(id='demographic-table')
    ],
    style={'backgroundColor': colors['background']})
],
    style={'backgroundColor': colors['background']}
)


# Define the callback function to update the student demographic table
@app.callback(Output('demographic-table', 'children'),
              Input('student-dropdown', 'value'))
def update_demographic_table(student_name):
    return create_demographic_table(student_name)

if __name__ == '__main__':
    '''Dash includes "hot-reloading" 
    Dash will automatically refresh your browser when you make a change in your code.'''
    app.run_server(debug=True)
