import plotly.express as px
import plotly.offline as opy
import pandas as pd

def y3c(df):
    df.groupby("manufacturer").agg({
        "selling_price": "mean"
    })

    return df.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center")



# 1️⃣ Frequency Table
def frequency_table(df):
    manufacturer_counts = df['manufacturer'].value_counts().reset_index()
    manufacturer_counts.columns = ['Manufacturer', 'Count']

    return manufacturer_counts.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center",
        index=False
    )


# 2️⃣ Full Dataset
def full_dataset_table(df):
    return df.to_html(
        classes="table table-hover table-striped table-bordered align-middle",
        index=False
    )


# 3️⃣ Describe Table
def describe_table(df):
    description = df.describe(include='all')

    return description.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center",
        float_format="%.2f"
    )


# 4️⃣ Group By Selling Price
def group_by_selling_price(df):
    new_df = df.copy()
    new_df['profit'] = new_df['selling_price'] - new_df['wholesale_price']
    new_df['profit_or_loss'] = new_df['profit'].apply(
        lambda x: 'Profit' if x > 0 else ('Loss' if x < 0 else 'Break-even')
    )

    grouped = new_df.groupby(
        ["manufacturer", "body_type", "transmission"]
    ).agg({
        "selling_price": ["min","max", "sum"],
        "wholesale_price": ["sum"],
        "profit": ["sum"],
       
    })

    return grouped.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center",
        
    )


# 5️⃣ Pivot Table
def pivot_table_analysis(df):
    pivot = pd.pivot_table(
        df,
        values="selling_price",
        index="manufacturer",
        columns="fuel_type",
        aggfunc="mean"
    ).round(2)

    return pivot.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center"
    )


# 6️⃣ Cross Tabulation
def crosstab_analysis(df):
    cross_tab = pd.crosstab(
        df["manufacturer"], df["body_type"], values=df["selling_price"],aggfunc=["sum",get_range]
    )

    return cross_tab.to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center"
    )


# 7️⃣ Aggregate Function
def aggre_func(df):
    return df.groupby(["manufacturer", "body_type"]).agg({
        "selling_price": ["mean", "min", "max"],
        "wholesale_price": ["mean", "min", "max"]
    }).to_html(
        classes="table table-hover table-striped table-bordered align-middle text-center"
    )


# 8️⃣ Sunburst Chart
def sunburst_chart(df):
    df_copy = df.copy()
    df_copy['profit'] = df_copy['selling_price'] - df_copy['wholesale_price']
    df_copy['profit_or_loss'] = df_copy['profit'].apply(
        lambda x: 'Profit' if x > 0 else ('Loss' if x < 0 else 'Break-even')
    )

    fig = px.sunburst(
        df_copy,
        path=['manufacturer', 'fuel_type', 'transmission', 'profit_or_loss'],
        values='selling_price',
        color='profit',
        color_continuous_scale='RdYlGn',
        title="Sunburst: Manufacturer → Fuel → Transmission → Profit/Loss",
        hover_data=['selling_price', 'wholesale_price', 'profit']
    )

    div = opy.plot(fig, auto_open=False, output_type='div')
    return div


# 9️⃣ Treemap Chart
def treemap_chart(df):
    df_copy = df.copy()
    df_copy['profit'] = df_copy['selling_price'] - df_copy['wholesale_price']
    df_copy['profit_or_loss'] = df_copy['profit'].apply(
        lambda x: 'Profit' if x > 0 else ('Loss' if x < 0 else 'Break-even')
    )

    fig = px.treemap(
        df_copy,
        path=['manufacturer', 'fuel_type', 'transmission', 'profit_or_loss'],
        values='selling_price',
        color='profit',
        color_continuous_scale='RdYlGn',
        title="Treemap: Manufacturer → Fuel → Transmission → Profit/Loss",
        hover_data=['selling_price', 'wholesale_price', 'profit']
    )

    div = opy.plot(fig, auto_open=False, output_type='div')
    return div