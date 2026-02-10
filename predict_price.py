from src.predictor import ApartmentPricePredictor

def main():
    print("=" * 60)
    print("KENYA APARTMENT PRICE PREDICTOR")
    print("=" * 60)

    # Initialize predictor
    predictor = ApartmentPricePredictor('data/processed/apartments_clean.csv')

    # Get user input
    print("\nEnter apartment details:")
    bedrooms = int(input("Number of bedrooms: "))
    bathrooms = int(input("Number of bathrooms: "))

    # Show available locations
    print("\nSome popular locations:")
    locations = predictor.get_available_locations()
    for i, loc in enumerate(locations[:10], 1):
        print(f"  {i}. {loc}")
    print("  ... and more")

    location = input("\nEnter location (exactly as shown): ")

    # Make prediction
    price, count, method = predictor.predict(bedrooms, bathrooms, location)

    # Display result
    print("\n" + "=" * 60)
    print("PREDICTION RESULT")
    print("=" * 60)
    print(f"Apartment: {bedrooms} bedrooms, {bathrooms} bathrooms")
    print(f"Location: {location}")
    print(f"\nEstimated Price: {price:,.0f} KES/month")
    print(f"Confidence: Based on {count} similar apartments ({method})")
    print("=" * 60)

if __name__ == "__main__":
    main()