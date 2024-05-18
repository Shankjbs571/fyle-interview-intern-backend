import unittest
from unittest.mock import patch

# class TestApp(unittest.TestCase):

#     def setUp(self):
#         self.app = app.test_client()
#         self.app.testing = True

#     @patch('helpers.get_utc_now')
#     def test_ready_endpoint(self, mock_get_utc_now):
#         mock_get_utc_now.return_value = '2024-05-18T00:00:00Z'  # Mock the UTC time return value
        
#         response = self.app.get('/')
        
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.content_type, 'application/json')
        
#         data = response.get_json()
#         self.assertEqual(data['status'], 'ready')
#         self.assertEqual(data['time'], '2024-05-18T00:00:00Z')

def test_ready_endpoint(client):
        # mock_get_utc_now.return_value = '2024-05-18T00:00:00Z'  # Mock the UTC time return value
        
        response = client.get('/')
        
        assert response.status_code == 200
        assert response.content_type == 'application/json'
        
        data = response.get_json() 
        assert data['status'] == 'ready'
        # assert data['time'] == '2024-05-18T00:00:00Z'