# Geonames Search

Don't feel like downloading Geonames data, but still need a badly parsed response from Geonames keyword search?

Look no further, this script will give you a response... yep!

After you install the dependencies:

    pip install requests bs4 pandas

Import the directory as a library:

    from geonames_search import *

Then run you query, assigning it to an object:

    df = get_geoname_query_data('search_term', 'country')

Keep in mind: the country digraph is used for country

Licensed under CC-NC-SA.