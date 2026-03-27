import statistics

MAJOR_BOOKS = ["BookA", "BookB", "BookC", "BookD", "BookE"]


def fetch_odds():
    odds = []
    for book in MAJOR_BOOKS:
        # Simulate fetching odds from each book
        odds.append(get_odds_from_book(book))
    
    # Calculate median odds across all sportsbooks
    median_odds = statistics.median(odds)
    return median_odds


def get_odds_from_book(book):
    # Placeholder for getting odds from a specific book
    # In practice, this function would make a network request to get current odds.
    return 100 + hash(book) % 10  # Simulated odds
