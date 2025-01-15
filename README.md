# movie-rating-project
A Python-based application that allows users to rate movies, calculate average ratings, and export data for analysis. Designed for simplicity and usability, this project is ideal for anyone looking to organize and analyze movie preferences.

## Overview
The goal of this project is to build a system that processes movie ratings data by:
1. Verifying the data for consistency and correctness.
2. Transforming the data to fit a desired format. ( missing values,remoivng outlies, making the numerical values standardized)
3. Sending the transformed data to Kafka for further processing.
4. Analyzing the data to gain insights into the ratings.

## Project Structure
- data_verification.py: Verifies the downloaded CSV file for consistency, missing values, and other integrity checks.
- kafka_producer.py: Pushes the processed data into Kafka topics for real-time streaming.
- analyze_data.py: Analyzes the data stored in Kafka topics to extract valuable insights.
- transform_data.py: Transforms the raw data into a suitable format for processing and storage.

## Requirements
The project relies on the following dependencies to run successfully. You can install them using the "requirements.txt" file.

## Setup and Installation

1. Clone the repository:
   bash
   git clone https://github.com/roazima/movie-rating-project.git
2. Navigate to the project directory:
   cd movie-rating-project
3. Create a virtual environment
   python3 -m venv venv
4. Active the vm
   for Mac: source venv/bin/activate
   for Windows: venv\Scripts\activate
5. Install the requirements:
   pip install -r requirements.txt
6. Make sure Kafka and Zookeeper is running:
  https://kafka.apache.org/quickstart
  https://zookeeper.apache.org/
7. Run the project
   python kafka_producer.py
   python transform_data.py
   python analyze_data.py

     
