
import matplotlib.pyplot as plt

def student_grade_chart(request, student_id):
    student = Student.objects.get(pk=student_id)
    grades = Grade.objects.filter(student=student)
    dates = [grade.date for grade in grades]
    scores = [grade.score for grade in grades]
    plt.plot(dates, scores)
    plt.xlabel('Date')
    plt.ylabel('Grade')
    plt.title(f'Grades for {student.name}')
    plt.grid(True)
    # Use BytesIO to create an in-memory image file
    imgdata = BytesIO()
    plt.savefig(imgdata, format='png')
    imgdata.seek(0)
    # Pass the image data to the template
    context = {'student': student, 'image': imgdata.getvalue()}
    return render(request, 'grades.html', context)

