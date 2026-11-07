# 🌐 Publish a Website with GitHub Pages

> **Code Therapist Publishing Guide** · **7 November 2026** · Beginner  
> Based on GitHub's official Pages documentation.

## Why use GitHub Pages?

GitHub Pages hosts static websites from repository content. It is useful for documentation, portfolios, frontend demos and project pages. It does **not** run ordinary backend PHP, Python or database servers for you.

```mermaid
flowchart LR
 A[Write index.html] --> B[Commit to repository]
 B --> C[Configure Pages source]
 C --> D[GitHub builds site]
 D --> E[Public website URL]
 E --> F[Review mobile and links]
```

## Beginner checklist

1. Create a new repository or use an existing suitable public repository.
2. Add an `index.html` (or another supported entry file) at the correct publishing location.
3. Open **Settings → Pages** in the repository.
4. Choose the publishing source supported by your repository workflow.
5. Save the configuration and monitor the Pages build.
6. Open the displayed **Visit site** link when deployment completes.
7. Test page navigation, responsiveness, accessibility and HTTPS.

## Sample homepage

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Code Therapist — Learning Notes</title>
  <meta name="description" content="Practical coding guides and technical references.">
</head>
<body>
  <main>
    <h1>Welcome to Code Therapist</h1>
    <p>Read tutorials, open-source guides and software notes.</p>
  </main>
</body>
</html>
```

## Before sharing

| Check | Expected result |
|---|---|
| No secrets committed | API keys and private documents removed |
| Links work | No broken internal navigation |
| Mobile layout | Readable without sideways scrolling |
| Images have descriptions | Meaningful images include alt text |
| Titles describe pages | Visitors understand what each page offers |

Publishing a page does **not** guarantee search-engine indexing or first-page ranking. Build genuinely useful content and monitor search performance if you own the website.

## Official reference

- [GitHub Docs — Creating a GitHub Pages site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site)

---

[← Technical Notes](./README.md) · [← Knowledge Hub](../../README.md) · [Portfolio](https://codetherapist.netlify.app/)
