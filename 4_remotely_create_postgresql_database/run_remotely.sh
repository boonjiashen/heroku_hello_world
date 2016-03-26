# create temporary directory since we need a separate git
# repo for deployment
rm -rf /tmp/app
mkdir -p /tmp/app
cp * /tmp/app
cd /tmp/app

# Create fresh repo due to above reason
git init
git add .
git commit -m 'first commit'

# Create Heroku app and git branch
heroku create  
heroku addons:create heroku-postgresql:hobby-dev  # create database

## Set DATABASE_URL as URL of newly created PSQL DB
#echo -n 'export ' > tmp
#heroku config -s | grep DATABASE_URL >> tmp
#. tmp

git push heroku master  # deploy web app to cloud
echo 'Setting up tables in database...'
heroku run python setup_tables.py  # create tables in database
echo 'Populating tables in database...'
heroku run python populate_tables.py  # insert tuples in tables

# Return to directory at the start of script
cd -
