var staticCacheName = 'djangopwa-v1';

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(staticCacheName).then(function(cache) {
      return cache.addAll([
        // '/base_layout',
        // 'static/assets/img/favicon.png',
        // 'static/assets/img/apple-touch-icon.png',
        // 'static/assets/img/news-4.jpg',
        '',
      ]);
    })
  );
});

// Clear cache on activate
self.addEventListener('activate', event => {
  event.waitUntil(
      caches.keys().then(cacheNames => {
          return Promise.all(
              cacheNames
                  .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                  .filter(cacheName => (cacheName !== staticCacheName))
                  .map(cacheName => caches.delete(cacheName))
          );
      })
  );
});

self.addEventListener('fetch', function(event) {
  var requestUrl = new URL(event.request.url);
    if (requestUrl.origin === location.origin) {
      if ((requestUrl.pathname === '/')) {
        event.respondWith(caches.match('/base_layout'));
        return;
      }
    }
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
});

