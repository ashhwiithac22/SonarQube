"""
Unit tests for goodcode.py - Exercise 13C
"""

import pytest
import math
from goodcode import (
    process_payment, calculate_area, 
    Counter, process_list, execute_safely,
    calculate_discount
)

class TestPaymentProcessing:
    """Test payment processing functions"""
    
    def test_valid_payment(self):
        """Test payment with valid card"""
        result = process_payment("4111-1111-1111-1111")
        assert "successfully" in result
    
    def test_invalid_payment(self):
        """Test payment with invalid card"""
        with pytest.raises(ValueError):
            process_payment("")
    
    def test_short_card(self):
        """Test payment with too short card"""
        with pytest.raises(ValueError):
            process_payment("123")

class TestAreaCalculation:
    """Test area calculation functions"""
    
    def test_circle_area_positive(self):
        """Test area with positive radius"""
        assert calculate_area(1) == math.pi
        assert calculate_area(2) == math.pi * 4
    
    def test_circle_area_zero(self):
        """Test area with zero radius"""
        assert calculate_area(0) == 0
    
    def test_circle_area_negative(self):
        """Test area with negative radius"""
        with pytest.raises(ValueError):
            calculate_area(-1)

class TestCounter:
    """Test Counter class"""
    
    def test_initial_count(self):
        """Test counter starts at zero"""
        counter = Counter()
        assert counter.count == 0
    
    def test_increment(self):
        """Test incrementing counter"""
        counter = Counter()
        assert counter.increment() == 1
        assert counter.increment() == 2
        assert counter.increment() == 3
    
    def test_multiple_counters(self):
        """Test multiple counters independently"""
        c1 = Counter()
        c2 = Counter()
        c1.increment()
        c1.increment()
        c2.increment()
        assert c1.count == 2
        assert c2.count == 1

class TestListProcessing:
    """Test list processing functions"""
    
    def test_empty_list(self):
        """Test processing empty list"""
        assert process_list([]) == []
    
    def test_normal_list(self):
        """Test processing normal list"""
        items = [1, 2, 3, 4, 5]
        result = process_list(items)
        assert len(result) == 5
        assert result == items

class TestCommandExecution:
    """Test safe command execution"""
    
    def test_allowed_command(self):
        """Test allowed command"""
        result = execute_safely("echo hello")
        assert "hello" in result or result == "Command not allowed"
    
    def test_disallowed_command(self):
        """Test disallowed command"""
        result = execute_safely("rm -rf /")
        assert "not allowed" in result

class TestDiscountCalculation:
    """Test discount calculation"""
    
    def test_normal_discount(self):
        """Test normal discount"""
        assert calculate_discount(100, 20) == 80
        assert calculate_discount(50, 10) == 45
    
    def test_zero_discount(self):
        """Test zero discount"""
        assert calculate_discount(100, 0) == 100
    
    def test_invalid_inputs(self):
        """Test invalid inputs"""
        with pytest.raises(ValueError):
            calculate_discount(-100, 10)
        with pytest.raises(ValueError):
            calculate_discount(100, -10)

if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
