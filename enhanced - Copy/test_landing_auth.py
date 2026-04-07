#!/usr/bin/env python3
"""
Test script to verify the landing page authentication functionality
"""

import sys
import os
import requests
import time

def test_landing_page_routes():
    """Test if all landing page routes are accessible"""
    base_url = "http://localhost:5000"
    
    routes = [
        "/",
        "/landing", 
        "/auth-forms",
        "/login-page"
    ]
    
    print("Testing Landing Page Routes...")
    print("=" * 50)
    
    for route in routes:
        try:
            response = requests.get(f"{base_url}{route}", timeout=5)
            if response.status_code == 200:
                print(f"✅ {route} - Status: {response.status_code}")
            else:
                print(f"❌ {route} - Status: {response.status_code}")
                return False
        except requests.exceptions.ConnectionError:
            print(f"❌ {route} - Connection Error (Server not running?)")
            return False
        except Exception as e:
            print(f"❌ {route} - Error: {e}")
            return False
    
    return True

def test_auth_forms_content():
    """Test if auth-forms route returns proper content"""
    base_url = "http://localhost:5000"
    
    try:
        response = requests.get(f"{base_url}/auth-forms", timeout=5)
        content = response.text
        
        # Check for key elements
        checks = [
            ("Login Form", "loginForm" in content),
            ("Register Form", "registerForm" in content),
            ("Tab Navigation", "auth-tabs" in content),
            ("Username Field", "loginUsername" in content),
            ("Password Field", "loginPassword" in content),
            ("Register Fields", "registerFirstName" in content),
            ("Submit Buttons", "btn btn-primary" in content)
        ]
        
        print("\nTesting Auth Forms Content...")
        print("-" * 30)
        
        all_passed = True
        for check_name, check_result in checks:
            if check_result:
                print(f"✅ {check_name} - Found")
            else:
                print(f"❌ {check_name} - Missing")
                all_passed = False
        
        return all_passed
        
    except Exception as e:
        print(f"❌ Error testing auth forms: {e}")
        return False

def test_landing_page_content():
    """Test if landing page contains expected elements"""
    base_url = "http://localhost:5000"
    
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        content = response.text
        
        # Check for key landing page elements
        checks = [
            ("Hero Section", "hero-section" in content),
            ("Features Section", "features-section" in content),
            ("SafeGuard Branding", "SafeGuard" in content),
            ("Sign In Button", "Sign In" in content),
            ("Get Started Button", "Get Started" in content),
            ("Auth Modal", "authModal" in content),
            ("Landing Styles", "landing-styles.css" in content)
        ]
        
        print("\nTesting Landing Page Content...")
        print("-" * 35)
        
        all_passed = True
        for check_name, check_result in checks:
            if check_result:
                print(f"✅ {check_name} - Found")
            else:
                print(f"❌ {check_name} - Missing")
                all_passed = False
        
        return all_passed
        
    except Exception as e:
        print(f"❌ Error testing landing page: {e}")
        return False

def test_javascript_functions():
    """Test if JavaScript functions are properly defined"""
    base_url = "http://localhost:5000"
    
    try:
        response = requests.get(f"{base_url}/", timeout=5)
        content = response.text
        
        # Check for JavaScript functions
        js_checks = [
            ("showAuthModal Function", "function showAuthModal" in content),
            ("closeAuthModal Function", "function closeAuthModal" in content),
            ("handleLogin Function", "function handleLogin" in content),
            ("handleRegister Function", "function handleRegister" in content),
            ("switchTab Function", "function switchTab" in content),
            ("togglePassword Function", "function togglePassword" in content)
        ]
        
        print("\nTesting JavaScript Functions...")
        print("-" * 32)
        
        all_passed = True
        for check_name, check_result in js_checks:
            if check_result:
                print(f"✅ {check_name} - Found")
            else:
                print(f"❌ {check_name} - Missing")
                all_passed = False
        
        return all_passed
        
    except Exception as e:
        print(f"❌ Error testing JavaScript: {e}")
        return False

def main():
    """Run all tests"""
    print("SafeGuard Landing Page Authentication Test")
    print("=" * 50)
    print("Make sure the Flask server is running on http://localhost:5000")
    print()
    
    tests = [
        ("Route Accessibility", test_landing_page_routes),
        ("Auth Forms Content", test_auth_forms_content),
        ("Landing Page Content", test_landing_page_content),
        ("JavaScript Functions", test_javascript_functions)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        if test_func():
            passed += 1
            print(f"\n{test_name}: PASSED ✅")
        else:
            print(f"\n{test_name}: FAILED ❌")
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Landing page authentication is ready.")
        print("\nTo test manually:")
        print("1. Start the Flask server: python app.py")
        print("2. Open browser to: http://localhost:5000")
        print("3. Click 'Sign In' or 'Get Started' buttons")
        print("4. Verify the authentication modal appears and forms work")
        return True
    else:
        print("❌ Some tests failed. Please check the issues above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)