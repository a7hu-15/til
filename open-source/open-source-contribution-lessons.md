# Lessons Learned from Open Source Contributions

Today, I made three contributions to open-source repositories:
1. **TLG-Start-Page**: Fixed responsive terminal window scaling on mobile screens (<638px) via media queries in globals CSS.
2. **Soterios**: Added a new "Midnight" dark blue theme by defining CSS variables and updating select dropdown dropdowns.
3. **Prompt2Issue**: Added a text search and filter system to search Kanban board card titles and descriptions.

Here are the key lessons learned from these contributions:

## 1. Network Constraints & GitHub API Commits
When cloning large repositories is slow or times out due to network latency, we can use the **GitHub contents API** to perform file lookups, updates, and commits directly on branch trees without ever cloning the repository locally.
- Use `GET /repos/{owner}/{repo}/contents/{path}` to retrieve the file schema and current SHA.
- Modify the file locally.
- Use `PUT /repos/{owner}/{repo}/contents/{path}` with base64 encoded content and branch specs to commit changes.
- Use `gh pr create` via CLI to open the Pull Request.

## 2. Flex-based CSS Layout Responsiveness
Fixed-width layouts (e.g. `width: 40em` on terminal windows) often break on mobile viewports. To make them responsive without modifying JavaScript layout math:
- Wrap them in media queries (`@media (max-width: 638px)`).
- Override rigid width behaviors by setting `width: 100%` and `min-width: 0`.
- Enable scrollable wrappers (`overflow-x: auto` and `word-break: break-word`) to handle long CLI command outputs nicely.

## 3. Designing clean Theme Systems with CSS Variables
Integrating themes is highly clean and modular when using CSS variables:
- Define themes in `:root[data-theme="theme-name"]` blocks using custom properties (e.g., `--bg-base`, `--accent-primary`).
- To allow runtime theme switching, dynamic JS only needs to set the HTML attribute: `document.documentElement.setAttribute('data-theme', themeName)`.
- Make sure to update the select options list in settings pages and allowlist variables in your application configurations.

## 4. Substring Filtering in Local-First Web Apps
In light local-first JS interfaces (like Prompt2Issue), client-side search is fast and efficient:
- Track search queries with a simple reactive state variable (`textFilter`).
- Perform case-insensitive substring checks using `.toLocaleLowerCase("tr")` (critical for handling Turkish characters like dotted/dotless 'I').
- Filter cards array using `cards.filter(c => !textFilter || c.title.toLowerCase().includes(textFilter))` before rendering.
