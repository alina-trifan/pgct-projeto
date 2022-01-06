from pybliometrics.scopus import AbstractRetrieval, AuthorRetrieval, AffiliationRetrieval

#AbstractRetrieval

ab = AbstractRetrieval("10.1016/j.softx.2019.100263")

print(ab.title)
print(ab.publicationName)
print(ab.authors)
#[Author(auid=57209617104, indexed_name='Rose M.E.', surname='Rose',
# given_name='Michael E.', affiliation='60105007'),
# Author(auid=7004212771, indexed_name='Kitchin J.R.', surname='Kitchin',
# given_name='John R.', affiliation='60027950')]

#AuthorRetrieval

au2 = AuthorRetrieval(ab.authors[1].auid)
print(au2.h_index)

au1 = AuthorRetrieval(ab.authors[0].auid)
print(au1.affiliation_current)

#[Affiliation(id=60105007, parent=None, type='parent', relationship='author',
# afdispname=None, preferred_name='Max Planck Institute for Innovation and Competition',
# parent_preferred_name=None, country_code='deu', country='Germany',
# address_part='Marstallplatz 1', city='Munich', state='Bayern',
# postal_code='80539', org_domain='ip.mpg.de', org_URL='http://www.ip.mpg.de/')]

# Affiliation information

aff1 = AffiliationRetrieval(au1.affiliation_current[0].id)
print(aff1.author_count)
