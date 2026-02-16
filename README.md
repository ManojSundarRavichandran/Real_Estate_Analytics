# Real-Estate
The real estate domain involves property listings, sales transactions, agent performance, and buyer financing behavior across cities and neighborhoods. Property pricing depends on multiple factors such as location, furnishing status, metro connectivity, property attributes, and market demand. Data-driven analytics enables stakeholders to identify pricing trends, optimize sales strategies, and make informed investment decisions.
# Project Overview 
BrickView is a SQL-powered real estate analytics dashboard built using Python and Streamlit to analyze property listings, agent performance, sales efficiency, and buyer behavior. The platform integrates normalized relational data and delivers 30 business insights through interactive filters, charts, and location-based visualizations.
# Objective 
The objective of this project is to design a structured real estate analytics system that transforms raw listing and sales data into actionable insights using SQL and visual dashboards. It aims to support buyers, agents, and investors in making data-informed decisions.
# Data preparation & Cleaning 
## Data sources 
listings_final_expanded.json

property_attributes_final_expanded.json

agents_cleaned.json

sales_cleaned.csv

buyers_cleaned.json
## cleaning & standardization Process
Converted all column names to lowercase

Removed spaces and replaced with underscores for consistency

Ensured uniform naming conventions across datasets

Verified that all JSON files were flat (no nested structures)

Standardized numeric and categorical formats

# Data Type Validation 
## Listings Dataset
date_listed converted from object → datetime
All numeric columns validated
## sales Dataset
date_sold converted from object → datetime
## Buyers Dataset 
Data types validated
Missing values identified in loan_provider









