import pandas as pd
from django.shortcuts import render
from .dashboard import (
    frequency_table,
    full_dataset_table,
    describe_table,
    group_by_selling_price,
    pivot_table_analysis,
    crosstab_analysis,
    aggre_func,
    sunburst_chart,
    treemap_chart,
    y3c,
    visualizing_clients_world_map  
)


def dashboard_view(request):
    df = pd.read_csv("dummy_data/vehicles_data_1000.csv")

    return render(request, "vehicles/index.html", {
        "":y3c(df),
        "manufacturer_frequency_table": frequency_table(df),
        "dataset_table": full_dataset_table(df),
        "description_table": describe_table(df),
        "groupby_table": group_by_selling_price(df),
        "pivot_table": pivot_table_analysis(df),
        "crosstab_table": crosstab_analysis(df),
        "aggregate_table": aggre_func(df),
        "sunburst_div": sunburst_chart(df),
        "treemap_div": treemap_chart(df),
        "world_map_div": visualizing_clients_world_map(df)
    })