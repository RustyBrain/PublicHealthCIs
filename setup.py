from distutils.core import setup
setup(
    name='public-health-cis',
    packages=['public-health-cis'], # this must be the same as the name above
    version='0.1.1',
    description='A lib to calculate specific confidence intervals that are used in Public Health',
    author='Russell Plunkett',
    author_email='russ.plunkett@gmail.com',
    url='https://github.com/RustyBrain/PublicHealthCIs.git', # use the URL to the github repo
    download_url='https://github.com/RustyBrain/PublicHealthCIs/archive/0.1.1.tar.gz', # I'll explain this in a second
    keywords=['confidence interval', 'wilsons', 'byars', 'statistics'], # arbitrary keywords
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering :: Statistics',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
    ],
)
