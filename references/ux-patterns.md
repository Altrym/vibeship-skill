# VibeShip Community UX Patterns

> **Version**: 0.1.0 (seed)  
> **Patterns**: 127  
> **Contributors**: Seed from maintainers — community contributions start now  
> **Last Updated**: 2026-04-01

Every pattern below is a specific UX correction. They are written as instructions because that's what they are — direct fixes for mistakes that AI code generation makes repeatedly. The confirmation count will increase as more users validate each pattern.

Read the categories relevant to your current generation task. You don't need to read all 127 for every task — match categories to the interface you're building.

---

## Interaction (18 patterns)

**INT-001** · Buttons must have three visual states: default, hover, and active/pressed. The active state should feel like the button physically depresses — use `transform: scale(0.97)` or a subtle inset shadow. Without all three states, buttons feel broken.
`confirmations: seed · category: interaction`

**INT-002** · Never use `opacity` changes alone for hover states. Opacity makes elements look disabled. Use background colour shifts, border changes, or shadow additions instead.
`confirmations: seed · category: interaction`

**INT-003** · Transitions should be 150ms for micro-interactions (button hovers, toggles) and 250–300ms for layout changes (panels opening, modals appearing). Below 100ms feels instant and jarring. Above 400ms feels sluggish.
`confirmations: seed · category: interaction`

**INT-004** · When a user clicks a button that triggers an async action, disable the button AND replace the label with a loading indicator ("Saving..." or a spinner). If you only disable without visual change, users think the click didn't register and try again.
`confirmations: seed · category: interaction`

**INT-005** · Modals must close on Escape key press AND clicking the backdrop. Every generated modal misses at least one of these. Also: focus should trap inside the modal while it's open.
`confirmations: seed · category: interaction`

**INT-006** · Dropdown menus should open on click, not hover. Hover-triggered dropdowns are unusable on touch devices and cause accidental triggers on desktop when the cursor passes over on the way to something else.
`confirmations: seed · category: interaction`

**INT-007** · Toggle switches need an immediate visual change. Don't wait for an API response to flip the toggle — flip it optimistically and revert if the request fails. Toggling that waits for a server response feels like a broken switch.
`confirmations: seed · category: interaction`

**INT-008** · After a drag-and-drop operation, highlight the dropped item briefly (200ms glow or background flash) so the user can confirm it landed where they intended.
`confirmations: seed · category: interaction`

**INT-009** · Tooltips should appear after a 300ms delay, not instantly. Instant tooltips fire constantly as the cursor moves across the page. They should also disappear immediately when the cursor leaves (no exit delay).
`confirmations: seed · category: interaction`

**INT-010** · Selection interactions (checkboxes, multi-select) should show a count of selected items and provide a "Select all" / "Deselect all" action when more than 5 items exist.
`confirmations: seed · category: interaction`

**INT-011** · Click targets should extend beyond the visible element. A small icon button (24×24px) should have a click area of at least 44×44px using padding, not visible size.
`confirmations: seed · category: interaction`

**INT-012** · Search inputs should filter as-you-type with a debounce of 200–300ms. Don't require pressing Enter. If the search hits an API, show a subtle loading indicator inside the input field (replacing the search icon with a spinner).
`confirmations: seed · category: interaction`

**INT-013** · Tab interfaces should animate the content transition. A simple `opacity` crossfade (150ms) prevents the jarring "jump" of instant content swaps. The active tab indicator should also animate its position (sliding underline, not instant jump).
`confirmations: seed · category: interaction`

**INT-014** · Accordion/collapsible sections should animate height changes smoothly. Use `grid-template-rows: 0fr` to `1fr` with a transition for smooth height animation without JavaScript height calculation hacks.
`confirmations: seed · category: interaction`

**INT-015** · Scroll-linked animations must respect `prefers-reduced-motion`. Wrap all scroll-triggered effects in `@media (prefers-reduced-motion: no-preference)`. Without this, motion-sensitive users can't use your interface.
`confirmations: seed · category: interaction`

**INT-016** · Copy-to-clipboard buttons should: (a) show a checkmark or "Copied!" confirmation for 2 seconds, (b) revert to the original state, (c) work without HTTPS on localhost. Use the `navigator.clipboard` API with a fallback `textarea` hack.
`confirmations: seed · category: interaction`

**INT-017** · Swipe gestures on mobile should have a visible threshold indicator. If swiping left reveals a delete action, show a progressive red background that intensifies as the swipe crosses the commit threshold.
`confirmations: seed · category: interaction`

**INT-018** · Double-click-to-edit patterns must also support a visible "edit" button for discoverability. Hidden interaction patterns are invisible to new users, touch users, and screen reader users.
`confirmations: seed · category: interaction`

---

## Layout (16 patterns)

**LAY-001** · Never use `100vh` for full-height layouts on mobile. Mobile browsers have a dynamic toolbar that changes viewport height. Use `100dvh` (dynamic viewport height) or `min-height: 100svh` as fallback.
`confirmations: seed · category: layout`

**LAY-002** · Cards in a grid should be equal height within each row. Use `display: grid` with `grid-template-rows: subgrid` or ensure card content uses flex with `flex-grow: 1` on the body section so CTAs align at the bottom.
`confirmations: seed · category: layout`

**LAY-003** · Sidebar layouts must collapse to a hamburger menu on viewports below 768px. The sidebar should overlay (not push) the content on mobile, with a semi-transparent backdrop behind it.
`confirmations: seed · category: layout`

**LAY-004** · Sticky headers must not cover content when the page loads with a URL hash (`#section`). Add `scroll-margin-top` equal to the header height on all potential anchor targets.
`confirmations: seed · category: layout`

**LAY-005** · Table layouts should switch to a card/stacked layout on mobile. Never make tables horizontally scrollable as the primary mobile strategy — users don't discover horizontal scroll. If the table is the primary content, transform each row into a card.
`confirmations: seed · category: layout`

**LAY-006** · Content containers should have a max-width (1200px–1400px for full layouts, 720px for reading content). Full-width content on a 27" monitor is unreadable and looks broken.
`confirmations: seed · category: layout`

**LAY-007** · Multi-column form layouts should collapse to single column at 640px. Two-column forms on narrow screens force cramped inputs that are frustrating to fill.
`confirmations: seed · category: layout`

**LAY-008** · Fixed/sticky elements (headers, FABs, bottom navs) must account for iOS safe areas. Use `padding-bottom: env(safe-area-inset-bottom)` on bottom-positioned elements to avoid the home indicator overlap.
`confirmations: seed · category: layout`

**LAY-009** · When a page has a primary action and secondary content (e.g., article + sidebar), the primary content column should be at least 60% of the width. Never give the sidebar equal or greater width than the main content.
`confirmations: seed · category: layout`

**LAY-010** · Modal/dialog widths should be: small (400px) for confirmations, medium (560px) for forms, large (720px) for complex content. Never use full-screen modals on desktop — that's a page, not a modal.
`confirmations: seed · category: layout`

**LAY-011** · Padding inside cards should be 16px minimum on mobile and 24px on desktop. Cards with 8px or 12px padding look cramped and unfinished.
`confirmations: seed · category: layout`

**LAY-012** · Space between sections should be visually larger than space between items within a section. If items within a section have 16px gap, sections should have at least 40px gap. This is the most common visual hierarchy failure in AI-generated layouts.
`confirmations: seed · category: layout`

**LAY-013** · Hero sections should not push all meaningful content below the fold. If the hero is purely decorative, limit it to 60vh maximum. Users who land from a search result want to see content, not a giant image.
`confirmations: seed · category: layout`

**LAY-014** · When a list/grid has a "load more" or pagination mechanism, preserve the user's scroll position. Clicking "page 2" should scroll to the top of the list, not the top of the page.
`confirmations: seed · category: layout`

**LAY-015** · Z-index values should use a defined scale: base content (0), sticky elements (10), dropdowns (20), modals/overlays (30), toasts/notifications (40). Never use arbitrary large numbers like `z-index: 9999`.
`confirmations: seed · category: layout`

**LAY-016** · Aspect ratios on images and video containers should use `aspect-ratio` CSS property to prevent layout shift during loading. Never rely on the image's natural dimensions alone.
`confirmations: seed · category: layout`

---

## Typography (12 patterns)

**TYP-001** · Body text must be 16px minimum. This is not a suggestion. On mobile, 14px body text causes eye strain and increases bounce rate. The single most impactful UX fix across all AI-generated interfaces.
`confirmations: seed · category: typography`

**TYP-002** · Line height for body text should be 1.5 to 1.7. For headings, 1.1 to 1.3. Headings with body-text line height have awkward gaps between lines. Body text with heading line height is unreadable.
`confirmations: seed · category: typography`

**TYP-003** · Limit paragraph width to 65–75 characters (roughly `max-width: 65ch`). Wide text blocks cause readers to lose their place when returning to the next line.
`confirmations: seed · category: typography`

**TYP-004** · Use `font-display: swap` on all `@font-face` declarations and Google Font imports. Without it, text is invisible during font loading (FOIT), which makes the page feel broken for 200–500ms.
`confirmations: seed · category: typography`

**TYP-005** · Heading hierarchy must be strictly sequential. Never jump from `h2` to `h4`. Screen readers and search engines depend on heading levels for document structure.
`confirmations: seed · category: typography`

**TYP-006** · Bold text within a paragraph should use `font-weight: 600` (semibold), not `700` (bold). Full bold within body text is visually aggressive and disrupts reading flow. Reserve `700` for headings.
`confirmations: seed · category: typography`

**TYP-007** · Monospace text (code snippets, IDs, file paths) should have a slightly smaller font size than surrounding body text (0.9em) and a subtle background colour to distinguish it.
`confirmations: seed · category: typography`

**TYP-008** · All-caps text should use `letter-spacing: 0.05em` to 0.1em. Without letter spacing, uppercase text feels cramped and is harder to read. Apply this to labels, badges, and section headers.
`confirmations: seed · category: typography`

**TYP-009** · Numbers in data displays (dashboards, prices, stats) should use `font-variant-numeric: tabular-nums` so digits align vertically in columns and don't shift width as values change.
`confirmations: seed · category: typography`

**TYP-010** · Truncated text (`text-overflow: ellipsis`) must have a mechanism to see the full text — usually a tooltip on hover or expansion on click. Truncation without access to the full content is data loss.
`confirmations: seed · category: typography`

**TYP-011** · Error messages should use `font-weight: 500` and a red colour that passes contrast checks against its background — typically `#dc2626` on white or `#fca5a5` on dark backgrounds. Never use light pink (#fecaca) for error text — it's unreadable.
`confirmations: seed · category: typography`

**TYP-012** · Price and currency displays: the currency symbol should be the same size as the digits or slightly smaller. Never display prices without the currency symbol/code, even when it "seems obvious" from context.
`confirmations: seed · category: typography`

---

## Forms (15 patterns)

**FRM-001** · Labels go ABOVE inputs, not beside them and never as placeholder-only. Placeholder text disappears when the user starts typing, removing the label entirely. This is the most common form UX failure in AI-generated code.
`confirmations: seed · category: forms`

**FRM-002** · Error validation should happen on blur (when the user leaves the field), not on every keystroke. Keystroke validation shows errors while the user is still typing, which is stressful and distracting.
`confirmations: seed · category: forms`

**FRM-003** · After form submission fails with validation errors, focus the first field with an error. Don't just show red text — programmatically move focus so keyboard and screen reader users land on the problem.
`confirmations: seed · category: forms`

**FRM-004** · Password fields need a show/hide toggle. Every single time. No exceptions. Place it inside the input field on the right side as an eye icon.
`confirmations: seed · category: forms`

**FRM-005** · Multi-step forms must show a progress indicator (step 2 of 4) and allow going back to previous steps without losing data. Never clear previous steps on back navigation.
`confirmations: seed · category: forms`

**FRM-006** · Date inputs should use the native `<input type="date">` where possible. Custom date pickers are almost always worse than the native one on mobile. If a custom picker is necessary (date ranges, blackout dates), always also accept typed input.
`confirmations: seed · category: forms`

**FRM-007** · Textarea fields for long-form input should auto-grow in height as the user types (up to a max-height with scroll). Fixed-height textareas that start at 3 rows force the user to write inside a tiny window.
`confirmations: seed · category: forms`

**FRM-008** · Select/dropdown fields with more than 15 options need a search/filter mechanism. Scrolling through 50 country names in a native `<select>` is not acceptable UX.
`confirmations: seed · category: forms`

**FRM-009** · Form field groups (name, address, payment) should have visual grouping with subtle borders or background colours and a group label. A flat list of 12 ungrouped fields is overwhelming.
`confirmations: seed · category: forms`

**FRM-010** · File upload inputs should: show accepted file types, show max file size, preview the file after selection (images as thumbnails, documents as filename + size), and have a "remove" button.
`confirmations: seed · category: forms`

**FRM-011** · Required field indicators should use an asterisk (*) next to the label with a note at the top of the form: "* Required". Alternatively, mark optional fields with "(optional)" if most fields are required.
`confirmations: seed · category: forms`

**FRM-012** · Auto-save in long forms should: save silently in the background, show a subtle "Saved" indicator with timestamp, and NOT show a toast/notification every time (toast fatigue).
`confirmations: seed · category: forms`

**FRM-013** · Phone number inputs should accept any format and parse programmatically. Don't force users to type numbers without spaces or dashes. Use `inputmode="tel"` for the numeric keypad on mobile.
`confirmations: seed · category: forms`

**FRM-014** · Inline form validation checkmarks (green ✓ when valid) give positive reinforcement and reduce submission anxiety. Show them on fields as the user completes them correctly.
`confirmations: seed · category: forms`

**FRM-015** · Never clear a form after a failed submission. This is data destruction. If the server rejects the form, show errors but keep all user input intact. The user should only need to fix the specific problem.
`confirmations: seed · category: forms`

---

## Empty & Loading States (11 patterns)

**EMP-001** · Empty states should contain three things: (a) a brief explanation of what belongs here, (b) a visual (illustration or icon), and (c) a primary action to create the first item. Never show a blank container with just "No items found."
`confirmations: seed · category: empty-states`

**EMP-002** · Loading skeletons should match the shape of the actual content. A card grid should show skeleton cards. A table should show skeleton rows. Generic spinners are acceptable for full-page loads, but never for partial content loading within a page.
`confirmations: seed · category: empty-states`

**EMP-003** · Skeleton loading should have a subtle shimmer/pulse animation to indicate activity. A static grey rectangle looks like a rendering bug, not a loading state.
`confirmations: seed · category: empty-states`

**EMP-004** · Error states should: (a) explain what went wrong in plain language (not error codes), (b) offer a specific recovery action ("Try again", "Refresh", "Go back"), and (c) never blame the user ("Invalid input" → "Please enter a valid email address").
`confirmations: seed · category: empty-states`

**EMP-005** · Search results with zero matches should suggest: (a) checking spelling, (b) trying different keywords, (c) browsing categories, or (d) clearing filters. "No results found" alone is a dead end.
`confirmations: seed · category: empty-states`

**EMP-006** · First-time user experiences should show contextual tips or a brief walkthrough, not a full-screen tutorial that blocks the interface. Tooltips pointing to key features (dismissible, 3–4 max) beat a 5-step onboarding modal.
`confirmations: seed · category: empty-states`

**EMP-007** · If data is loading but you already have stale/cached data, show the stale data with a "Refreshing..." indicator rather than replacing it with a loading skeleton. Stale data is better than no data.
`confirmations: seed · category: empty-states`

**EMP-008** · Offline states should: (a) clearly indicate the app is offline, (b) specify what still works and what doesn't, (c) auto-reconnect without the user needing to manually refresh.
`confirmations: seed · category: empty-states`

**EMP-009** · Long-running operations (file processing, report generation) should show a progress indicator with estimated time remaining or a step counter, not an indefinite spinner. Users abandon pages with indefinite spinners after 8–10 seconds.
`confirmations: seed · category: empty-states`

**EMP-010** · "Permission denied" or "unauthorised" states should explain what access is needed and who can grant it, with a direct action like "Request access" or "Contact admin." Never just show a lock icon and "Access denied."
`confirmations: seed · category: empty-states`

**EMP-011** · Lists with pagination should show the total count ("Showing 1–20 of 347 results") so users understand the scale of results and can decide whether to filter more narrowly.
`confirmations: seed · category: empty-states`

---

## Mobile (12 patterns)

**MOB-001** · Primary actions belong in the thumb zone (bottom half of screen on mobile). Navigation bars at the bottom, FABs in the bottom-right. Critical CTAs that only live at the top of the page are unreachable with one hand.
`confirmations: seed · category: mobile`

**MOB-002** · Touch targets must be minimum 44×44px. This is Apple's Human Interface Guideline and Google's Material Design spec. Small touch targets are the number one mobile usability failure.
`confirmations: seed · category: mobile`

**MOB-003** · On mobile, replace hover-dependent interactions with tap alternatives. No content should be accessible only via hover — hover doesn't exist on touchscreens.
`confirmations: seed · category: mobile`

**MOB-004** · Input fields on mobile should use the correct `inputmode`: `numeric` for PIN codes, `tel` for phone numbers, `email` for email addresses, `url` for URLs, `search` for search fields. This controls which keyboard appears.
`confirmations: seed · category: mobile`

**MOB-005** · Fixed bottom bars (nav, CTAs) must add `padding-bottom: env(safe-area-inset-bottom)` for notched iPhones. Without this, the home indicator overlaps your buttons.
`confirmations: seed · category: mobile`

**MOB-006** · Image carousels on mobile should show partial visibility of the next slide (peek) to indicate swipeability. A full-width slide with dots below gives no affordance that swiping works.
`confirmations: seed · category: mobile`

**MOB-007** · Pull-to-refresh should only be implemented if the content is time-sensitive (feeds, messages). For static content, pull-to-refresh creates confusion about whether data actually changed.
`confirmations: seed · category: mobile`

**MOB-008** · Multi-column grids on mobile should collapse to 1 column at 480px and 2 columns at 640px. Three columns on a phone screen make each item too small to read or tap.
`confirmations: seed · category: mobile`

**MOB-009** · When a mobile keyboard opens, the focused input should scroll into view above the keyboard. If using `position: fixed` elements, they will likely cover the input — handle this explicitly.
`confirmations: seed · category: mobile`

**MOB-010** · Bottom sheets are preferable to modals on mobile. They feel native, can be dismissed by swiping down, and don't obscure the entire screen. Reserve full-screen modals for complex flows.
`confirmations: seed · category: mobile`

**MOB-011** · Long lists on mobile should use `scroll-snap-type` or section headers with a sticky position so users maintain context while scrolling through many items.
`confirmations: seed · category: mobile`

**MOB-012** · Landscape orientation should work, even if portrait is the primary design target. At minimum, content shouldn't overflow, overlap, or become inaccessible when the phone rotates.
`confirmations: seed · category: mobile`

---

## Accessibility (13 patterns)

**A11Y-001** · Focus indicators must be visible. Never use `outline: none` without providing a custom focus style. Use `outline: 2px solid` with a colour that contrasts against both light and dark backgrounds (e.g., a blue ring with a white offset).
`confirmations: seed · category: accessibility`

**A11Y-002** · Icon-only buttons (hamburger menu, close, settings gear) MUST have `aria-label` describing the action: `aria-label="Open menu"`, `aria-label="Close dialog"`, `aria-label="Settings"`.
`confirmations: seed · category: accessibility`

**A11Y-003** · Colour must never be the sole indicator of state. Red for error, green for success — always pair with an icon (✓ for success, ✕ for error) or text. 8% of men are colour blind.
`confirmations: seed · category: accessibility`

**A11Y-004** · Dynamic content changes (toast notifications, inline errors, live counters) need `aria-live="polite"` or `role="status"` so screen readers announce them. Without this, dynamic updates are invisible to non-sighted users.
`confirmations: seed · category: accessibility`

**A11Y-005** · Skip navigation link: every page with a header/nav should have a visually hidden "Skip to main content" link as the first focusable element. It becomes visible on focus for keyboard users.
`confirmations: seed · category: accessibility`

**A11Y-006** · Form error summaries should use `role="alert"` to immediately announce to screen readers when validation fails after submission.
`confirmations: seed · category: accessibility`

**A11Y-007** · Tables need `<th>` elements with `scope="col"` or `scope="row"`. Without proper table headers, screen readers read data tables as meaningless number sequences.
`confirmations: seed · category: accessibility`

**A11Y-008** · Custom controls (toggles, sliders, star ratings, drag-and-drop) must expose their state via ARIA: `aria-checked` for toggles, `aria-valuenow` for sliders, `aria-selected` for selectable items.
`confirmations: seed · category: accessibility`

**A11Y-009** · All functionality must be reachable via keyboard: Tab to navigate, Enter/Space to activate, Escape to dismiss, Arrow keys to navigate within components (tabs, menus, radio groups).
`confirmations: seed · category: accessibility`

**A11Y-010** · `tabindex="-1"` for programmatic focus targets (modal containers, error summaries). `tabindex="0"` for custom interactive elements. Never use `tabindex` values above 0 — they break natural tab order.
`confirmations: seed · category: accessibility`

**A11Y-011** · Decorative images use `alt=""` (empty string, not omitted). Informative images have alt text describing what the image conveys. Functional images (icons that are links) have alt text describing the action, not the image.
`confirmations: seed · category: accessibility`

**A11Y-012** · Text contrast: minimum 4.5:1 for normal text, 3:1 for large text (18px bold or 24px regular). Use https://webaim.org/resources/contrastchecker/ to verify. The most commonly failed contrast: light grey placeholder text.
`confirmations: seed · category: accessibility`

**A11Y-013** · Motion and animation: always wrap in `@media (prefers-reduced-motion: no-preference)`. Users with vestibular disorders can be physically sickened by scroll-jacking, parallax, or large-scale animations.
`confirmations: seed · category: accessibility`

---

## Feedback & Microcopy (11 patterns)

**FBK-001** · Success messages after form submission should confirm WHAT was saved: "Project 'Q2 Report' saved" not just "Saved successfully." Users need confirmation that the right thing happened, not just that something happened.
`confirmations: seed · category: feedback`

**FBK-002** · Destructive action confirmations should name the thing being destroyed: "Delete project 'Q2 Report'? This cannot be undone." Generic "Are you sure?" modals don't help the user evaluate the risk.
`confirmations: seed · category: feedback`

**FBK-003** · Toast/snackbar notifications should auto-dismiss after 4–5 seconds for success messages. Error toasts should persist until manually dismissed — the user may need to read and act on them.
`confirmations: seed · category: feedback`

**FBK-004** · Button labels should describe the outcome, not the action: "Create account" not "Submit", "Save changes" not "OK", "Delete project" not "Confirm". The user should know what happens before they click.
`confirmations: seed · category: feedback`

**FBK-005** · Placeholder text should show format examples, not repeat the label: for a date field labelled "Start date", use placeholder `DD/MM/YYYY` not `Enter start date`.
`confirmations: seed · category: feedback`

**FBK-006** · Validation error messages should tell the user how to fix the problem: "Password must be at least 8 characters" not "Invalid password". "Enter a valid email (e.g., name@company.com)" not "Invalid email format".
`confirmations: seed · category: feedback`

**FBK-007** · When a feature is locked behind a plan/permission, the message should name the plan required AND provide a direct upgrade/request path. "Available on Pro plan — Upgrade" not "Feature unavailable."
`confirmations: seed · category: feedback`

**FBK-008** · Relative timestamps ("3 minutes ago", "yesterday") are more scannable than absolute timestamps for recent events. Switch to absolute format for events older than 7 days. Show the full absolute timestamp in a tooltip.
`confirmations: seed · category: feedback`

**FBK-009** · Confirmation of account/settings changes should persist visibly for at least 3 seconds, not flash briefly. Users who click "Save" and then glance away need to see the confirmation when they look back.
`confirmations: seed · category: feedback`

**FBK-010** · "Undo" is better than "Are you sure?" for low-risk destructive actions (archiving, removing from list, dismissing). Show a brief undo toast instead of a pre-action confirmation dialog. Reserve confirmation dialogs for truly irreversible actions.
`confirmations: seed · category: feedback`

**FBK-011** · When the user performs a bulk action (delete 12 items, export 50 records), show the count in the confirmation AND the result: "12 items deleted" or "Exporting 50 records... (23%)".
`confirmations: seed · category: feedback`

---

## Navigation & Wayfinding (9 patterns)

**NAV-001** · The current page/section must always be visually indicated in the navigation. Active nav items should differ from inactive ones via background colour, font weight, or an indicator bar — not just a colour change that could be missed.
`confirmations: seed · category: navigation`

**NAV-002** · Breadcrumbs should be present on any page that is 3+ levels deep in a hierarchy. The current page in the breadcrumb trail should not be a link — it's where you already are.
`confirmations: seed · category: navigation`

**NAV-003** · External links should open in a new tab (`target="_blank"` with `rel="noopener noreferrer"`) and have a subtle external link icon (↗) indicating they'll leave the current site.
`confirmations: seed · category: navigation`

**NAV-004** · Anchor links / table of contents for long pages should highlight the currently visible section as the user scrolls (scroll spy). This is expected behaviour and its absence feels like a bug.
`confirmations: seed · category: navigation`

**NAV-005** · 404 pages should: (a) confirm the URL doesn't exist, (b) suggest similar pages or a search, (c) link to the homepage. Never show a blank screen or a technical error page.
`confirmations: seed · category: navigation`

**NAV-006** · After completing a multi-step flow (checkout, onboarding, wizard), the final step should have a clear "what happens next" — where will they land, what should they expect, and what action they can take.
`confirmations: seed · category: navigation`

**NAV-007** · Deep links should work. If a user copies the URL from any state of the application (filtered list, open modal, specific tab), pasting that URL should restore that state. Use URL search params or hash fragments.
`confirmations: seed · category: navigation`

**NAV-008** · Mobile hamburger menus should animate open (slide from left or expand from the icon) and have a clear close mechanism (X button AND tapping outside). The hamburger icon should animate into the X.
`confirmations: seed · category: navigation`

**NAV-009** · "Back" navigation should take you to your previous context with its state preserved, not to a default/root view. If a user was on a filtered, paginated list, back should restore that exact view.
`confirmations: seed · category: navigation`

---

## Design & Visual Polish (10 patterns)

**DES-001** · Box shadows should use multiple layered shadows for depth, not a single heavy shadow. Two or three shadows with increasing blur and offset look more natural: `box-shadow: 0 1px 2px rgba(0,0,0,0.05), 0 4px 12px rgba(0,0,0,0.1)`.
`confirmations: seed · category: design`

**DES-002** · Border radius should be consistent across the interface. Pick a system: 4px for small elements (badges), 8px for medium (inputs, cards), 12–16px for large (modals, panels). Mixing 4px, 6px, 8px, 10px randomly looks undesigned.
`confirmations: seed · category: design`

**DES-003** · Use CSS custom properties for all colours, not hardcoded values. Define a palette with semantic names: `--color-primary`, `--color-error`, `--color-text`, `--color-text-secondary`, `--color-surface`, `--color-border`. This enables theming and dark mode.
`confirmations: seed · category: design`

**DES-004** · Dark mode must be designed, not inverted. Don't just swap black and white. Dark surfaces should be dark grey (#1a1a2e, #16161a), not pure black (#000000). Elevated surfaces should be lighter than the background (opposite of light mode).
`confirmations: seed · category: design`

**DES-005** · Borders should be subtle: 1px solid with a colour close to the background (e.g., `#e5e7eb` on white, `#2a2a32` on dark). Heavy borders (2px+, high contrast) make interfaces look dated and cluttered.
`confirmations: seed · category: design`

**DES-006** · Icons within the same interface should come from one icon set and be the same size/weight. Mixing outlined and filled icons, or icons from different sets, creates visual dissonance.
`confirmations: seed · category: design`

**DES-007** · Status colours must be semantic and consistent: green for success/active, amber/yellow for warning/pending, red for error/destructive, blue for informational. Never use red for a non-destructive primary action.
`confirmations: seed · category: design`

**DES-008** · Avatar/profile image placeholders should show the user's initials on a coloured background (colour derived from name hash for consistency), not a generic grey person icon.
`confirmations: seed · category: design`

**DES-009** · Notification badges (unread count dots) should be positioned at the top-right of the icon they relate to, using `position: absolute` with a negative offset. They should use minimum width with pill-shape (`min-width: 18px; border-radius: 9px`) so single and double digits both look correct.
`confirmations: seed · category: design`

**DES-010** · Dividers between sections should use `border-top` or `border-bottom` on the element, not a separate `<hr>` element with margin. This produces cleaner spacing and fewer DOM elements. When in doubt, use whitespace instead of a visible divider.
`confirmations: seed · category: design`

---

## How To Contribute New Patterns

If you've corrected a UX issue in generated code and it seems like a pattern others would hit:

1. Run `/vibeship-capture` in your Claude Code session or check `learnings/local-corrections.jsonl`
2. Run `python scripts/contribute.py` to submit
3. Maintainers review and merge confirmed patterns

**What makes a good pattern:**
- Specific enough to be actionable (not "make it look better")
- Universal enough to apply across different projects
- Corrects a real mistake, not a personal preference
- Includes the reasoning (why the correction matters for users)

**What doesn't belong:**
- Brand-specific style preferences
- Framework-specific API choices (use X library over Y)
- Content/copywriting for specific domains
- Performance optimizations (separate concern from UX)
