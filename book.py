class Book:
    def __init__(self, title, author, reviews):
        self.title = title
        self.author = author
        self.reviews =reviews
        def add_a_new_review(self, review):
            self.reviews.append(review)
        def count_of_reviews(self):
            return len(self.reviews)
        def display_all_reviews(self):
            for review in self.reviews:
                print(review)
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", ["A masterpiece of American literature.", "A timeless classic."])


book1.display_all_reviews()
print("Total number of reviews:", book1.count_of_reviews())
