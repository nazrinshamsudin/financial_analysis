import yfinance as yf
import pandas as pd
import streamlit as st
import plotly.graph_objects as go
import wikipedia
from datetime import datetime, timedelta

# Home Page
def home_page():
    st.title("Welcome to the Home Page")
    st.write("This is the work of Nazrin Shamsudin, enjoy reading about stock prices.📖")

    st.subheader("What is the S&P 500?")
    st.image("sp 500 market size.jpeg", caption="S&P 500 Market Size", use_column_width=True)

   # Add the additional text to the home page
    st.write("The Standard & Poor’s 500 index, or S&P 500, is a collection of about 500 of the largest publicly traded companies in the U.S. It’s an ironic name for one of the best collections of stocks in the world, one that has returned investors about 10 percent annually over long periods of time.")
    st.write("Here are the details on the S&P 500, including its top holdings and long-term performance.")
    st.write("S&P 500 index: What companies are included?")
    st.write("The S&P 500 is perhaps the world’s most well-known stock index. The index contains about 500 of the largest publicly traded companies in the U.S., making it a bellwether for stocks. It includes stocks across all 11 sectors of the economy, as defined by the GICS classification system.")
    st.write("According to Standard & Poor’s, the index represents about 80 percent of the total value of all stocks trading in the U.S. markets. And the index is synonymous with the market as a whole. When people ask “how the market did today,” they’re often referring specifically to the S&P 500.")
    st.write("Tens of trillions of dollars are invested in the companies in the index, and investors can own those companies directly or buy a fund tracking the whole index. If they buy an index fund, they’ll get immediate diversified exposure to the hundreds of companies contained in the index.")
    st.write("For a company, it’s quite valuable to be included in the index. When a new firm is added to the S&P 500, all the funds tracking the index must rebalance their holdings. They’ll have to go into the market and buy the new stock joining the index and sell the old one leaving it. And when net new money is added to an S&P 500 index fund, the fund company must buy the stocks in it.")
    st.write("All that buying helps keep the stocks in the S&P 500 running high. A strong stock price makes it cheaper for a company to raise money by issuing new shares and generally makes the firm more attractive. So being added to the index is not only prestigious, it’s also financially valuable.")

        # Add more content for the home page if needed
        # Add the additional article
    st.subheader("How does a stock get added to the S&P 500?")
    st.write("Standard & Poor’s has strict criteria for being admitted into its flagship index, and companies are admitted, on a quarterly basis, if they fulfill the criteria (and may also be replaced and removed). Following the collapse of Silicon Valley Bank in March 2023, S&P Dow Jones Indices announced that medical device company Insulet (PODD) would replace SVB Financial Group in the S&P 500. The change was set to take effect March 15, 2023.")
    st.write("Here are the key requirements to make it into the index, as of January 2023:")
    st.write("- Must be a U.S. company.")
    st.write("- Must have a market capitalization of at least $8.2 billion and at least 50 percent of shares must be available (“floated”) on the exchange.")
    st.write("- Must be traded on a major U.S. exchange, including the New York Stock Exchange or Nasdaq.")
    st.write("- Companies must have positive earnings in the latest quarter and over the prior four quarters summed together.")
    st.write("- Must have traded at least 250,000 daily shares in the six months prior to inclusion.")
    st.write("Those are the most important criteria for inclusion, but Standard & Poor’s also considers how the inclusion of a stock maintains a balance of sectors for the index as a whole. Index managers want a collection of companies that give a representative picture of major American businesses.")

    st.subheader("The S&P 500 is a weighted index")
    st.write("The S&P 500 is an index that’s weighted according to the size of the companies in the index. The larger the company, the more heft it carries. The weightings rely on each firm’s market capitalization – the total value of its outstanding shares. A larger firm carries a larger weighting in the index, though Standard & Poor’s makes some adjustments based on how much of the stock is actually traded (“floated”) in the market (versus how much is held off the market.)")
    st.write("The price of the S&P 500 index that you see quoted – for example, 4,301.56 – is measured in points, not dollars. That’s the weighted average value of all the index’s components. As the component stocks move up or down, the index rises or falls according to the calculation.")
    st.write("Other popular indexes include the Dow Jones Industrial Average, which tracks 30 stocks across major sectors, and the Nasdaq Composite, which follows more than 3,000 companies on that exchange.")


    st.image("sp 500 by weight.png", caption="S&P 500 Market Size", use_column_width=True)
    st.subheader("What are the largest companies in the S&P 500?")
    st.write("The market’s largest companies are represented heavily in the index, and you’ll recognize some household names, including some of the popular FAANG stocks. Alphabet (parent of Google) has multiple classes of stock, so it appears in the list more than once.")
    st.write("The stocks are ranked by what percentage of the index they comprise (as of January 2023, according to data from Slickcharts), and this weighting changes over time as companies grow or shrink:")
    st.write("- Apple: 6.4 percent")
    st.write("- Microsoft: 5.4 percent")
    st.write("- Amazon: 2.7 percent")
    st.write("- Alphabet Class A: 1.7 percent")
    st.write("- Berkshire Hathaway Class B: 1.6 percent")
    st.write("- Alphabet Class C: 1.5 percent")
    st.write("- NVIDIA Corporation: 1.4 percent")
    st.write("- ExxonMobil: 1.4 percent")
    st.write("- United Healthgroup: 1.3 percent")
    st.write("- Tesla Inc: 1.3 percent")
    st.write("It’s worth noting that these 10 stocks alone make up about 25 percent of the total value of the index. The other 490 or so stocks represent the remaining 75 percent of the index’s value. So, the S&P 500 is heavily weighted to its largest components, and the largest stocks have market caps in the trillions, literally more than 100 times the minimum to be admitted into the index.")

    st.subheader("The S&P 500 has been a great investment over the years")
    st.write("The S&P 500 is the most followed stock index in the world and one of the most successful as well. Over time the index has returned about 10 percent annually on average. But over the last decade it’s done even better than that, due in large part to the strength of tech companies such as Amazon, Apple and Microsoft.")
    st.write("Here’s the S&P 500’s performance over the last 10 years, to January 26, 2023, and its average annual performance and total performance over four time periods:")
    st.write("Time\t1 year\t3 years\t5 years\t10 years")
    st.write("Annualized return\t-6.7 percent\t7.2 percent\t7.2 percent\t10.4 percent")
    st.write("Total return\t-6.7 percent\t23.2 percent\t41.3 percent\t170.2 percent")
    st.write("Source: Yahoo Finance")
    st.write("This kind of consistently strong performance as well as broad diversification are reasons legendary investor Warren Buffett recommends that individual investors buy an S&P 500 index fund, hold on through thick and thin, and ideally add more money to their position over time.")
    st.write("It’s remarkably easy to buy an S&P 500 index fund, and the best index funds offer a low-cost way to own the whole index, often charging just a few dollars for every $10,000 invested.")


    st.subheader("Bottom line")
    st.write("The S&P 500 index tracks hundreds of the largest and most successful American companies, giving investors a way to measure the performance of American business. It’s also a solid basis for funds, allowing investors to capture the index’s attractive returns in a low-cost vehicle.")
    st.write("Editorial Disclaimer: All investors are advised to conduct their own independent research into investment strategies before making an investment decision. In addition, investors are advised that past investment product performance is no guarantee of future price appreciation.")


# Function to fetch company data
def fetch_company_data(tickers, period):
    try:
        data = yf.download(tickers, period=period, interval="1d", rounding=True, threads=True)
        return data
    except KeyError:
        print(f"No data found for tickers: {tickers}")
        return None



# Dashboard Page
def dashboard_page():
    st.title("Financial Analysis Dashboard")
    st.write("This is the work of Nazrin Shamsudin, enjoy the analysis of stock prices.🙂")

    # Load S&P 500 tickers
    sp500_table = wikipedia.page("List_of_S&P_500_companies").html().encode("UTF-8")
    df = pd.read_html(sp500_table)[0]
    sp500_tickers = df["Symbol"].tolist()

    selected_tickers = ["AAPL", "MSFT", "AMZN", "GOOGL", "NVDA"]
    selected_period = '1y'
    selected_tickers.append("SPY")

    
    selected_tickerlist = st.sidebar.multiselect("Select Tickers", sp500_tickers, ["AAPL", "MSFT", "AMZN", "GOOGL", "META", "NVDA", "TSLA"])

    # Fetch SPY data
    spy_data = fetch_company_data("SPY", f"{selected_period}y")

    # Sidebar Settings
    st.sidebar.header("Settings")
    selected_period = st.sidebar.slider("Select Period (Years)", min_value=1, max_value=7, value=5)
   

    # Append "SPY" to the selected_tickerlist
    if "SPY" not in selected_tickerlist:
        selected_tickerlist.append("SPY")

    # Fetch and display SPY data separately
    if selected_tickerlist:
        spy_data = fetch_company_data("SPY", period=f"{selected_period}y")
        if spy_data is not None:
            st.subheader("SPY Stock Data")
            spy_data['Return'] = spy_data["Close"] - spy_data["Open"]
            spy_data['Return%'] = (spy_data["Close"] - spy_data["Open"]) / spy_data['Open'] * 100
            st.dataframe(spy_data)

    # Fetch and display selected companies data
    selected_data = fetch_company_data(selected_tickerlist, period=f"{selected_period}y")
    if selected_data is not None:
        st.subheader("Selected Companies Data")
        st.dataframe(selected_data)

    # Calculate correlation and covariance_matrix
    if selected_data is not None:
        selected_data_returns = selected_data['Adj Close'].pct_change()
        selected_data_returns.dropna(inplace=True)
        correlation_matrix = selected_data_returns.corr()
        covariance_matrix = selected_data_returns.cov()
        spy_covariance = covariance_matrix.loc['SPY', 'SPY']
        print(spy_covariance)
        

    # Create a correlation heatmap
    st.subheader("Correlation Table")
    st.dataframe(correlation_matrix.style.background_gradient(cmap='coolwarm'))

    # Create a covariance heatmap
    st.subheader("Covariance Table")
    st.dataframe(covariance_matrix.style.background_gradient(cmap='coolwarm'))

    # Create a DataFrame for covariance and correlation data
    cov_corr_data = []
    for ticker in selected_tickerlist:
        correlation = correlation_matrix.loc[ticker, "SPY"]
        covariance = covariance_matrix.loc[ticker, "SPY"]
        cov_corr_data.append({"Ticker": ticker, "Covariance with SPY": covariance, "Correlation with SPY": correlation})
    sorted_cov_corr_df = pd.DataFrame(cov_corr_data)

    
    # Calculate scaled covariance
    sorted_cov_corr_df['Scaled Covariance'] = sorted_cov_corr_df['Covariance with SPY'] / spy_covariance

    # Convert the columns to numeric types
    sorted_cov_corr_df['Correlation with SPY'] = pd.to_numeric(sorted_cov_corr_df['Correlation with SPY'])
    sorted_cov_corr_df['Scaled Covariance'] = pd.to_numeric(sorted_cov_corr_df['Scaled Covariance'])

    # Sort the DataFrame in descending order of both Correlation and Scaled Covariance
    sorted_cov_corr_df = sorted_cov_corr_df.sort_values(by=['Correlation with SPY', 'Scaled Covariance'], ascending=[False, False])

    # Display the sorted DataFrame in a table with numbered index to the left of the sidebar
    st.sidebar.subheader("Top 10 Tickers with Correlation and Covariance")
    st.sidebar.table(sorted_cov_corr_df[['Ticker', 'Correlation with SPY', 'Scaled Covariance']].head(20))



    # # Calculate scaled covariance
    # sorted_cov_corr_df['Scaled Covariance'] = sorted_cov_corr_df['Covariance with SPY'] / spy_covariance
    # cov_cor_df = pd.DataFrame(cov_corr_data)

    # print(sorted_cov_corr_df['Scaled Covariance'])
    # print(sorted_cov_corr_df)

    # # Display the sorted DataFrame in a table with numbered index
    # st.subheader("Top 10 Tickers with Correlation and Covariance")
    # st.table(sorted_cov_corr_df[['Ticker', 'Correlation with SPY', 'Covariance with SPY']].head(10))

    # Create the scatter plot using Plotly Go
    scatter_fig = go.Figure()

    for ticker, scaled_covariance, correlation in zip(
        sorted_cov_corr_df["Ticker"],
        sorted_cov_corr_df["Scaled Covariance"],
        sorted_cov_corr_df["Correlation with SPY"]
    ):
        scatter_fig.add_trace(go.Scatter(
            x=[correlation],
            y=[scaled_covariance],
            mode='markers',
            marker=dict(size=15),
            text=[f"{ticker} (Cov: {scaled_covariance:.6f}, Corr: {correlation:.2f})"],
            hoverinfo='text',
            name=ticker
        ))

        scatter_fig.add_annotation(
            x=correlation,
            y=scaled_covariance,
            xshift=-24,
            text=ticker,
            showarrow=False
        )

    # Update scatter plot layout
    scatter_fig.update_layout(
        title="Covariance vs Correlation (SPY as a Benchmark)",
        xaxis_title="Correlation",
        yaxis_title="Covariance",
        template="plotly_white",
    )

    # Display the scatter plot
    st.plotly_chart(scatter_fig)












def graph_plot_analysis():

    import yfinance as yf
    import pandas as pd
    import wikipedia
    import streamlit as st
    import plotly.graph_objects as go

    # Function to fetch company data
    def fetch_company_data(tickers, period):
        try:
            data = yf.download(tickers, period=period, interval="1d", rounding=True, threads=True)
            return data
        except ValueError:
            st.error(f"No data found for tickers: {tickers}")
            return None

    # Function to fetch SPY data
    def fetch_spy_data(period):
        try:
            data = yf.download('SPY', period=period, interval="1d", rounding=True, threads=True)
            return data
        except ValueError:
            st.error("No data found for SPY")
            return None

    # Function to calculate correlation and covariance
    def calculate_correlation_and_covariance(data):
        correlation_matrix = data.corr()
        covariance_matrix = data.cov()
        return correlation_matrix, covariance_matrix

    # Function to calculate return
    def calculate_return(data_frame, ticker):
        return data_frame[("Close", ticker)] - data_frame[("Open", ticker)]

    # Function to calculate return percent
    def calculate_return_percent(data_frame, ticker):
        return (data_frame[("Close", ticker)] - data_frame[("Open", ticker)]) / data_frame[("Open", ticker)] * 100  


        # Function to create a scatter plot
    def create_scatter_plot(data, selected_tickers, num_data_points, spy_data):
        scatter_fig = go.Figure()

        spy_covariance = data['Close']['SPY'].cov(spy_data['Close'])

        for ticker in selected_tickers:
            correlation = data['Close'][ticker].corr(data['Close']['SPY'])
            covariance = data['Close'][ticker].cov(data['Close']['SPY'])
            scaled_covariance = covariance / spy_covariance

            scatter_fig.add_trace(go.Scatter(
                x=[correlation],
                y=[scaled_covariance],
                mode='markers',
                marker=dict(size=15),
                text=[f"{ticker} (Cov: {scaled_covariance:.6f}, Corr: {correlation:.2f})"],
                hoverinfo='text',
                name=ticker
            ))

            scatter_fig.add_annotation(
                x=correlation,
                y=scaled_covariance,
                xshift=-24,
                text=ticker,
                showarrow=False
            )

        # Update scatter plot layout
        scatter_fig.update_layout(
            title="Scaled Covariance vs Correlation (SPY as a Benchmark)",
            xaxis_title="Correlation",
            yaxis_title="Scaled Covariance",
            template="plotly_white",
        )

        return scatter_fig


    # Fetch the list of S&P 500 companies
    sp500_table = wikipedia.page("List_of_S&P_500_companies").html().encode("UTF-8")
    df = pd.read_html(sp500_table)[0]
    sp500_tickers = df["Symbol"].tolist()

    # Define the selected tickers (initially)
    selected_tickers = ["AAPL", "MSFT", "GOOGL", "NVDA"]

    # Streamlit App
    st.title("S&P 500 Data Graph Analysis")
    st.sidebar.header("Settings")
    # Create a sidebar multi-select widget to select tickers (excluding SPY)
    selected_tickers = st.multiselect("Select Tickers (excluding SPY)", sp500_tickers, selected_tickers)

    # Create a sidebar number input with plus and minus buttons for the number of data points
    num_data_points = st.sidebar.number_input("Select Number of Recent Days", min_value=1, step=1, value=1)

    # Allow the user to input a custom period
    custom_period = st.sidebar.text_input("Custom Period (e.g., '30d', '3mo', '1y')", '7d')

    

    # Append "SPY" to the selected_tickers
    if "SPY" not in selected_tickers:
        selected_tickers.append("SPY")

    # Fetch data for selected tickers and custom period
    company_data = fetch_company_data(selected_tickers, custom_period)
    spy_data = fetch_spy_data(custom_period)

    # Display the selected data in a table format with magma color gradient
    if company_data is not None and spy_data is not None:
        st.subheader(f"Data table for {num_data_points} Recent Days")
        st.dataframe(company_data.tail(num_data_points).style.background_gradient(cmap='magma'))
        
        # Calculate correlation and covariance
        correlation_matrix, covariance_matrix = calculate_correlation_and_covariance(company_data)
        


        tab_labels = ["Correlation Matrix", "Covariance Matrix"]
        tabs = st.tabs(tab_labels)


        with tabs[0]:
            # Display correlation matrix heatmap
            st.subheader("Correlation Matrix")
            st.dataframe(correlation_matrix.style.background_gradient(cmap='viridis'))
            
        with tabs[1]:
            # Display covariance matrix heatmap
            st.subheader("Covariance Matrix")
            st.dataframe(covariance_matrix.style.background_gradient(cmap='jet'))
        
        # Create and display the scatter plot
        scatter_fig = create_scatter_plot(company_data, selected_tickers, num_data_points, spy_data)
        st.plotly_chart(scatter_fig)
        
        # Create return and return% tables
        return_data = {}
        for ticker in selected_tickers:
            return_col = f'{ticker}_Return'
            return_percent_col = f'{ticker}_Return%'
            
            return_data[return_col] = calculate_return(company_data, ticker)
            return_data[return_percent_col] = calculate_return_percent(company_data, ticker)

        return_df = pd.DataFrame(return_data)
        
        # Create nested columns and rows for layout
        col1, col2 = st.columns(2)

        with col1:
            for ticker in selected_tickers[::2]:  # Display first table of each pair
                return_col = f'{ticker}_Return'
                return_percent_col = f'{ticker}_Return%'
                
                st.subheader(f"{ticker} Stock Data")
                st.dataframe(return_df[[return_col, return_percent_col]])

        with col2:
            for ticker in selected_tickers[1::2]:  # Display second table of each pair
                return_col = f'{ticker}_Return'
                return_percent_col = f'{ticker}_Return%'
                
                st.subheader(f"{ticker} Stock Data")
                st.dataframe(return_df[[return_col, return_percent_col]])
    else:
        st.warning("No data available for the selected tickers and period.")








    import requests
    import streamlit as st
    import folium
    from streamlit_folium import folium_static

    def get_coordinates(location_name):
        base_url = "https://nominatim.openstreetmap.org/search"
        params = {
            "format": "json",
            "q": location_name,
            "limit": 1  # Limit to 1 result
        }
        response = requests.get(base_url, params=params)
        data = response.json()
        
        if data:
            return float(data[0]["lat"]), float(data[0]["lon"])
        else:
            return None, None
        

    def display_company_maps():
        selected_companies = ["META", "Google", "Microsoft", "Apple", "Tesla", "AMAZON", "NVIDIA", "NASDAQ"]
 
        st.header("Company Headquarters Geolocations")


            
        for company in selected_companies:
            with st.expander(f"{company} Headquarters"):
                if company == "NVIDIA":
                    # Manually set coordinates for Nvidia
                    latitude, longitude = 37.3691, -121.9582
                elif company == "AMAZON":
                    # Manually set coordinates for Amazon
                    latitude, longitude = 47.6061, -122.3328
                elif company == "NASDAQ":
                    latitude, longitude = 40.7128, -74.0060
                else:
                    # Get company coordinates using the get_coordinates function
                    latitude, longitude = get_coordinates(f"{company} headquarters")

                if latitude is not None and longitude is not None:
                    company_location = (latitude, longitude)
                    company_map = folium.Map(location=company_location, zoom_start=10)
                    folium.Marker(location=company_location, popup=company).add_to(company_map)

                    # Display the map in a tab
                    folium_static(company_map, width=600, height=300)  # Adjust width and height as needed
                else:
                    st.subheader(f"Coordinates not found for {company}")

    if __name__ == "__main__":
        display_company_maps()

   



def time_series_forecasting():
    st.write("This is the work of Nazrin Shamsudin, enjoy the forecasting of stock prices.🙂")



# Sidebar Settings
st.sidebar.header("Navigation")
selected_page = st.sidebar.radio("Select Page", ("Home", "Dashboard", "Graph Plot Analysis", "Time Series Forecasting"))

# Display content based on the selected page
if selected_page == "Home":
    home_page()
elif selected_page == "Dashboard":
    dashboard_page()
elif selected_page == "Graph Plot Analysis":
    graph_plot_analysis()
elif selected_page == "Time Series Forecasting":
    time_series_forecasting()
