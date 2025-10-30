# ---- Builder Stage ----
# Use a Node.js image to build our frontend assets
FROM node:18-alpine as builder

# Set the working directory
WORKDIR /app

# Copy package files and install dependencies
COPY package.json ./
RUN npm install

# Copy the rest of the frontend source files
COPY . .

# Run the build script to generate the final CSS
RUN npm run build:css

# ---- Final Stage ----
# Use the official Python runtime
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy Python requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the built assets from the builder stage
COPY --from=builder /app/project/static/css/output.css ./project/static/css/output.css

# Copy the application code
COPY project/ ./project/
COPY run.py ./

# Make port 5000 available
EXPOSE 5000

# Define environment variable
ENV FLASK_APP run.py

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
