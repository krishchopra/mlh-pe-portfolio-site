#!/bin/bash

# Test script for timeline_post endpoints
# Tests POST, GET, and DELETE endpoints

set -e  # Exit on any error

BASE_URL="http://127.0.0.1:5000"
API_ENDPOINT="/api/timeline_post"

echo "🚀 Testing Timeline Post Endpoints"
echo "================================="

# Generate random test data
RANDOM_ID=$(date +%s)
TEST_NAME="Test User $RANDOM_ID"
TEST_EMAIL="test$RANDOM_ID@example.com"
TEST_CONTENT="This is a test timeline post created at $(date) with ID $RANDOM_ID"

echo "📝 Test data:"
echo "   Name: $TEST_NAME"
echo "   Email: $TEST_EMAIL"
echo "   Content: $TEST_CONTENT"
echo ""

# Test 1: POST - Create a new timeline post
echo "🔄 Test 1: Creating new timeline post..."
POST_RESPONSE=$(curl -s -X POST "$BASE_URL$API_ENDPOINT" \
  -d "name=$TEST_NAME" \
  -d "email=$TEST_EMAIL" \
  -d "content=$TEST_CONTENT")

echo "✅ POST Response:"
echo "$POST_RESPONSE" | jq '.'

# Extract the ID from the POST response
POST_ID=$(echo "$POST_RESPONSE" | jq -r '.id')

if [ "$POST_ID" == "null" ] || [ -z "$POST_ID" ]; then
    echo "❌ Error: Could not extract ID from POST response"
    exit 1
fi

echo "📋 Created post with ID: $POST_ID"
echo ""

# Test 2: GET - Retrieve all timeline posts and verify our post exists
echo "🔄 Test 2: Retrieving all timeline posts..."
GET_RESPONSE=$(curl -s -X GET "$BASE_URL$API_ENDPOINT")

echo "✅ GET Response (showing first 500 characters):"
echo "$GET_RESPONSE" | jq '.' | head -c 500
echo "..."
echo ""

# Check if our post exists in the response
POST_EXISTS=$(echo "$GET_RESPONSE" | jq -r --arg id "$POST_ID" '.timeline_posts[] | select(.id == ($id | tonumber)) | .id')

if [ "$POST_EXISTS" == "$POST_ID" ]; then
    echo "✅ Verification: Test post found in GET response"
else
    echo "❌ Error: Test post not found in GET response"
    exit 1
fi

echo ""

# Test 3: DELETE - Clean up the test post
echo "🔄 Test 3: Deleting test timeline post..."
DELETE_RESPONSE=$(curl -s -X DELETE "$BASE_URL$API_ENDPOINT/$POST_ID")

echo "✅ DELETE Response:"
echo "$DELETE_RESPONSE" | jq '.'

# Check if deletion was successful
DELETE_MESSAGE=$(echo "$DELETE_RESPONSE" | jq -r '.message // .error')
if [[ "$DELETE_MESSAGE" == *"deleted successfully"* ]]; then
    echo "✅ Verification: Test post deleted successfully"
else
    echo "❌ Error: Failed to delete test post"
    echo "Response: $DELETE_MESSAGE"
fi

echo ""

# Test 4: Verify deletion by checking GET again
echo "🔄 Test 4: Verifying deletion with GET request..."
FINAL_GET_RESPONSE=$(curl -s -X GET "$BASE_URL$API_ENDPOINT")

POST_STILL_EXISTS=$(echo "$FINAL_GET_RESPONSE" | jq -r --arg id "$POST_ID" '.timeline_posts[] | select(.id == ($id | tonumber)) | .id // empty')

if [ -z "$POST_STILL_EXISTS" ]; then
    echo "✅ Verification: Test post successfully removed from database"
else
    echo "❌ Error: Test post still exists in database after deletion"
    exit 1
fi

echo ""
echo "🎉 All tests passed successfully!"
echo "📊 Test Summary:"
echo "   ✅ POST endpoint: Created test post"
echo "   ✅ GET endpoint: Retrieved and verified post"
echo "   ✅ DELETE endpoint: Removed test post"
echo "   ✅ Verification: Confirmed post deletion"
echo ""
echo "🧹 Cleanup completed - no test data left in database"
