import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

def main():
    st.title('3D Plot Visualization')
    
    # Load the dataset into a DataFrame
    df = pd.read_csv("WomensClothingE-CommerceReviews.csv")  # Replace "your_dataset.csv" with the path to your dataset file
    
    # Create a 3D scatter plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    # Scatter plot with different colors
    colors = np.random.rand(len(df))
    sc = ax.scatter(df['Age'], df['Rating'], df['Positive Feedback Count'], c=colors, cmap='viridis', marker='o', label='Data Points')
    
    # Set labels and title
    ax.set_xlabel('Age')
    ax.set_ylabel('Rating')
    ax.set_zlabel('Positive Feedback Count')
    ax.set_title('Relationship between Age, Rating, and Positive Feedback Count')
    
    # Add a color bar
    cbar = fig.colorbar(sc)
    cbar.set_label('Color')
    
    # Add legend
    ax.legend()
    
    # Display the plot in Streamlit
    st.pyplot(fig)

if __name__ == "__main__":
    main()
