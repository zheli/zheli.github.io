# Systems Thoughts

A Jekyll 4.x blog site for thoughts on life, startup and software development.

## Prerequisites

- Ruby 3.0 or higher
- Bundler gem (`gem install bundler`)

## Installation & Setup

### Install/Update Dependencies
```bash
# Install all dependencies
bundle install

# Update to latest versions
bundle update

# Update bundler itself
bundle update --bundler
```

## Development

### Local Development Server
```bash
# Start development server with drafts and live reload
bundle exec jekyll serve --draft --livereload

# Start development server on specific port
bundle exec jekyll serve --draft --livereload --port 4000

# Build site without serving
bundle exec jekyll build
```

### Working with Drafts
1. Create your post in the `_drafts/` folder
2. Run `bundle exec jekyll serve --draft --livereload`
3. Edit your post and see changes in real-time
4. When ready to publish, move the file from `_drafts/` to `_posts/` folder

### Docker Development
```bash
# Start local development with Docker
docker-compose -f docker-compose.local.yaml up
```

## Publishing

1. Move your post from `_drafts/` folder to `_posts/` folder
2. Rename the file with the proper date format: `YYYY-MM-DD-title.md`
3. Commit and push to GitHub

## Configuration

- **Jekyll Version**: 4.3.4
- **Ruby Version**: 3.4.0+
- **Markdown**: Kramdown
- **Syntax Highlighter**: Rouge

## Plugins

This site uses the following Jekyll plugins:
- `jekyll-feed` - RSS/Atom feeds
- `jekyll-seo-tag` - SEO optimization
- `jekyll-sitemap` - XML sitemap
- `jekyll-archives` - Archive pages
- `jekyll-mentions` - GitHub-style mentions
- `jekyll-paginate` - Pagination
- `jekyll-redirect-from` - Redirects
- `jemoji` - GitHub-style emoji

## Notes

- Never commit the `_site/` folder (it's in `.gitignore`)
- The site is configured for GitHub Pages deployment
- A good guide: [GitHub Pages with Jekyll](http://jmcglone.com/guides/github-pages/)

## Troubleshooting

If you encounter issues:
1. Make sure you have Ruby 3.0+ installed
2. Run `bundle install` to ensure all dependencies are installed
3. Check that the `csv` gem is available (required for Ruby 3.4+)
4. Clear the `_site/` directory and rebuild if needed
