from distutils.core import setup
setup(
  name = 'PublicHealthCIs',
  packages = ['PublicHealthCIs'], # this must be the same as the name above
  version = '0.1',
  description = 'A lib to calculate specific confidence intervals that are used in Public Health',
  author = 'Russell Plunkett',
  author_email = 'russ.plunkett@gmail.com',
  url = 'https://github.com/RustyBrain/PublicHealthCIs.git', # use the URL to the github repo
  download_url = 'https://github.com/RustyBrain/PublicHealthCIs/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['confidence interval', 'wilsons', 'byars', 'statistics'], # arbitrary keywords
  classifiers = [],
)