import pandas as pd 
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import tree
# Main Title
st.markdown("<h1 style='text-align: center; color: black;'>Simple Streamlit App</h1>", unsafe_allow_html=True)

# Some Text
st.write("Welcome to my app!")
st.write("We are going to explore a data frame with some visualizations and train a tree model on it!")
st.divider()

# Subtitle
st.header("Data Frame")
st.write("Data Frame about Kidney Disease Risk:")
# Reading the data
df=pd.read_csv("F:/kidney_disease_dataset.csv")
# Showing the data frame
st.dataframe(df)
st.divider()

# Subtitle
st.header("Checking for NULL Values")
null_values= pd.DataFrame(df.isnull().sum())
null_values.reset_index(inplace=True)
null_values.columns=["Features", "Count"]
# Showing the Null values as a table
st.dataframe(null_values)
st.divider()

# Customized palette
my_colors=sns.set_palette("cubehelix", n_colors=10)
sns.set_theme(style="dark", palette=my_colors)

# Subtitle
st.header("Exploratory Data Analysis")

choices= ("None", "Distributions Using Histogram", "Ralations Using Bar Plot",
            "Relations Using Scatter Plot", "Distributions of Count Plots")
# Select Box to choose from various options
selections=st.selectbox("Select the Mehtod Used for Visualizing the Data:", choices)

if selections == "Distributions Using Histogram":
    fig, axes=plt.subplots(1, 2)
    fig.suptitle("Distributions of Numerical Features")
    # First Figure
    sns.histplot(df["Age"], edgecolor="blue", kde=True, ax=axes[0])
    axes[0].set_title("Age Distribution")
    # Second Figure
    sns.histplot(df["Creatinine_Level"], edgecolor= "blue", kde=True, ax=axes[1])
    axes[1].set_title("Creatinine Level Distrtibution")
    fig.tight_layout()
    st.pyplot(fig)

elif selections == "Ralations Using Bar Plot":
    sns.barplot(data=df, x="Diabetes", y="Creatinine_Level", edgecolor= "red")
    plt.title("Relation Between Diabetes and Creatinine Level")
    st.pyplot(plt.gcf())

elif selections == "Relations Using Scatter Plot":
    sns.scatterplot(data=df, x="Age", y="GFR", edgecolor="red")
    plt.title("Relation Between Glomerular Filtration Rate and Age")
    st.pyplot(plt.gcf())

elif selections == "Distributions of Count Plots":
    # First Chart
    fig, axes=plt.subplots(1, 2)
    fig.suptitle("Counts of Categorical Features")
    sns.countplot(data=df, x="Diabetes", edgecolor="red", ax=axes[0])
    axes[0].set_title("Count of Peaple Who Have Diabetes")
    # Second Chart
    counts=df["Hypertension"].value_counts()
    axes[1].pie(counts, labels=counts.index, autopct='%1.1f%%')
    axes[1].set_title("Percentage of Peaple Who have Hypertension", fontsize=10)
    fig.tight_layout()
    st.pyplot(plt.gcf())

else:
    st.write("You Didn't Select Anything Yet!")
st.divider()

# Training the Model
x=df[["Age", "Creatinine_Level", "BUN", "Diabetes", "Hypertension", "GFR", "Urine_Output"]]
y=df["CKD_Status"]
model=tree.DecisionTreeClassifier()
model=model.fit(x, y)
# Subtitle
st.header("Classification Using a Tree Model")
# Some Text
st.write("In this section we will use a tree classifier and show the plot below using the button!")

# A method to center a button
col1, col2, col3, col4, col5=st.columns(5)
with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3:
    # A button to show the tree plot
    center=st.button("Tree Plot", type="primary")

if center:
    # The tree plot
    fig=plt.figure(figsize=(10, 10))
    tree.plot_tree(model, filled=True, class_names={0: "No Risk", 1: "Risk"},
                fontsize=12, feature_names=["Age", "Creatinine_Level", "BUN", "Diabetes", "Hypertension", "GFR", "Urine_Output"],
                rounded=True)
    st.pyplot(fig)
    st.divider()
    # Conclusion
    st.markdown("<h1 style='text-align: center; color: black;'>Thank You!</h1>", unsafe_allow_html=True)

