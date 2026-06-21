# AI Resume Intelligence System

## Overview

An AI-powered Resume Intelligence System built using FastAPI, Python, and MySQL.

## Features

* Resume Upload
* PDF Resume Parsing
* Name Extraction
* Email Extraction
* Phone Number Extraction
* Skills Extraction
* LinkedIn and GitHub Extraction
* Candidate Storage in MySQL
* Duplicate Candidate Prevention
* Suitability Score Calculation
* Top 10 Candidate Ranking

## Technology Stack

* Python
* FastAPI
* MySQL
* SQLAlchemy
* PyMySQL
* PDF Processing

## Run Project

Install dependencies:

pip install -r requirements.txt

Run:

python -m uvicorn main:app --reload --port 8001

Open:

http://127.0.0.1:8001/docs

## Output

The system processes resumes, stores candidate details, calculates suitability scores, and ranks candidates to identify the top 10 finalists.
