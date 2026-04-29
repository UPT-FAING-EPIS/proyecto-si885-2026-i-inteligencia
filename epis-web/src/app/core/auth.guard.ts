import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';

import { AuthClientService } from './auth-client.service';

export const authGuard: CanActivateFn = () => {
  const authService = inject(AuthClientService);
  const router = inject(Router);

  if (authService.isAuthenticated()) {
    return true;
  }

  return router.parseUrl('/login');
};
