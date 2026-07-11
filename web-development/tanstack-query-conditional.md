# Conditional Fetching in TanStack Query

You can use the `enabled` option to prevent a query from running automatically when its dependencies (like a search query string) are empty.

```typescript
const { data, isLoading } = useQuery({
  queryKey: ["search", q],
  queryFn: () => searchService.globalSearch(q),
  enabled: q.trim().length > 0, // only fetch if query is not empty
});
```