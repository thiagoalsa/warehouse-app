import pandas as pd


# Create a Pandas DataFrame
images = pd.read_csv('/Users/thiagosantos/Desktop/dados warehouse/images.csv')

style = pd.read_csv('/Users/thiagosantos/Desktop/dados warehouse/styles.csv', on_bad_lines='skip')

# Add images link on style DataFrame

style['link'] = images['link']
