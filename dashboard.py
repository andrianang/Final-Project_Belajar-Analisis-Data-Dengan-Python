import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
import pandas as pd
import seaborn as sns

penjual_stats = pd.read_csv('penjual_stats.csv')
products_cat_stats = pd.read_csv('products_cat_stats.csv')
product_stats = pd.read_csv('product_stats.csv')
cust_order_stats = pd.read_csv('cust_order_stats.csv')
product_counts = pd.read_csv('product_counts.csv')
order_cust_items_prod_rev_sell_df = pd.read_csv('order_cust_items_prod_rev_sell_df.csv')
delivery_status_comparison = pd.read_csv('delivery_status_comparison.csv')
monthly_orders_df = pd.read_csv('monthly_orders_df.csv')


def plot_orders_per_month(data):
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(data["order_purchase_timestamp"], data["order_count"], marker='o', linewidth=2, color="#72BCD4")
    ax.set_title("Number of Orders per Month", loc="center", fontsize=20)
    ax.set_xticklabels(data["order_purchase_timestamp"], rotation=45, fontsize=10)
    ax.set_yticklabels(data["order_count"], fontsize=10)
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Number of Orders", fontsize=12)
    ax.grid(True)
    st.pyplot(fig)


def plot_seller_stats(data):
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x="num_orders", y="seller_id", data=data.sort_values(by="num_orders", ascending=False).head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("Seller with Most Sellings", loc="center", fontsize=15)
    ax[0].tick_params(axis ='y', labelsize=12)

    sns.barplot(x="total_payment", y="seller_id", data=data.sort_values(by="total_payment", ascending=False).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Seller with Most Gross Profit", loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)

    st.pyplot(fig)


def plot_category_stats(data):
    fig, ax = plt.subplots(figsize=(10, 5))

    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        y="num_products_sold",
        x="product_category_name_english",
        data=data.sort_values(by="num_products_sold", ascending=False).head(5),
        palette=colors,
        ax=ax
    )
    ax.set_title("Number of Transaction by Product Category", loc="center", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, fontsize=10)

    st.pyplot(fig)


def plot_product_stats(data):
    fig, ax = plt.subplots(figsize=(10, 5))

    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        y="average_review",
        x="product_id",
        data=data.sort_values(by=["num_products_sold", "num_review"], ascending=False).head(5),
        palette=colors,
        ax=ax
    )
    ax.set_title("Products with Best Review and Most Number of Reviews", loc="center", fontsize=15)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=12)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=90, fontsize=10)

    st.pyplot(fig)



def plot_customer_stats(cust_order_stats):
    cust_order_stats = cust_order_stats.reset_index()

    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

    colors = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(x="num_orders", y="customer_id", data=cust_order_stats.sort_values(by="num_orders", ascending=False).head(5), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title("Customers with Most Purchases", loc="center", fontsize=15)
    ax[0].tick_params(axis='y', labelsize=12)

    sns.barplot(x="total_payment", y="customer_id", data=cust_order_stats.sort_values(by="total_payment", ascending=False).head(5), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].invert_xaxis()
    ax[1].yaxis.set_label_position("right")
    ax[1].yaxis.tick_right()
    ax[1].set_title("Customer with Most Spendings", loc="center", fontsize=15)
    ax[1].tick_params(axis='y', labelsize=12)

    st.pyplot(fig)


def plot_place_comparison(same_state_counts, same_city_counts):
    plt.figure(figsize=(10, 6))

    plt.bar('Same', same_state_counts['Same'], color='lightgreen', label='Same State')
    plt.bar('Same', same_city_counts['Same'], color='skyblue', label='Same City')

    plt.bar('Not Same', same_city_counts['Not Same'], color='skyblue')
    plt.bar('Not Same', same_state_counts['Not Same'], color='lightgreen')

    plt.title('Counts of Same State and Same City', fontsize=16)
    plt.xlabel('Comparison', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title='Comparison')
    plt.tight_layout()

    st.pyplot(plt.gcf())


def plot_delivery_status_comparison(table):
    fig, ax = plt.subplots(figsize=(10, 6))

    table.plot(kind='bar', ax=ax, rot=0)

    plt.title('Delivery Status Comparison', fontsize=16)
    plt.xlabel('Delivery to Customer', fontsize=12)
    plt.ylabel('Count', fontsize=12)
    plt.xticks(range(len(table.index)), table.index)

    plt.legend(title='Delivery to Carrier')

    plt.tight_layout()

    st.pyplot(fig)



st.title('Dashboard E-Commerce Public Dataset')
tab1, tab2, tab3 = st.tabs(["Seller", "Product", "Customer"])
 
with tab1:
    st.header('Seller Analytics')
    st.subheader('Number of Orders per Month')

    plot_orders_per_month(monthly_orders_df)
    with st.expander("See explanation"):
        st.write(
            """Penjualan dari tahun 2016 hingga 2018 mengalami kenaikan yang signifikan (tidak termasuk pada bulan 9 tahun 2018, dikarenakan dataset tidak lagi tercatat). Namun, terdapat beberapa saat dimana penjualan mengalami penurunan
            . Hal ini dapat diakibatkan oleh beberapa faktor, seperti perubahan trend, persaingan, lingkungan, dan masih banyak lagi.""")
        

    st.subheader('Sales Statistics')
    plot_seller_stats(penjual_stats)
    with st.expander("See explanation"):
        st.write(
            """Pada selang tahun ini, seller telah memiliki penjualan terbanyak sejumlah 2133 pesanan, dengan pemasukan kotor sebanyak 301245.27 Peso.""")

with tab2:
    st.header('Product Analytics')
    st.subheader('Number of Transaction by Product Category')
    plot_category_stats(products_cat_stats)
    with st.expander("See explanation"):
        st.write(
            """Produk pada kategori 'bed_bath_table' cenderung dibeli oleh customer. Produk kategori ini merupakan produk dengan penjualan terbanyak mencapai 3638 pesanan.""")

    st.subheader('Products with Best Review and Most Number of Reviews')
    plot_product_stats(product_stats)
    with st.expander("See explanation"):
        st.write(
            """Pada selang tahun ini, produk yang paling laris adalah produk (id: aca2eb7d00ea1a7b8ebd4e68314663af) yang telah mencapai sebanyak 533 pesanan dengan rating 4. Produk ini berada pada kategori 'furniture_decor'.""")

with tab3:
    st.header('Customer Behaviour Analytics')
    st.subheader('Customers Spending Statistics')
    plot_customer_stats(cust_order_stats)
    with st.expander("See explanation"):
        st.write(
            """Sepanjang tahun 2016 hingga 2018, pelanggan dengan transaksi terbanyak sebanyak 63 (id: 270c23a11d024a44c896d1894b261a83). Namun, total spending dari satu pelanggan mencapai paling tinggi pada 45256 Peso dalam 20 transaksi.""")

    st.subheader('Customer\'s Preference in Choosing Seller') 
    same_state_counts = order_cust_items_prod_rev_sell_df['same_state'].value_counts()
    same_city_counts = order_cust_items_prod_rev_sell_df['same_city'].value_counts()
    plot_place_comparison(same_state_counts, same_city_counts)
    with st.expander("See explanation"):
        st.write(
            """Setelah dilakukan beberapa pengujian perilaku, diketahui bahwa kebanyakan customer melakukan transaksi pada toko yang berdomisili di luar kota customer.""")

    st.subheader('Customer\'s Experience') 
    plot_delivery_status_comparison(delivery_status_comparison)
    with st.expander("See explanation"):
        st.write(
            """Secara keseluruhan, pelanggan jarang menerima paket telat. Namun jika telat, pelanggan lebih sering mengalami keterlambatan paket yang sebagian besar dikarenakan oleh kurir yang telat mengirimkan paket kepada customer.""")


st.caption('Copyright (c) 2023')
