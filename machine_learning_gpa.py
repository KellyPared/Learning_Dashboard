import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from data.student_demographics import demographics



def predict_gpa(demographics):

    # Load the student data into a pandas dataframe
    demographics_df = pd.DataFrame(demographics)


    # Split the data into training and testing sets
    X = demographics_df.drop('GPA', axis=1)
    y = demographics_df['GPA']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create a decision tree classifier
    clf = DecisionTreeClassifier()

    # Fit the classifier to the training data
    clf.fit(X_train, y_train)

    # Make predictions on the testing data
    y_pred = clf.predict(X_test)

    # Evaluate the accuracy of the model
    accuracy = accuracy_score(y_test, y_pred)
    print('Accuracy:', accuracy)
    # Return the predicted GPA
    return y_pred.tolist()

predict_gpa(demographics)