# Mobile Landing Page Fix - TODO

## Status: [ ] In Progress

### 1. Project Setup & Analysis ✅
- [x] Analyzed `templates/landing.html` (self-contained, responsive CSS present)
- [x] Analyzed `static/style.css` (dashboard-focused, no landing impact)
- [x] Confirmed viewport meta exists, identified potential issues (nav, touch, overflow)

### 2. Create Mobile-Optimized TODO ✅
- [x] This file created

### 3. Fix Mobile Navigation
- [ ] Add hamburger menu for <768px (hide nav-links, toggle JS)
- [ ] Ensure nav-btn/nav-link min-height: 44px (touch target)

### 4. Enhance Viewport & Base Mobile
- [ ] Update viewport: `maximum-scale=5.0, user-scalable=yes`
- [ ] Add `touch-action: manipulation` to interactive elements
- [ ] Body: `overflow-x: hidden; -webkit-overflow-scrolling: touch`

### 5. Hero Section Mobile Fixes
- [ ] Responsive orbs: scale down/constrain @480px (prevent overflow)
- [ ] Hero-stats: better wrap/flex-basis @375px
- [ ] Phone mockup: already hidden OK

### 6. Typography & Fonts
- [ ] Font stack: `'Plus Jakarta Sans', system-ui, -apple-system, sans-serif`
- [ ] Add @supports for font loading

### 7. Media Query Enhancements
- [ ] Add @375px (iPhone): title size, padding tweaks
- [ ] @landscape: hero padding adjust
- [ ] Ensure all buttons >=44px

### 8. JavaScript Mobile Optimizations
- [ ] Debounce scroll listener
- [ ] Mobile menu toggle function
- [ ] IntersectionObserver for sections if perf issue

### 9. Testing
- [ ] Run `python run.py`, test on mobile dev tools (Chrome iPhone/Responsive)
- [ ] Check console/network (fonts, JS errors)
- [ ] Real device test (user to confirm)

### 10. Finalization
- [ ] Update TODO progress
- [ ] attempt_completion with demo command
