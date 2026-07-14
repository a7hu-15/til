# Vercel Serverless DevOps: Proxies and Connections

## The Reverse Proxy Rule
Vercel sits in front of your app as a reverse proxy. Because it forwards IP addresses using the `X-Forwarded-For` header, Express will crash things like rate limiters unless you explicitly tell it to trust the proxy:

```javascript
app.set('trust proxy', 1);
```

## Serverless Connections
Serverless environments (like Vercel) aggressively kill idle TCP connections to save money. This causes things like Redis to throw `ClientClosedError`. To solve this, you need to build a bulletproof proxy fallback to manage connections gracefully.
