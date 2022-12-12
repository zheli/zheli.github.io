## Install/Update bundle
Run `bundle install` or `bundle update` or `bundle update --bundler`

## Local draft mode
Run `bundle exec jekyll serve --draft --livereload` and edit your post in `_drafts` folder.
j
## Local draft mode in Docker
```
docker-compose -f docker-compose.local.yaml up
```

## Publish
Move post from _drafts folder to _posts folder. Rename the file and then commit to github.

## Misc
* Never commit `_site/` folder.
* A good guide: <http://jmcglone.com/guides/github-pages/>
