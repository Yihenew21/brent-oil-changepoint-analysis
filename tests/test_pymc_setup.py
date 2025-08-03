#!/usr/bin/env python3
"""
Test script to verify PyMC3 setup works correctly.
"""

import sys
import os

def test_imports():
    """Test that all required packages can be imported."""
    try:
        import pandas as pd
        print("✓ pandas imported successfully")
        
        import numpy as np
        print("✓ numpy imported successfully")
        
        import pymc3 as pm
        print("✓ pymc3 imported successfully")
        
        import matplotlib.pyplot as plt
        print("✓ matplotlib imported successfully")
        
        import arviz as az
        print("✓ arviz imported successfully")
        
        print("\n🎉 All imports successful! PyMC3 setup is working correctly.")
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def test_pymc_model():
    """Test that PyMC3 can create a simple model."""
    try:
        import pymc3 as pm
        import numpy as np
        
        # Create simple test data
        data = np.random.normal(0, 1, 100)
        
        # Create a simple model
        with pm.Model() as model:
            mu = pm.Normal('mu', mu=0, sd=1)
            sigma = pm.HalfNormal('sigma', sd=1)
            obs = pm.Normal('obs', mu=mu, sd=sigma, observed=data)
        
        print("✓ PyMC3 model creation successful")
        return True
        
    except Exception as e:
        print(f"❌ PyMC3 model creation failed: {e}")
        return False

if __name__ == "__main__":
    print("Testing PyMC3 setup...\n")
    
    # Test imports
    imports_ok = test_imports()
    
    if imports_ok:
        # Test model creation
        model_ok = test_pymc_model()
        
        if model_ok:
            print("\n✅ All tests passed! Your PyMC3 environment is ready.")
        else:
            print("\n❌ Model creation failed.")
    else:
        print("\n❌ Import tests failed.") 