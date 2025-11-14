def calculate_annualized_checkouts(book_tuple):
    book_id, genre, publication_year, total_checkouts = book_tuple
    years_since_pub = 2024-publication_year
    
    if years_since_pub == 0:
        return total_checkouts
    return total_checkouts/years_since_pub


def find_most_popular_book(library_data):
    highest_id = ''
    highest_co = 0


    for book in library_data:
        current_co = calculate_annualized_checkouts(book)
        current_book = book[0]

        if current_co > highest_co:
            highest_co = current_co
            highest_id = current_book
        elif current_co == highest_co:
            if current_book < highest_id:
                highest_id = current_book
    

    return highest_id

    
    
    
def get_books_in_genre(library_data, genre_name):
    genre_specified_list = []

    for each_tuple in library_data:
        if genre_name == each_tuple[1]:
            genre_specified_list.append(each_tuple[0])
    
    genre_specified_list.sort()
    return genre_specified_list




def get_genre_circulation_summary(library_data):
    unique_genres = []
    result = []

    for i in range(len(library_data)):
        if library_data[i][1] not in unique_genres:
            unique_genres.append(library_data[i][1])

    for genre in unique_genres:
        total_checkouts = 0
        for book in library_data:
            if genre in book:
                total_checkouts+=book[-1]
        result.append((genre, total_checkouts))

    result.sort()
    return result
            

def analyze_library(library_data):

    most_pop = find_most_popular_book(library_data)

    spec_genre = get_books_in_genre(library_data, "Fantasy")

    summary = get_genre_circulation_summary(library_data)

    return (most_pop, spec_genre, summary)

library_data = [
    ('B101', 'Fantasy', 2001, 506),    # Annualized: 506 / 23 = 22.0
    ('B205', 'Sci-Fi', 1999, 600),     # Annualized: 600 / 25 = 24.0
    ('B102', 'Fantasy', 2015, 207),    # Annualized: 207 / 9 = 23.0
    ('B301', 'Mystery', 2020, 100),    # Annualized: 100 / 4 = 25.0
    ('B206', 'Sci-Fi', 2018, 144),     # Annualized: 144 / 6 = 24.0
]


print(analyze_library(library_data))