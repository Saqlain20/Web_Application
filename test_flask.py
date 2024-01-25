import pytest 

from app import app

@pytest.fixture                           # it creates a client for us
def client():                   
    return app.test_client()

def test_welcome(client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/ping' page is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/welcome')       # a get request
    assert response.status_code == 200   #200 means succesfull
    assert response.json == {'message': "Welcome to the page"}


def test_predict(client):

    test_data = {"gender":"Male", "married":"Unmarried",
               "credit_history" : "Unclear Debts","applicant_income":100000,
               "loan_amount":2000000}
    
    response = client.post('/predict', json=test_data)
    assert response.status_code == 200
    assert response.json == {'loan_approval_status': "Rejected"}