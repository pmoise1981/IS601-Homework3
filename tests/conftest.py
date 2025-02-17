import pytest
from faker import Faker
from calculator.calculator import Calculator

fake = Faker()

# Create a fixture that will generate fake data for the tests
@pytest.fixture
def generate_data():
    return {
        "a": fake.random_int(min=1, max=100),
        "b": fake.random_int(min=1, max=100),
        "operation": fake.random_element(elements=('add', 'subtract', 'multiply', 'divide')),
        "expected_result": None  # Placeholder for expected result, will be computed in test
    }

# Add a pytest command line option to specify the number of records
def pytest_addoption(parser):
    parser.addoption(
        "--num_records", action="store", default=10, type=int, help="Number of records to generate"
    )

# Fixture to generate multiple records
@pytest.fixture
def multiple_operations(request, generate_data):
    num_records = request.config.getoption("--num_records")
    return [generate_data for _ in range(num_records)]

