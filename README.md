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

# Missing values Handling 
Buyers who did not take loans had:

loan_provider = None

loan_amount = 0

These were valid business cases, not errors.

Therefore, missing values were preserved and not deleted.

This ensures data integrity and avoids incorrect bias in financing analysis.

# Database Design & Schema 
A normalized relational schema (3NF) was created in SQLite.

Tables Created:

listings

properties

agents

buyers

sales

# Data Inserted into SQLite 
21,200 rows → listings

21,200 rows → properties

50 rows → agents

20,000 rows → buyers

720 rows → sales

# Data Analysis 
Performed analysis using 30 SQL queries covering:

Pricing analysis (AVG, SUM, median approximations)

Metro distance impact

Furnishing effect on price

Bedroom & bathroom influence

Sales velocity analysis

Sale-to-list price ratio

Agent performance metrics

Loan behavior analysis

Time-series monthly trends

## Techniques used:

GROUP BY aggregations

JOIN operations

Subqueries

Conditional filtering

Date-based grouping

# Streamlit Dashboard 
Built an interactive Streamlit application featuring:

Dynamic filters (City, Agent, Property Type, Price, Date)

Interactive map visualization

Pie chart (property distribution)

Bar chart (city-level aggregation)

Line chart (monthly trend analysis)

Paginated data tables

SQL insight explorer

All visualizations dynamically respond to applied filters.

# Key Technical Strengths
Structured ELT pipeline

Clean schema normalization (3NF)

Large-scale relational dataset (21k+ records)

Robust SQL analytical layer (30 queries)

Interactive front-end visualization

Business-aligned missing value handling

# Business Insights 
Property prices vary moderately across cities, with New York showing the highest median pricing in the dataset.

Metro proximity does not create a pricing premium, as properties farther from metro stations show slightly higher average prices.

Furnished properties command marginally higher prices compared to semi-furnished and unfurnished units.

Amenities such as parking and power backup contribute to slight pricing advantages.

Year built, bedroom count, bathroom count, and rental status do not significantly influence pricing in this dataset.

Houses sell faster (~58 days on average) compared to condos (~66 days), indicating stronger demand for independent housing.

Metro distance does not significantly affect time-on-market performance.

Approximately 49.31% of properties are sold above listing price, reflecting competitive pricing dynamics.

Sales activity peaked in October 2023 and gradually declined in 2024, indicating cyclical market behavior.

A substantial inventory backlog exists, with over 20,000 properties currently unsold.

Agent A0042 closed the highest number of deals, while Agent A0011 generated the highest total sales revenue.

Agent experience and rating do not show strong correlation with deal closure volume or speed.

Buyer distribution is nearly balanced between end users (50.1%) and investors (49.9%).

Loan uptake remains consistent across cities (~50%), with minimal regional variation.

Strategic focus should prioritize city-level pricing optimization, amenity-based differentiation, revenue-driven agent evaluation, seasonal marketing alignment, and improved inventory management



