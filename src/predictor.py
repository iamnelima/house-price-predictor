import pandas as pd
import pickle

class ApartmentPricePredictor:
    def __init__(self, data_path):
        """Load the apartment data"""
        self.df = pd.read_csv(data_path)

    def predict(self, bedrooms, bathrooms, location):
        """
        Predict apartment price based on similar apartments

        Returns: (predicted_price, count, method_used)
        """
        # Find exact matches
        similar = self.df[
            (self.df['bedrooms'] == bedrooms) &
            (self.df['bathrooms'] == bathrooms) &
            (self.df['location'] == location)
        ]

        if len(similar) > 0:
            return similar['price'].mean(), len(similar), "Exact match"

        # Find similar bed/bath in any location
        similar_bb = self.df[
            (self.df['bedrooms'] == bedrooms) &
            (self.df['bathrooms'] == bathrooms)
        ]

        if len(similar_bb) > 0:
            return similar_bb['price'].mean(), len(similar_bb), "Similar apartments"

        # Fallback to bedroom average
        similar_bed = self.df[self.df['bedrooms'] == bedrooms]
        if len(similar_bed) > 0:
            return similar_bed['price'].mean(), len(similar_bed), f"{bedrooms}BR average"

        return self.df['price'].mean(), len(self.df), "Overall average"

    def get_available_locations(self):
        """Get list of all locations in dataset"""
        return sorted(self.df['location'].unique())

# Test
if __name__ == "__main__":
    predictor = ApartmentPricePredictor('C:/Users/HP/house-price-predictor/data/processed/apartments_clean.csv')

    price, count, method = predictor.predict(3, 4, 'Kileleshwa, Nairobi')
    print(f"Prediction: {price:,.0f} KES/month")
    print(f"Based on: {count} apartments ({method})")