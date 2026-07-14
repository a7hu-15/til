# Node.js Destructuring Foot-guns

When importing variables, a tiny syntax error can cause massive cascading 500 errors across an entire platform. 

For example, when using Prisma, importing the instance incorrectly:

```javascript
// Incorrect (destructuring missing)
const prisma = require('./db');

// Correct
const { prisma } = require('./db');
```

Failing to destructure properly means you are trying to call methods on the module exports object rather than the intended Prisma client, leading to `undefined` errors and massive failures in production.
