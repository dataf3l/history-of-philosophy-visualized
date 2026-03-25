# UI Architecture and Implementation Plan: Philosopher Profiles

## Project Context
This UI Plan details the frontend implementation for visualizing structured JSON profiles of philosophers (e.g., Anaximander). The goal is to create a rich, interactive, and visually stunning display that clearly organizes complex philosophical metadata.

## Proposed Stack
- **Frontend Framework**: React, Vue, or Svelte (Single Page Application).
- **Styling**: Vanilla CSS, leveraging a highly customized, premium design system.
- **Routing**: Client-side routing to navigate between different philosophers via cross-links.

## UI/UX Design Aesthetics (CRITICAL)
- **Visuals**: A sleek dark mode layout with "glassmorphism" effects to give a premium, academic, yet modern feel.
- **Typography**: Scholarly but modern fonts (e.g., 'Cinzel' or 'Playfair Display' for headings to evoke historical depth, paired with 'Inter' or 'Roboto' for highly readable body text).
- **Color Palette**: Deep, rich tones (e.g., midnight blues, deep parchment golds, and subdued marble whites) to evoke a sense of history and wisdom.
- **Interactivity**: Smooth expanding/collapsing sections, subtle fade-ins when scrolling, and interactive hover states on philosophical concepts and cross-links.

## Core Features and Component Layout

### 1. Hero Section (Header)
- **Archetypal Summary**: Display the `archetypalSummary` prominently as a sweeping subtitle or stylish blockquote centered at the top.
- **Basic Info**: Large typographic display of the `name`, with `dates`, `regionTradition`, and `schoolMovement` presented elegantly as badges or metadata tags below the name.

### 2. Core Philosophy & Ideas
- **Key Ideas Grid**: A masonry or grid layout of cards for `keyIdeas`. Each card highlights the `concept` as a sub-header, with the `description` below. Hovering over a card could reveal subtle glowing borders to make the concepts feel alive.
- **Core Domains**: An interactive tag cloud or categorized list showing domains (e.g., `Science`, `Metaphysics`) and their associated points.

### 3. The Dialectic (Central Questions & Critiques)
- **Central Questions Panel**: A stylized section highlighting the dialectical nature of philosophy:
  - `problemsAddressed` and `definingTension` on one side to frame the historical problem.
  - `inheritedQuestion` and `bequeathedQuestion` (the ongoing dialogue) on the other.
- **Critiques Section**: A contrasting panel (perhaps slightly darker or using a muted warning tone) clearly outlining `famousObjections` and `internalContradictions` to show the limits of the philosophy.

### 4. Legacy, Influence, and Method
- **Influence Flow**: 
  - Show `influences` flowing into the philosopher.
  - Expand into `impact` (categorized by `immediate`, `longTerm`, and `modernRelevance`). This could be visualized as a structured timeline or a top-to-bottom flow diagram.
- **Method & Style**: A distinct sidebar or callout box detailing their `approach` and `notes`.

### 5. Interactive Knowledge Graph (Cross-Links)
- **Cross-Links Navigation**: The `crossLinks` (e.g., `[[Thales]]`, `[[Apeiron]]`) should be parsed and rendered as interactive pill buttons or hyperlinks that trigger a smooth transition to that related entity's profile or pop open a preview modal.

## Next Steps for the AI Developer
1. **Component Structure**: Break down the JSON into modular components (`<Hero />`, `<IdeaCard />`, `<DialecticPanel />`, `<LegacyTimeline />`, `<CrossLinkList />`).
2. **State Management**: Create a context or store to load the respective philosopher's JSON data when a cross-link is clicked.
3. **Styling Execution**: Write robust vanilla CSS for the grid layouts, responsive breakpoints (mobile-view is critical for text-heavy content), and glassmorphism UI treatments.
4. **Link Parsing**: Implement a markdown/regex parser to convert wiki-style links (`[[Link]]`) found in text into actual navigational elements.
