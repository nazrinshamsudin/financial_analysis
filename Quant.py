import streamlit as st

# Define the navigation options with emoji icons
navigation_options = {
    "📊 Company Data Analysis": "Company Data Analysis",
    "📈 Financial Analysis Dashboard": "Financial Analysis Dashboard"
}

# Create a sidebar text input for navigation
selected_page = st.sidebar.selectbox("Navigation", list(navigation_options.keys()), index=0)

# Use the selected_page to determine the chosen option
chosen_option = navigation_options[selected_page]

# Define the functions for the two pages
def financial_analysis_dashboard():
    import yfinance as yf
    import pandas as pd
    import streamlit as st
    import plotly.graph_objects as go
    import wikipedia
    from datetime import datetime, timedelta

    # Your code for the Company Data Analysis page here
    # Dashboard Page
    st.title("Financial Dashboard Analysis")
    st.write("This is the work of Nazrin Shamsudin, enjoy the analysis of stock prices.🙂")

        # Function to fetch company data
    def fetch_company_data(tickers, period):
        try:
            data = yf.download(tickers, period=period, interval="1d", rounding=True, threads=True)
            return data
        except KeyError:
            print(f"No data found for tickers: {tickers}")
            return None


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
    st.sidebar.subheader("Top Tickers with Correlation and Covariance")
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
            text=[f"{ticker} (Cov: {scaled_covariance:.2f}, Corr: {correlation:.2f})"],
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











def company_data_analysis():

    import yfinance as yf
    import pandas as pd
    import wikipedia
    import streamlit as st
    import plotly.graph_objects as go

    # Function to fetch company data
    def fetch_company_data(tickers, period, num_data_points):
        try:
            data = yf.download(tickers, period=period, interval="1d", rounding=True, threads=True)
            return data
        except ValueError:
            st.error(f"No data found for tickers: {', '.join(tickers)}")
            return None

    # Function to calculate return
    def calculate_return(data_frame, ticker):
        return data_frame[("Close", ticker)] - data_frame[("Open", ticker)]

    # Function to calculate return percentage
    def calculate_return_percent(data_frame, ticker):
        return (data_frame[("Close", ticker)] - data_frame[("Open", ticker)]) / data_frame[("Open", ticker)] * 100

    # Function to fetch SPY data
    def fetch_spy_data(period, num_data_points):
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

    # Function to create a scatter plot
    def create_scatter_plot(data, cov_corr_df, selected_tickers, num_data_points, spy_data):
        data = data.tail(num_data_points)
        scatter_fig = go.Figure()

        for ticker in selected_tickers:
            
            correlation = cov_corr_df.loc[cov_corr_df['Ticker'] == ticker, 'Correlation'].values[0]

            scaled_covariance = cov_corr_df.loc[cov_corr_df['Ticker'] == ticker, 'Scaled Covariance'].values[0]

            scatter_fig.add_trace(go.Scatter(
                x=[correlation],
                y=[scaled_covariance],
                mode='markers',
                marker=dict(size=15),
                text=[f"{ticker} (Scaled Cov: {scaled_covariance:.2f}, Corr: {correlation:.2f})"],
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
            yaxis_title="Covariance",
            template="plotly_white",
        )

        return scatter_fig

    # Function to update data based on the selected number of days and custom period
    def update_data(num_data_points, custom_period):
        
        # Fetch data for selected tickers and custom period
        company_data = fetch_company_data(selected_tickers, custom_period, num_data_points)
        spy_data = fetch_spy_data(custom_period, num_data_points)

        # Calculate correlation and covariance
        company_data_returns = company_data["Close"].pct_change()
        company_data_returns.dropna(inplace=True)
        correlation_matrix, covariance_matrix = calculate_correlation_and_covariance(company_data_returns)
        spy_covariance = covariance_matrix.loc['SPY', 'SPY']

        # Create a DataFrame for covariance and correlation data
        cov_corr_data = []
        for ticker in selected_tickers:
            correlation = correlation_matrix.loc[ticker, "SPY"]
            covariance = covariance_matrix.loc[ticker, "SPY"]
            cov_corr_data.append({"Ticker": ticker, "Covariance with SPY": covariance, "Correlation": correlation})
        cov_corr_df = pd.DataFrame(cov_corr_data)

        # Calculate scaled covariance
        cov_corr_df['Scaled Covariance'] = cov_corr_df['Covariance with SPY'] / spy_covariance

        # Sort the DataFrame by scaled covariance in descending order
        cov_corr_df = cov_corr_df.sort_values(by='Scaled Covariance', ascending=False)

        # Display the top 10 tickers in the sidebar with scaled covariance and correlation values
        st.sidebar.subheader("Top Tickers by Correlation and Scaled Covariance")
        top_ticker_table = st.sidebar.empty()  # Create an empty placeholder for the table

        if top_ticker_table.button("Refresh Top Tickers"):  # Add a "Refresh" button
            top_ticker_data = cov_corr_df.head(10)[['Ticker', 'Correlation', 'Scaled Covariance']]
            top_ticker_table.dataframe(top_ticker_data)
        else:
            top_ticker_table.dataframe(cov_corr_df.head(10)[['Ticker', 'Correlation', 'Scaled Covariance']])


        # Create return and return% tables
        return_data = {}
        for ticker in selected_tickers:
            return_col = f'{ticker}_Return'
            return_percent_col = f'{ticker}_Return%'
            
            return_data[return_col] = calculate_return(company_data, ticker)
            return_data[return_percent_col] = calculate_return_percent(company_data, ticker)

        return_df = pd.DataFrame(return_data)






        # Create a scatter plot
        scatter_fig = create_scatter_plot(company_data, cov_corr_df, selected_tickers, num_data_points, spy_data)

        # Display the selected data in a table format with magma color gradient
        if company_data is not None and spy_data is not None:
            st.subheader(f"Data table for {num_data_points} Recent Days")
            st.dataframe(company_data.tail(num_data_points).style.background_gradient(cmap='magma'))

            # Print selected DataFrame into a table
            st.subheader("Selected Company DataFrame")
            st.dataframe(company_data["Close"].tail(num_data_points).style.background_gradient(cmap='plasma'))

            correlation_matrix_scaled = correlation_matrix
            covariance_matrix_scaled = covariance_matrix

            tab_labels = ["Correlation Table", "Covariance Table"]
            tabs = st.tabs(tab_labels)

            with tabs[0]:
                st.subheader("Correlation Table")
                st.dataframe(correlation_matrix_scaled.style.background_gradient(cmap='viridis'))

            with tabs[1]:
                st.subheader("Covariance Table")
                st.dataframe(covariance_matrix_scaled.style.background_gradient(cmap='jet'))

            # Update scatter plot layout
            scatter_fig.update_layout(
                title="Scaled Covariance vs Correlation (SPY as a Benchmark)",
                xaxis_title="Correlation",
                yaxis_title="Covariance",
                template="plotly_white",
            )

            # Display the scatter plot in your Streamlit app
            st.plotly_chart(scatter_fig)


            # Display return and return% tables in two columns
        st.subheader("Return and Return%")
        
        col1, col2 = st.columns(2)
        for ticker in selected_tickers:
            return_col = f'{ticker}_Return'
            return_percent_col = f'{ticker}_Return%'
            
            if selected_tickers.index(ticker) % 2 == 0:
                with col1:
                    st.subheader(f"{ticker} Stock Data")
                    st.dataframe(return_df[[return_col, return_percent_col]].tail(num_data_points))
            else:
                with col2:
                    st.subheader(f"{ticker} Stock Data")
                    st.dataframe(return_df[[return_col, return_percent_col]].tail(num_data_points))


    # Fetch the list of S&P 500 companies
    sp500_table = wikipedia.page("List_of_S&P_500_companies").html().encode("UTF-8")
    df = pd.read_html(sp500_table)[0]
    sp500_tickers = df["Symbol"].tolist()

    # Define the selected tickers (initially)
    selected_tickers = ["AAPL", "MSFT", "AMZN", "GOOGL", "NVDA", "META", "AMD", "JPM", "ADBE", "CSCO", "INTC", "QCOM", "SBUX", "MCD", "XOM", "WMT"]

    # Streamlit App
    st.title("S&P 500 Company Data Analysis")
    st.write("This is the work of Nazrin Shamsudin, enjoy the analysis of stock prices.💸")
    st.sidebar.header("Settings")

    # Create a sidebar multi-select widget to select tickers (excluding SPY)
    selected_tickers = st.multiselect("Select Tickers (excluding SPY)", sp500_tickers, selected_tickers)

    # Allow the user to input a custom period
    custom_period = st.sidebar.text_input("Custom Period (Example: 7d, 5mo, 1y)", '7d')

    # Create a sidebar number input with plus and minus buttons for the number of data points
    num_data_points = st.sidebar.number_input("Select Number of Recent Days", min_value=1, step=1, value=1)

    # Append "SPY" to the selected_tickers
    if "SPY" not in selected_tickers:
        selected_tickers.append("SPY")

    # Call the update_data function with the current number of data points and custom period
    update_data(num_data_points, custom_period)





# Use a dictionary to map the selected option to the corresponding function
page_mapping = {
    "Company Data Analysis": company_data_analysis,
    "Financial Analysis Dashboard": financial_analysis_dashboard,
}

# Call the selected function based on the user's choice
page_mapping[chosen_option]()