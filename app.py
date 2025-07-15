import joblib
from dash import Dash, html, dcc
import plotly.graph_objects as go
from sklearn.metrics import confusion_matrix, roc_curve, roc_auc_score, classification_report

# Load saved variables
y_true = joblib.load('y_test.pkl')
y_pred = joblib.load('y_pred.pkl')
y_prob = joblib.load('y_prob.pkl')

# Metrics
cm = confusion_matrix(y_true, y_pred)
fpr, tpr, _ = roc_curve(y_true, y_prob)
roc_auc = roc_auc_score(y_true, y_prob)

# Dash App
app = Dash(__name__)
app.layout = html.Div([
    html.H1("Cancer Detection Dashboard", style={'textAlign': 'center'}),

    dcc.Graph(
        figure=go.Figure(
            data=go.Heatmap(
                z=cm,
                x=['Predicted 0', 'Predicted 1'],
                y=['Actual 0', 'Actual 1'],
                colorscale='Blues',
                showscale=True
            )
        ).update_layout(title='Confusion Matrix')
    ),

    dcc.Graph(
        figure=go.Figure([
            go.Scatter(x=fpr, y=tpr, mode='lines', name='ROC Curve'),
            go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='Random', line=dict(dash='dash'))
        ]).update_layout(
            title=f'ROC Curve (AUC = {roc_auc:.2f})',
            xaxis_title='False Positive Rate',
            yaxis_title='True Positive Rate'
        )
    ),

    html.H4("Classification Report"),
    html.Pre(classification_report(y_true, y_pred), style={'whiteSpace': 'pre-wrap'})
])

if __name__ == '__main__':
    app.run(debug=True)
