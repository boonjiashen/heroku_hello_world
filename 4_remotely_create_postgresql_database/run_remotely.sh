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

heroku addons:create heroku-postgresql:hobby-dev

# Set DATABASE_URL as URL of newly created PSQL DB
echo -n 'export ' > tmp
heroku config -s | grep DATABASE_URL >> tmp
. tmp
