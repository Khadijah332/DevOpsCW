import unittest
from app import app, classify_weather, load_model
import numpy as np

class TestUnit(unittest.TestCase):
	def setUp(self):
		app.testing = True
		self.client = app.test_client()
	
	# Complete this function to test proper handling of missing input field in the input
	def test_post_missing_field(self):
		form_data = {
			'temperature': '270.277',
			'pressure': '1006',
			'humidity': '84',
			# 'wind_speed' is missing
			'wind_deg': '274',
			'rain_1h': '0',
			'rain_3h': '0',
			'snow': '0',
			'clouds': '9'
		}
		response = self.client.post('/', data=form_data)
		#checks app did not crash
		self.assertEqual(response.status_code, 200)

		#Check that error message is displayed
		self.assertIn(b"Error processing input", response.data)

	# Complete this function to test that the model can be loaded correctly
	def test_model_can_be_loaded(self):
		model = load_model()
		#The test ensures model is loaded and not none
		self.assertIsNotNone(model)
		

	# Test model classification is within the 9 classes, each time for a different class with three different inputs
	def test_clear_classification_output(self):
		test_input = np.array([
			[269.686,1002,78,0,23,0,0,0,0],	
        	[270.0, 1005, 80, 1, 30, 0, 0, 0, 5],
        	[271.0, 1008, 75, 2, 40, 0, 0, 0, 10]
			])
		for features in test_input:
			class_result, _ = classify_weather(features.reshape(1,-1))
			self.assertEqual(class_result, 'clear')# Ensure that 'clear' class is returned

	def test_rainy_classification_output(self):
		test_input = np.array([
			[279.626,998,99,1,314,0.3,0,0,88],	
			[280.0, 995, 95, 2, 320, 0.5, 0, 0, 90],
        	[281.0, 993, 97, 3, 330, 0.7, 0, 0, 85]
			])
		for features in test_input:
			class_result, _ = classify_weather(features.reshape(1,-1)) 
			self.assertEqual(class_result, 'rainy')# Ensure that 'rainy' class is returned

	def test_foggy_classification_output(self):
		test_input = np.array([
			[289.47,1015,88,2,300,0,0,0,20],
			[290.0, 1018, 90, 1, 310, 0, 0, 0, 25],
			[291.5, 1019, 95, 3, 290, 0, 0, 0, 35]
			])
		for features in test_input:
			class_result, _ = classify_weather(features.reshape(1,-1)) 
			self.assertEqual(class_result, 'foggy')# Ensure that 'foggy' class is returned
	
		
if __name__ == '__main__':
	unittest.main()