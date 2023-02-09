import re

movies = [
    {
        "title": "Beetlejuice",
        "year": 1988,
        "genres": ["Comedy", "Fantasy"],
    },
    {
        "title": "The Cotton Club",
        "year": 1984,
        "genres": ["Crime", "Drama", "Music"],
    },
    {
        "title": "The Shawshank Redemption",
        "year": 1994,
        "genres": ["Crime", "Drama"],
    },
    {
        "title": "Crocodile Dundee",
        "year": 1986,

        "genres": ["Adventure", "Comedy"],
    },
    {
        "title": "Valkyrie",
        "year": 2008,
        "genres": ["Drama", "History", "Thriller"],
    },
    {
        "title": "Ratatouille",
        "year": 2007,
        "genres": ["Animation", "Comedy", "Family"],
    },
    {
        "title": "City of God",
        "year": 2002,

        "genres": ["Crime", "Drama"],
    },
    {
        "title": "Memento",
        "year": 2000,

        "genres": ["Mystery", "Thriller"],
    },
    {
        "title": "The Intouchables",
        "year": 2011,

        "genres": ["Biography", "Comedy", "Drama"],
    },
    {
        "title": "Stardust",
        "year": 2007,
        "genres": ["Adventure", "Family", "Fantasy"],
    },
]


def year_sort(arr):
    output = []
    arr.sort(key=lambda x: x['year'])
    arr.reverse()
    for movie in movies:
        output.append(movie["title"])
    return output


def title_sort(arr):
    output = []
    for movie in movies:
        output.append(movie["title"])
    # big ups to this article: https://leancrew.com/all-this/2019/11/the-key-to-sorting-in-python/
    # whose explaination was neeeded and method was adapted to my function via an altered output
    articles = ['a', 'an', 'the']
    punct = re.compile(r'[^\w ]')
    titles = output
    titles = [t.strip() for t in titles]

    def title_key(title):
        s = title.casefold()
        s = punct.sub('', s)
        w = s.split()
        while w[0] in articles:
            w = w[1:] + w[:1]
        return w

    titles.sort(key=title_key)
    return titles
