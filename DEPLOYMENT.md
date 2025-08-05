# Deployment Guide - Render

This guide will help you deploy the Neighborhood Incident Tracker to Render as a static site.

## 🚀 Quick Deploy (Recommended)

### Option 1: One-Click Deploy
1. Click the "Deploy to Render" button below:
   [![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy/schema-new?schema=render.yaml&repo=https://github.com/natduffy/neighborhood-incident-tracker)

### Option 2: Manual Deploy

#### Step 1: Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Verify your email address

#### Step 2: Connect GitHub Repository
1. In Render dashboard, click "New +"
2. Select "Static Site"
3. Connect your GitHub account if not already connected
4. Select the `neighborhood-incident-tracker` repository

#### Step 3: Configure Deployment
1. **Name**: `neighborhood-incident-tracker` (or your preferred name)
2. **Branch**: `main`
3. **Build Command**: Leave empty (static site)
4. **Publish Directory**: `.` (root directory)
5. **Environment**: `Static Site`

#### Step 4: Deploy
1. Click "Create Static Site"
2. Render will automatically deploy your site
3. Your site will be available at: `https://your-app-name.onrender.com`

## ⚙️ Configuration Files

### render.yaml
- Configures the static site deployment
- Sets up proper headers for different file types
- Routes all traffic to the dynamic viewer by default

### package.json
- Provides metadata for the project
- Includes deployment scripts (for reference)

### index.html
- Landing page with navigation options
- Auto-redirects to dynamic viewer after 5 seconds
- Provides links to different viewer options

## 🔧 Customization

### Change Default Viewer
To change which viewer loads by default, edit `render.yaml`:

```yaml
routes:
  - type: rewrite
    source: /*
    destination: /map_viewer.html  # Change to static viewer
```

### Custom Domain
1. In Render dashboard, go to your static site
2. Click "Settings" → "Custom Domains"
3. Add your domain and follow DNS instructions

### Environment Variables
For future enhancements, you can add environment variables in Render:
1. Go to your static site settings
2. Click "Environment Variables"
3. Add variables like `API_URL`, `DEFAULT_LAT`, `DEFAULT_LON`

## 📱 Mobile Optimization

The application is already mobile-optimized with:
- Responsive design
- Touch-friendly interface
- Optimized map controls
- Fast loading times

## 🔍 Troubleshooting

### Common Issues

1. **Site not loading**
   - Check if the repository is public
   - Verify the branch name is `main`
   - Check Render logs for errors

2. **Map not displaying**
   - Ensure JavaScript is enabled
   - Check browser console for errors
   - Verify internet connection for map tiles

3. **API errors**
   - Check if the API endpoint is accessible
   - Verify CORS settings on the API
   - Check browser network tab for failed requests

### Render Logs
1. Go to your static site in Render dashboard
2. Click "Logs" tab
3. Check for any error messages

## 🌐 Alternative Deployment Options

### Netlify
1. Connect GitHub repository to Netlify
2. Set build command to empty
3. Set publish directory to `.`

### Vercel
1. Import GitHub repository to Vercel
2. Configure as static site
3. Deploy automatically

### GitHub Pages
1. Go to repository settings
2. Enable GitHub Pages
3. Select source branch (main)

## 📊 Performance Monitoring

After deployment, monitor:
- **Page load times** (should be < 3 seconds)
- **API response times** (should be < 2 seconds)
- **User engagement** (time on site, interactions)
- **Error rates** (check browser console)

## 🔄 Continuous Deployment

Render automatically deploys when you:
- Push changes to the `main` branch
- Create pull requests (preview deployments)
- Manually trigger deployments

## 📞 Support

If you encounter issues:
1. Check the [Render documentation](https://render.com/docs)
2. Review the [GitHub repository](https://github.com/natduffy/neighborhood-incident-tracker)
3. Create an issue in the GitHub repository

---

**Note**: This is a static site deployment. The Python script (`filter_incidents.py`) is for local development and data processing. For server-side functionality, consider deploying as a web service. 