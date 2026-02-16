import streamlit as st
import sqlite3
import pandas as pd
import math
import matplotlib.pyplot as plt


st.set_page_config(
    page_title="Real Estate Dashboard",
    layout="wide",
    page_icon="🏠"
)

st.markdown("<h1 style='text-align:center;'>🏠 Real Estate Analytics Dashboard</h1>", unsafe_allow_html=True)
st.markdown("---")


conn = sqlite3.connect("realestate_data.db")
df = pd.read_sql_query("SELECT * FROM listings", conn)
df["date_listed"] = pd.to_datetime(df["date_listed"])


st.sidebar.header("🎛️ Filters")

cities = sorted(df["city"].unique())
selected_cities = st.sidebar.multiselect("City", cities, default=cities)

property_types = sorted(df["property_type"].unique())
selected_property_type = st.sidebar.selectbox("Property Type", ["All"] + property_types)

min_price, max_price = int(df.price.min()), int(df.price.max())
selected_price_range = st.sidebar.slider("Price Range", min_price, max_price, (min_price, max_price))

agents = sorted(df["agent_id"].unique())
selected_agent = st.sidebar.selectbox("Agent", ["All"] + agents)

min_date, max_date = df.date_listed.min(), df.date_listed.max()
selected_date_range = st.sidebar.date_input("Date Listed Range", (min_date, max_date))


filtered_df = df.copy()

if selected_cities:
    filtered_df = filtered_df[filtered_df.city.isin(selected_cities)]

if selected_property_type != "All":
    filtered_df = filtered_df[filtered_df.property_type == selected_property_type]

filtered_df = filtered_df[
    (filtered_df.price >= selected_price_range[0]) &
    (filtered_df.price <= selected_price_range[1])
]

if selected_agent != "All":
    filtered_df = filtered_df[filtered_df.agent_id == selected_agent]

if len(selected_date_range) == 2:
    start, end = selected_date_range
    filtered_df = filtered_df[
        (filtered_df.date_listed >= pd.to_datetime(start)) &
        (filtered_df.date_listed <= pd.to_datetime(end))
    ]


st.subheader("📋 Filtered Listings")

rows_per_page = 10
total_pages = math.ceil(len(filtered_df) / rows_per_page)

page = st.number_input("Page",
                       min_value=1,
                       max_value=max(total_pages, 1),
                       step=1)

start = (page - 1) * rows_per_page
end = start + rows_per_page

st.dataframe(filtered_df.iloc[start:end], use_container_width=True)

st.markdown("---")


col1, col2, col3 = st.columns(3)

col1.metric("Total Listings", len(filtered_df))
col2.metric("Average Price",
            f"${int(filtered_df.price.mean()):,}" if len(filtered_df)>0 else "0")
col3.metric("Max Price",
            f"${int(filtered_df.price.max()):,}" if len(filtered_df)>0 else "0")

st.markdown("---")


st.subheader("📊 Property Insights")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 🥧 Property Type Distribution")
    type_counts = filtered_df.property_type.value_counts()

    if not type_counts.empty:
        fig, ax = plt.subplots(figsize=(4, 4))

        ax.pie(
            type_counts,
            labels=type_counts.index,
            autopct='%1.1f%%',
            startangle=90,
            textprops={'fontsize': 9}
        )

        ax.axis('equal')
        plt.tight_layout()
        st.pyplot(fig)

with col2:
    st.markdown("### 📊 Listings by City")
    city_counts = filtered_df.groupby("city").size()

    if not city_counts.empty:
        st.bar_chart(city_counts)

st.markdown("---")


st.subheader("📈 Monthly Listings Trend")

if not filtered_df.empty:
    filtered_df["month"] = filtered_df.date_listed.dt.to_period("M")
    monthly = filtered_df.groupby("month").size()
    monthly.index = monthly.index.astype(str)
    st.line_chart(monthly)

st.markdown("---")


st.subheader("🗺️ Property Locations")

if "latitude" in filtered_df.columns and not filtered_df.empty:
    st.map(filtered_df[["latitude", "longitude"]])

st.markdown("---")


st.subheader("📑 Business Insights (15 SQL Queries)")

queries = {

"1. Average Price by City":
"SELECT city, AVG(price) FROM listings GROUP BY city",

"2. Highest Avg Price City":
"SELECT city, AVG(price) FROM listings GROUP BY city ORDER BY AVG(price) DESC LIMIT 1",

"3. Listings per City":
"SELECT city, COUNT(*) FROM listings GROUP BY city",

"4. Average Price by Property Type":
"SELECT property_type, AVG(price) FROM listings GROUP BY property_type",

"5. Most Common Property Type":
"SELECT property_type, COUNT(*) FROM listings GROUP BY property_type ORDER BY COUNT(*) DESC LIMIT 1",

"6. Top 5 Expensive Listings":
"SELECT * FROM listings ORDER BY price DESC LIMIT 5",

"7. Top 5 Cheapest Listings":
"SELECT * FROM listings ORDER BY price ASC LIMIT 5",

"8. Agent with Most Listings":
"SELECT agent_id, COUNT(*) FROM listings GROUP BY agent_id ORDER BY COUNT(*) DESC LIMIT 1",

"9. Average Price by Agent":
"SELECT agent_id, AVG(price) FROM listings GROUP BY agent_id",

"10. Listings per Month":
"SELECT strftime('%Y-%m', date_listed), COUNT(*) FROM listings GROUP BY 1",

"11. Highest Activity Month":
"SELECT strftime('%Y-%m', date_listed), COUNT(*) FROM listings GROUP BY 1 ORDER BY COUNT(*) DESC LIMIT 1",

"12. Average Price per Sqft":
"SELECT AVG(price / sqft) FROM listings",

"13. Highest Priced City":
"SELECT city, MAX(price) FROM listings GROUP BY city ORDER BY MAX(price) DESC LIMIT 1",

"14. Properties Above Avg Price":
"SELECT COUNT(*) FROM listings WHERE price > (SELECT AVG(price) FROM listings)",

"15. Total Market Value per City":
"SELECT city, SUM(price) FROM listings GROUP BY city ORDER BY SUM(price) DESC"
}

selected_query = st.selectbox("Select Business Question", list(queries.keys()))
result_df = pd.read_sql_query(queries[selected_query], conn)
st.dataframe(result_df)

conn.close()
