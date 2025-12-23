# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

PEACH STUDIO is a creative AI studio based in Everberg, Belgium (Molenstraat 64, 3078 Everberg). This is a plain HTML5 website showcasing the company's products and expertise in AI, creative development, and digital innovation. The company builds products (not services) and provides keynotes on AI and cybersecurity topics. The design is inspired by summate.io's clean aesthetic with a warm peach color palette.

## Technology Stack

- **HTML5**: Semantic markup, no framework
- **CSS3**: Custom styling with modern features (CSS Grid, Flexbox, CSS Variables)
- **No Build Process**: Direct file serving - no compilation needed

## Company Information

- **Name**: PEACH STUDIO
- **Location**: Molenstraat 64, 3078 Everberg, Belgium
- **Domain**: peachstudio.be
- **Email**: info@peachstudio.be
- **Focus Areas** (Product Building):
  - Creative AI & Agentic Development (building AI products and autonomous agents)
  - AI & Cybersecurity Keynotes (thought leadership, not consulting)
  - Business Workflow Automation (building automation products)
  - Game Development (building games and interactive experiences)
  - 3D Art & Design (creating visual assets)
  - Video Production (producing video content)

## File Structure

```
/
├── index.html          # Main HTML file
├── styles.css          # All styles in one file
├── logo.svg           # PEACH STUDIO logo (vectorized)
└── CLAUDE.md          # This file
```

## Design System

### Color Palette
```css
--primary-color: #FF6B35    /* Peach/Orange accent */
--background: #FAF9F7       /* Warm off-white */
--text-primary: #1F1F1F     /* Near black */
--text-secondary: #9CA3AF   /* Gray for subtitles */
```

### Typography
- System font stack for performance
- Heading sizes: 72px (desktop) to 48px (mobile)
- Body text: 18px base with 1.6 line-height
- Font weight: 500 for nav, 600 for cards, 700 for headings

### Spacing System
Based on 8px grid:
- xs: 8px, sm: 16px, md: 24px, lg: 48px, xl: 72px, xxl: 120px

### Border Radius
- Small: 8px, Medium: 12px, Large: 16px

## Key Design Principles

1. **Minimalist**: No JavaScript, no dependencies, pure HTML/CSS
2. **Responsive**: Mobile-first with breakpoint at 768px
3. **Performance**: System fonts, minimal animations, optimized for speed
4. **Accessibility**: Semantic HTML, proper contrast ratios, smooth scroll
5. **Warm Aesthetic**: Peach accent color with subtle gradients

## Development Workflow

### Viewing the Site
Simply open `index.html` in a browser. No build step required.

For live reloading during development:
```bash
# Using Python
python3 -m http.server 8000

# Using Node.js
npx serve

# Using PHP
php -S localhost:8000
```

Then visit `http://localhost:8000`

### Making Changes

**HTML Changes**: Edit `index.html` directly
**Style Changes**: Edit `styles.css` directly
**Logo**: Replace `logo.png` with actual PEACH STUDIO logo

### Site Structure

- **Navigation**: "What We Do" (not "Services"), "About", "Contact"
- **Sections**: Hero → What We Do → Insights & Thought Leadership → About → Contact
- **Main Section ID**: `#focus` (not `#services`)
- **Messaging**: Emphasizes building products and providing keynotes, not selling services
- **Social Links**: Medium blog and LinkedIn integrated in Insights section

### Adding New Sections

Follow the existing pattern:
```html
<section id="new-section" class="new-section">
    <div class="container">
        <h2 class="section-title">Section Title</h2>
        <!-- Content here -->
    </div>
</section>
```

## Important Notes

- **Logo**: SVG vectorized logo at `logo.svg` - fully functional
- **Email**: info@peachstudio.be configured in contact section
- **Business Model**: PEACH STUDIO builds products, not services. They also provide keynotes on AI and cybersecurity topics.
- **Focus Cards**: Six focus area cards with unique gradient backgrounds representing what the company does
- **Content**: Core company information in place - emphasizes product building and thought leadership
- **Focus Area Cards**: Each card has a distinct gradient color scheme:
  - Creative AI & Agentic Development: Purple to blue
  - AI & Cybersecurity Keynotes: Coral to orange (peach theme)
  - Business Workflow Automation: Teal to cyan
  - Game Development: Purple to cream
  - 3D Art & Design: Peach to pink
  - Video Production: Gold to red-orange
- **Insights Section**: Showcases thought leadership with 3 cards:
  - Medium blog (https://medium.com/@vito.rallo)
  - LinkedIn company page (https://www.linkedin.com/company/peachstudiobv)
  - Keynotes & Speaking (links to contact)
  - Features warm peach gradient background and hover effects with SVG icons

## CSS Architecture

Organized top-to-bottom:
1. Reset & Base
2. CSS Variables (`:root`)
3. Global Styles
4. Header
5. Hero Section
6. Work Section
7. About Section
8. Contact Section
9. Footer
10. Responsive (@media queries)
11. Animations (@keyframes)

## Responsive Breakpoints

- Desktop: 1200px max-width container
- Tablet/Mobile: < 768px
  - Stacked navigation
  - Single column grid
  - Reduced spacing

## Animation Details

Subtle animations on hero elements:
- Fade in + slide up effect
- Staggered delays (0s, 0.2s, 0.4s)
- 0.8s duration with ease-out timing

Hover effects:
- Cards lift 8px with shadow
- Buttons lift 2px with enhanced shadow
- Nav links get subtle background tint

## Browser Compatibility

Modern browsers only (Chrome, Firefox, Safari, Edge):
- CSS Grid
- CSS Custom Properties
- Backdrop Filter
- Smooth Scroll

No IE11 support needed.
