# CSS Variable Fallbacks

You can provide a fallback value for custom CSS properties (variables) in case they are not defined.

```css
.card {
  /* If --card-bg is not defined, it will fallback to white */
  background-color: var(--card-bg, #ffffff);
}
```
You can also nest variables:
```css
.text {
  color: var(--primary-color, var(--fallback-color, black));
}
```