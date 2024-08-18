#!/bin/bash

# Start the backend server
cd backend
python -m uvicorn app.main:app --reload &

# Start the frontend server
cd ../frontend
npm run start &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?