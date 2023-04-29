import pandas as pd
import seaborn as sns
import plotly.express as px

def student_info(request):
    # Example student data
    students = [
        {'name': 'Jane Doe', 'age': 13, 'siblings': 3, 'interests': 'dance', 'gpa': 3.7},
        {'name': 'John Smith', 'age': 14, 'siblings': 1, 'interests': 'soccer', 'gpa': 3.5},
        {'name': 'Sarah Johnson', 'age': 13, 'siblings': 2, 'interests': 'reading', 'gpa': 4.0},
        {'name': 'Mike Williams', 'age': 15, 'siblings': 0, 'interests': 'music', 'gpa': 3.8},
        {'name': 'Emily Brown', 'age': 14, 'siblings': 2, 'interests': 'art', 'gpa': 3.2},
    ]

    # Convert student data to a Pandas DataFrame
    df = pd.DataFrame(students)

    # Create a Seaborn scatterplot of student data
    sns_plot = sns.scatterplot(data=df, x='age', y='gpa', hue='interests', size='siblings', sizes=(20, 200))

    # Convert the Seaborn plot to a Plotly figure
    fig = sns_plot.get_figure()
    fig_data = fig.to_dict()

    # Get a list of student names for the dropdown menu
    student_names = df['name'].tolist()

    # Render the template with the Plotly graph and student names for the dropdown menu
    context = {'fig_data': fig_data, 'student_names': student_names}
    return render(request, 'student_info.html', context)
