#!/bin/bash
set -e

# Set base URL
BASE_URL="http://localhost:8000/api/v1"

# Colors for output
GREEN='\033[0;32m'
RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Testing DraftLine API endpoints...${NC}"

# Test root endpoint
echo -e "\n${BLUE}Testing root endpoint:${NC}"
curl -s http://localhost:8000/ | grep "Welcome"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Root endpoint working${NC}"
else
    echo -e "${RED}✗ Root endpoint not working${NC}"
    exit 1
fi

# Register a test user
echo -e "\n${BLUE}Registering test user:${NC}"
REGISTER_RESPONSE=$(curl -s -X POST \
    -H "Content-Type: application/json" \
    -d '{
        "email": "test@example.com",
        "password": "password123",
        "full_name": "Test User",
        "is_superuser": false
    }' \
    $BASE_URL/auth/register)

echo $REGISTER_RESPONSE | grep "test@example.com"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ User registration successful${NC}"
else
    echo -e "${RED}✗ User registration failed${NC}"
    echo $REGISTER_RESPONSE
fi

# Login with the test user
echo -e "\n${BLUE}Logging in with test user:${NC}"
LOGIN_RESPONSE=$(curl -s -X POST \
    -H "Content-Type: application/x-www-form-urlencoded" \
    -d "username=test@example.com&password=password123" \
    $BASE_URL/auth/login/access-token)

echo $LOGIN_RESPONSE
if echo $LOGIN_RESPONSE | grep -q "access_token"; then
    echo -e "${GREEN}✓ Login successful${NC}"
    # Extract token for further tests
    TOKEN=$(echo $LOGIN_RESPONSE | sed 's/.*"access_token":"\([^"]*\)".*/\1/')
else
    echo -e "${RED}✗ Login failed${NC}"
    exit 1
fi

# Test token endpoint
echo -e "\n${BLUE}Testing token validation:${NC}"
TOKEN_TEST_RESPONSE=$(curl -s -X POST \
    -H "Authorization: Bearer $TOKEN" \
    $BASE_URL/auth/login/test-token)

echo $TOKEN_TEST_RESPONSE | grep "test@example.com"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Token validation successful${NC}"
else
    echo -e "${RED}✗ Token validation failed${NC}"
    echo $TOKEN_TEST_RESPONSE
fi

# Get current user
echo -e "\n${BLUE}Getting current user:${NC}"
ME_RESPONSE=$(curl -s -X GET \
    -H "Authorization: Bearer $TOKEN" \
    $BASE_URL/users/me)

echo $ME_RESPONSE | grep "test@example.com"
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Get current user successful${NC}"
else
    echo -e "${RED}✗ Get current user failed${NC}"
    echo $ME_RESPONSE
fi

echo -e "\n${GREEN}All tests completed!${NC}"
