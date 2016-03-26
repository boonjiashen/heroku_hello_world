for app in $(heroku apps); do heroku apps:destroy --app $app --confirm $app; done
#Source:
#https://gist.github.com/naaman/1384970
