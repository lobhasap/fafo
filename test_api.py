#!/usr/bin/env python3
"""
Test script for the House Price Prediction API
Run this after starting the API server to verify everything works
"""

import requests
import json
import time

# API base URL
BASE_URL = "http://localhost:5000"

def test_health():
    """Test the health endpoint"""
    print("🏥 Testing health endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/health")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Health check passed: {data}")
            return True
        else:
            print(f"❌ Health check failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Health check error: {e}")
        return False

def test_features():
    """Test the features endpoint"""
    print("\n📋 Testing features endpoint...")
    try:
        response = requests.get(f"{BASE_URL}/features")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Features retrieved: {data['features']}")
            return True
        else:
            print(f"❌ Features request failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Features request error: {e}")
        return False

def test_sample_prediction():
    """Test the sample prediction endpoint"""
    print("\n🎯 Testing sample prediction...")
    try:
        response = requests.get(f"{BASE_URL}/sample-prediction")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Sample prediction: {data['prediction_formatted']}")
            print(f"   Input: {data['sample_input']}")
            return True
        else:
            print(f"❌ Sample prediction failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Sample prediction error: {e}")
        return False

def test_custom_prediction():
    """Test a custom prediction"""
    print("\n🏠 Testing custom prediction...")
    
    test_data = {
        "square_feet": 2500,
        "bedrooms": 4,
        "bathrooms": 3,
        "age": 5,
        "distance_to_city": 2
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(test_data)
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Custom prediction: {data['prediction_formatted']}")
            print(f"   Input features: {data['input_features']}")
            return True
        else:
            print(f"❌ Custom prediction failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Custom prediction error: {e}")
        return False

def test_error_handling():
    """Test error handling with invalid data"""
    print("\n🚨 Testing error handling...")
    
    # Test missing feature
    invalid_data = {
        "square_feet": 2000,
        "bedrooms": 3
        # Missing bathrooms, age, distance_to_city
    }
    
    try:
        response = requests.post(
            f"{BASE_URL}/predict",
            headers={"Content-Type": "application/json"},
            data=json.dumps(invalid_data)
        )
        
        if response.status_code == 400:
            data = response.json()
            print(f"✅ Error handling works: {data['error']}")
            return True
        else:
            print(f"❌ Error handling failed: expected 400, got {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Error handling test error: {e}")
        return False

def test_api_info():
    """Test the main API info endpoint"""
    print("\nℹ️  Testing API info...")
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ API info: {data['message']}")
            print(f"   Version: {data['version']}")
            return True
        else:
            print(f"❌ API info failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ API info error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 Starting API Tests...")
    print("=" * 50)
    
    tests = [
        test_api_info,
        test_health,
        test_features,
        test_sample_prediction,
        test_custom_prediction,
        test_error_handling
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"❌ Test {test.__name__} crashed: {e}")
        time.sleep(0.5)  # Small delay between tests
    
    print("\n" + "=" * 50)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your API is working correctly.")
    else:
        print("⚠️  Some tests failed. Check the API server and try again.")
    
    return passed == total

if __name__ == "__main__":
    main() 