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

# Deploy app to cloud
git push heroku master

# Make sure you have at least one dyno running
heroku ps:scale web=1

# Return to directory at the start of script
cd -
