# React useEffect Cleanup

If you set up a subscription or a timer in `useEffect`, return a cleanup function to prevent memory leaks.

```javascript
useEffect(() => {
  const timer = setInterval(() => console.log('Tick'), 1000);
  return () => clearInterval(timer);
}, []);
```