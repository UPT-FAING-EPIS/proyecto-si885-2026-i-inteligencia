import { HttpInterceptorFn } from '@angular/common/http';
import { inject } from '@angular/core';

import { AuthClientService } from './auth-client.service';

export const authInterceptor: HttpInterceptorFn = (request, next) => {
  const authService = inject(AuthClientService);
  const token = authService.getAccessToken();

  if (!token || !request.url.includes('/api/dashboard')) {
    return next(request);
  }

  return next(
    request.clone({
      setHeaders: {
        Authorization: `Bearer ${token}`,
      },
    }),
  );
};
